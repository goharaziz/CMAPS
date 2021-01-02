const mongoose = require('mongoose');
const Schema = mongoose.Schema;

var offenceCategorySchema = new Schema({
    title: {
        type: String,
        required: true
    }
 
});

const offenceCategoryObj = mongoose.model('offenceCategory', offenceCategorySchema);
module.exports = offenceCategoryObj;  