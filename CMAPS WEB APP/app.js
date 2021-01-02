/* Importing Different Modules */

const {globalVariables} = require('./config/configuration');

const express = require('express');
const mongoose = require('mongoose');
const path = require('path');
const hbs = require('express-handlebars');
const Handlebars = require('handlebars');
const {mongoDbUrl, PORT} = require('./config/configuration');
const flash = require('connect-flash');
const session = require('express-session');
const {allowInsecurePrototypeAccess} = require('@handlebars/allow-prototype-access');
const methodOverrirde = require('method-override');
const {selectOption} = require('./config/customFunctions');
const passport = require('passport');
const LocalStrategy = require('passport-local').Strategy;
const axios = require('axios').default;
 

const app = express();


// Configure Mongoose to Connect to MongoDB
mongoose.connect(mongoDbUrl, { useUnifiedTopology: true, useNewUrlParser: true })
    .then(response => {
        console.log("MongoDB Connected Successfully.");
    })
    .catch(err => {
        console.log(err);
    });


/* Configure express*/
app.use(express.json());
app.use(express.urlencoded({extended: true}));
app.use(express.static(path.join(__dirname, 'public')));

/*  Flash and Session*/
app.use(session({
    secret: 'anysecret',
    saveUninitialized: true,
    resave: true
}));

app.use(passport.initialize());
app.use(passport.session());

app.use(flash());


/* Use Global Variables */
app.use(globalVariables);


/* Setup View Engine To Use Handlebars */
app.engine('handlebars', hbs({
    defaultLayout: 'default',
    helpers: {select: selectOption},
    handlebars: allowInsecurePrototypeAccess(Handlebars)
}));
app.set('view engine' , 'handlebars');

//method override middleware
app.use(methodOverrirde('newMethod'));

/* Routes */
const defaultRoutes = require('./Routes/defaultRoutes');
const adminRoutes = require('./Routes/adminRoutes');

app.use('/', defaultRoutes);
app.use('/admin', adminRoutes);


/* Start The Server */
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});