const express = require('express');
const router = express.Router();
const adminController = require('../Controllers/adminController');
const {isUserAuthenticated} = require('../Config/customFunctions');
const csv      = require('csv-express');
const CaseModel = require('../models/caseModel');
const fs = require('fs');
const moment = require('moment');
const mdq = require('mongo-date-query');
const json2csv = require('json2csv').parse;
const path = require('path')
const fields = ['Posting', 'Latitudes', 'Longitudes', 'Date', 'Month', 'Year', 'day', 'time', 'Offences', 'OffenceCategory', 'PartOfTheDay'];


router.all('/*', isUserAuthenticated, (req, res, next) => {
    
    req.app.locals.layout = 'admin';
    
    next();
}); 

 
router.route('/')

    .get(adminController.index);

router.route('/cases')
    .get(adminController.getCases);

router.route('/cases/exporttocsv')
    .get(adminController.exportToCsv);

router.route('/cases/create')
    .get(adminController.createCase)
    .post(adminController.submitCases);

router.route('/cases/edit/:id')
    .get(adminController.editCase)
    .put(adminController.editUpdateCase)
 
router.route('/cases/delete/:id')
    .delete(adminController.deleteCase);

    /* ADMIN USERS ROUTES*/

router.route('/users')
    .get(adminController.getRegisteredUser);

router.route('/users/update/:id')
    .get(adminController.editUser)
    .put(adminController.editUpdateUser);

router.route('/users/delete/:id')
    .delete(adminController.deleteUser);

router.route('/register')
    .get(adminController.registerGet)
    .post(adminController.registerPost);

/* ADMIN CATEGORY ROUTES*/

router.route('/category')
    .get(adminController.getOffenceCategories);


router.route('/category/create')
    .post(adminController.createCategories);


router.route('/category/edit/:id')
    .get(adminController.editCategoriesGetRoute)
    .post(adminController.editCategoriesPostRoute);

router.route('/category/delete/:id')
    .delete(adminController.deleteCategory);
    
module.exports = router;
 