module.exports = {
    mongoDbUrl : 'mongodb+srv://admin:admin@cmaps-fyz6x.mongodb.net/test?retryWrites=true&w=majority',
    PORT : process.env.PORT || 3000,
    
    globalVariables: (req, res, next) => {
        res.locals.success_message = req.flash('success-message');
        res.locals.error_message = req.flash('Error-message');
        res.locals.user = req.user || null;
        next();
    }
};