const express = require('express');
const router = express.Router();
const defaultController = require('../Controllers/defaultController');
const passport = require('passport');
const LocalStrategy = require('passport-local').Strategy;
const bcrypt = require('bcryptjs');
const User = require('../models/userModel');



router.all('/*', (req, res, next) => {
    
    req.app.locals.layout = 'default';
    
    next();
});

 
router.route('/')
    .get(defaultController.index);


//defining local strategy
passport.use(new LocalStrategy({
    usernameField: 'userName',
    passReqToCallback: true,
}, (req, userName, password, done) => {
    User.findOne({ userName: userName}).then(user => {
        if(!user){
            console.log('user not found');
            return done(null, false, req.flash('Error-message', `Username not found`));
        }

        bcrypt.compare(password, user.password, (err, passwordMatched) => {
            if(err){
                console.log('password wrong');
                return err;
            }

            if(!passwordMatched){
                console.log('user not found');
                return done(null, false, req.flash('Error-message', `Invalid Username or Password`));
            }


            return done(null, user, req.flash('success-message', 'You have logged into Admin Portal Successfully'));
        });

    });
}));


passport.serializeUser(function(user, done) {
    done(null, user.id);
});
  
passport.deserializeUser(function(id, done) {
    User.findById(id, function(err, user) {
      done(err, user);
    });
  });

 


router.route('/login')
    .get(defaultController.loginGet)
    .post(passport.authenticate('local', {
        successRedirect: '/admin',
        failureRedirect: '/login',
        failureFlash: true,
        successFlash: true,
    }),defaultController.loginPost);

router.route('/reportGraphs')
    .get(defaultController.reportGraphs);

router.route('/reportCharts')
    .get(defaultController.reportCharts);

router.route('/map')    
    .get(defaultController.mapping);

router.route('/mapTwo')    
    .get(defaultController.mappingTwo);

router.route('/mapThree')    
    .get(defaultController.mappingThree);

router.route('/mapFour')    
    .get(defaultController.mappingFour);

//For Offence Category Model
router.route('/prediction')    
    .get(defaultController.prediction)
    .post(defaultController.postPrediction);

//For Day Model
router.route('/predictionTwo')
    .get(defaultController.predictionTwo)
    .post(defaultController.postPredictionTwo);

//For Month Model
router.route('/predictionThree')
    .get(defaultController.predictionThree)
    .post(defaultController.postPredictionThree);

//For Area Model
router.route('/predictionFour')    
    .get(defaultController.predictionFour)
    .post(defaultController.postPredictionFour);

router.get('/logout', (req, res) => {
    req.logOut();
    req.flash('success-message','Logged Out Succesfully');
    res.redirect('/');
});



module.exports = router;


