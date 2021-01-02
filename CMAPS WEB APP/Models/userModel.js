const mongoose = require('mongoose');
const Schema = mongoose.Schema;

var userSchema = new Schema({
    firstName:{
        type: String,
    },
    
    lastName: {
        type: String,
    }, 
 
    userName: {
        type: String,
    },

    email: {
        type: String,
    },

    password: {
        type: String,
    }
});
 
const UserObj = mongoose.model('user', userSchema);
module.exports = UserObj;  