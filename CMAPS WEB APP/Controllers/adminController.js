const CaseModel = require('../models/caseModel');
const offenceCategoryModel = require('../models/offenceCategoryModel');
const User = require('../models/userModel');
const bcrypt = require('bcryptjs');
var path   = require('path');
var XLSX = require('xlsx');


module.exports= {
    //To display Dashboard of Admin Portal
    index: (req,res) => {           
        CaseModel.countDocuments().then(count => {
            User.countDocuments().then(users => {
                res.render('Admin/index', {
                    caseCount: count,
                    userCount: users,
                    users: users
                });        
            })
        })
    },
 
    //To display Cases List
    
    getCases: (req,res) => {
         CaseModel.find((err, docs) => {
             if(!err){
                 res.render('Admin/Cases/index', {
                    list: docs                     
                 });
             }
             else{
                 console.log('error in getting documents of db' +err);
             }
         });
    },

    //To Export Cases List to excel sheet
    exportToCsv: (req, res) => {
        var wb = XLSX.utils.book_new(); //new workbook
        CaseModel.find((err,data)=>{
            if(err){
                console.log(err)
            }else{
                var temp = JSON.stringify(data);
                temp = JSON.parse(temp);
                var ws = XLSX.utils.json_to_sheet(temp);
                var down ='E:/CMAP-WEB-APPLICATION/cases.csv'
               XLSX.utils.book_append_sheet(wb,ws,"sheet1");
               XLSX.writeFile(wb,down);
               res.download(down);
            }
        });
        req.flash('success-message','File Exported');
        res.redirect('/admin/cases');

    },

    //To display Create New Case Form
    createCase: (req,res) => {
        offenceCategoryModel.find().then(cats => {

            res.render('Admin/Cases/create', {categories: cats});
      });
    },

    //To Enter New Case
    submitCases: (req, res) => { 
      const newCase = new CaseModel({
            Posting: req.body.posting,
            Latitudes: req.body.latitudes,
            Longitudes: req.body.longitudes,
            Date: req.body.date,
            Month: req.body.month,
            Year: req.body.year,
            Day: req.body.day,
            Time: req.body.time,
            Offences: req.body.offences,
            OffenceCategory: req.body.offenceCategory,
            PartOfTheDay: req.body.partOfTheDay,
        });
   
        newCase.save().then(Case => {
            req.flash('success-message', `Case Added.`);
            res.redirect('/admin/cases/create');
        }).catch(err => {
            console.log(err);
        })
    },

    //To display Edit Case Form
    editCase: (req,res) => { //get route to show form filled with data when click edit in the list
        const id = req.params.id;

        CaseModel.findById(id)
        .then(CaseObj => {

            offenceCategoryModel.find().then(cats => {
                res.render('Admin/Cases/edit', {CaseObj: CaseObj, categories: cats});
            })

        });

    }, 

    //To update a Case
    editUpdateCase: (req, res) => {
        const id = req.params.id;

        CaseModel.findById(id)
        .then(CaseObj => {
            CaseObj.Posting = req.body.posting;
            CaseObj.Date = req.body.date;
            CaseObj.Month = req.body.month;
            CaseObj.Year = req.body.year;
            CaseObj.Day = req.body.day;
            CaseObj.Time = req.body.time;
            CaseObj.Offences = req.body.offences;
            CaseObj.OffenceCategory = req.body.offenceCategory;
            CaseObj.PartOfTheDay = req.body.partOfTheDay;

            CaseObj.save().then(updateCase => {
                req.flash('success-message', 'Case has been updated');
                res.redirect('/admin/cases/');
            })
            .catch(err => { console.log(err);})

       });        
    },

    //To delete a case
    deleteCase: (req, res) => {

        CaseModel.findByIdAndDelete(req.params.id)
            .then(deletedPost => {
                req.flash('success-message', `The case has been deleted.`);
                res.redirect('/admin/cases');
            });
    },


    /*Users Methods*/ 
 
    //To display all registered users in a table
    getRegisteredUser: (req, res) => {
        User.find().then(users => {
            res.render('admin/registeredUsers', {users: users});
        });
    },

    deleteUser: (req, res) => {

        User.findByIdAndDelete(req.params.id)
            .then(deletedPost => {
                req.flash('success-message', `The User has been deleted.`);
                res.redirect('/admin/users');
            });
    },

    registerGet: (req, res) => {
        res.render('Admin/register');
    },
    
    registerPost: (req, res ) => {
        let errors = [];
        

        if(!req.body.firstName){
            errors.push({message: 'First name is mandatory'});
        }

        if(!req.body.lastName){
            errors.push({message: 'Last name is mandatory'});
        }

        if(!req.body.userName){
            errors.push({message: 'Username name is mandatory'});
        }

        if(!req.body.email){
            errors.push({message: 'Email name is mandatory'});
        }


        if(req.body.password !== req.body.passwordConfirm){
            errors.push({message: 'Password do not match'});
        }

  

        if(errors.length > 0) {
            res.render('Admin/register', {
                errors: errors,
                firstName: req.body.firstName,
                lastName: req.body.lastName,
                userName: req.body.userName,
                email: req.body.email,
            });
        }
        else{
            User.findOne({ userName: req.body.userName}).then(user => {
                if (user) {
                  errors.push({ message: 'Username or Email already exist try to log-in or change username or email' });
                  if(errors.length > 0) {
                    res.render('Admin/register', {
                        errors: errors,
                    });
                }
                } 
                else{
                    const newUser = new User(req.body);

                    bcrypt.genSalt(10, (err, salt) => {
                        bcrypt.hash(newUser.password, salt, (err, hash) => {
                            newUser.password = hash;
                            newUser.save().then(UserObj => {
                                req.flash('success-message', 'YOU ARE NOW REGISTERED');
                                res.render('Admin/register');
                            })
                        })
                    })

                }
            })
        }
    },

    editUser: (req, res) => {
        const id = req.params.id;

        User.findById(id).then(users => {
            res.render('admin/updateRegisteredUsers', {users: users});
        });
    },

    editUpdateUser: (req, res) => {
        const id = req.params.id;

        User.findById(id).then(users => {
            let errors = [];
        
            if(!req.body.firstName){
                errors.push({message: 'First name is mandatory'});
            }
    
            if(!req.body.lastName){
                errors.push({message: 'Last name is mandatory'});
            }
    
            if(!req.body.userName){
                errors.push({message: 'Username name is mandatory'});
            }
    
            if(!req.body.email){
                errors.push({message: 'Email name is mandatory'});
            }

            if(errors.length > 0) {
                res.render('admin/updateRegisteredUsers', {
                    errors: errors,
                    users: users
                });
            }
            else{
                users.firstName = req.body.firstName;
                users.lastName = req.body.lastName;
                users.userName = req.body.userName;
                users.email = req.body.email;
                users.password = req.body.password;
                $unset: { firstName: ""}
                users.save().then(updateUser => {
                    req.flash('success-message', 'User has been updated');
                    res.redirect('/admin/users/');
                })
                .catch(err => {
                    console.log(err);
                })    
            }                
        })

    },



    /* ALL CATEGORY METHODS*/
    getOffenceCategories: (req, res) => {

        offenceCategoryModel.find().then(cats => {
            res.render('admin/category/index', {categories: cats});
        });
    },

    createCategories: (req, res) => {
        var offenceCategoryName = req.body.name;

        if (offenceCategoryName) {
            const newoffenceCategory = new offenceCategoryModel({
                title: offenceCategoryName
            });

            newoffenceCategory.save().then(offenceCategory => {
                res.status(200).json(offenceCategory);
            });
        }

    },    
    

    editCategoriesGetRoute: async (req, res) => {
        const catId = req.params.id;

        const cats = await offenceCategoryModel.find();


        offenceCategoryModel.findById(catId).then(cat => {

            res.render('Admin/Category/edit', {category: cat, categories: cats});

        });
    },


    editCategoriesPostRoute: (req, res) => {
        const catId = req.params.id;
        const newTitle = req.body.name;

        if(newTitle){
            offenceCategoryModel.findById(catId).then(OffenceCategoryObj => {
                OffenceCategoryObj.title = newTitle;

                OffenceCategoryObj.save().then(updated => {
                    req.flash('success-message','Category updated');
                    res.status(200).json({url: '/admin/category'});
                });
            });
        }

    },

    deleteCategory: (req, res) => {
        const catId = req.params.id;
        
        offenceCategoryModel.findByIdAndDelete(catId)
            .then(deletedCategory => {
                req.flash('success-message', `The Category has been deleted.`);
                res.redirect('/admin/category');
            });
    },


};