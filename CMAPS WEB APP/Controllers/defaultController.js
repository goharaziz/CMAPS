const caseModel = require('../models/caseModel');
const offenceCategoryModel = require('../models/offenceCategoryModel');
const User = require('../models/userModel');
const bcrypt = require('bcryptjs');
const axios = require('axios').default;

var finalresponse = 'Hello G';

module.exports = {
    index: async (req,res) => {
        const offenceCategories = await offenceCategoryModel.find();
        var docs = offenceCategories;
        
        res.render('default/index', {
            list: docs,
        });
    },

    reportGraphs: (req, res) => {
        res.render('default/reportGraphs');
    },

    reportCharts: (req, res) => {
        res.render('default/reportCharts');
    },

    mapping: (req, res) => {
        res.render('default/mapping');
    },

    mappingTwo: (req, res) => {
        res.render('default/mappingTwo');
    },
    
    mappingThree: (req, res) => {
        res.render('default/mappingThree');
    },
    
    mappingFour: (req, res) => {
        res.render('default/mappingFour');
    },

    prediction: (req, res) => { 
        res.render('default/prediction');
    },
    
    postPrediction: (req, res) => {
        
        function makePostRequest(path, queryObj) { 
            axios.post(path, queryObj).then( 
                (response) => { 
                    var result = response.data; 
                    finalresponse = result
                    res.render('Default/predictionResult',{
                        finalresponse:finalresponse,
                        queryObj: queryObj
                    })
                }, 
                (error) => { 
                    console.log(error); 
                } 
            ); 
            
        } 
        
        queryObj = {
            posting : req.body.posting,
            date: req.body.date,
            month: req.body.month,
            year: req.body.year,
            day: req.body.day,
            hours: req.body.hours,
            minutes: req.body.minutes,
            PartOfTheDay: req.body.partOfTheDay,
            Crime: req.body.crime,
            Model: req.body.model
        };
        

        makePostRequest('http://127.0.0.1:5000/', queryObj);
    },

    predictionTwo: (req, res) => {
        res.render('default/predictionTwo');
    },

    postPredictionTwo: (req, res) => {
        function makePostRequest(path, queryObj) { 
            axios.post(path, queryObj).then( 
                (response) => { 
                    var result = response.data; 
                    finalresponse = result
                    res.render('Default/output',{
                        finalresponse:finalresponse,
                        queryObj: queryObj
                    })
                }, 
                (error) => { 
                    console.log(error); 
                } 
            ); 
            
        } 
        
        queryObj = {
            Crime: req.body.crime,
            Model: req.body.model
        };
        

        makePostRequest('http://127.0.0.1:5000/predict  ', queryObj);

    },
    
    predictionThree: (req, res) => {
        res.render('default/predictionThree');
    },

    postPredictionThree: (req, res) => {
        function makePostRequest(path, queryObj) { 
            axios.post(path, queryObj).then( 
                (response) => { 
                    var result = response.data; 
                    finalresponse = result
                    res.render('Default/output',{
                        finalresponse:finalresponse,
                        queryObj: queryObj
                    })
                }, 
                (error) => { 
                    console.log(error); 
                } 
            ); 
            
        } 
        
        queryObj = {
            Crime: req.body.crime,
            Model: req.body.model
        };
        

        makePostRequest('http://127.0.0.1:5000/predictThree  ', queryObj);

    },

    predictionFour: (req, res) => {
        res.render('default/predictionFourth');
    },

    postPredictionFour: (req, res) => {
        function makePostRequest(path, queryObj) { 
            axios.post(path, queryObj).then( 
                (response) => { 
                    var result = response.data; 
                    finalresponse = result
                    res.render('Default/output',{
                        finalresponse:finalresponse,
                        queryObj: queryObj
                    })
                }, 
                (error) => { 
                    console.log(error); 
                } 
            ); 
            
        } 
        
        queryObj = {
            Crime: req.body.crime,
            Model: req.body.model
        };
        

        makePostRequest('http://127.0.0.1:5000/predictThree  ', queryObj);

    },

    loginGet: (req,res) => {
        res.render('default/login');
    },

    loginPost: (req,res) => {
        res.send('congrats you have subitted the data');
    }

};
