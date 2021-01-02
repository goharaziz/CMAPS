const mongoose = require('mongoose');
const Schema = mongoose.Schema;

var caseSchema = new Schema({
    Posting: {
        type: String,
        required: true
    },

    Latitudes: {
        type: String,
    },

    Longitudes: {
        type: String,
    },

    Date: {
        type: String,
        required: true
    },

    Month: {
        type: String,
        required: true
    },

    Year: {
        type: String,
        required: true
    },

    Day: {
        type: String,
        required: true
    },

    Time: {
        type: String,
        required: true
    },

    Offences: {
        type: String,
        required: true
    },

    OffenceCategory: {
        type: String,
        required: true
    },
    
    PartOfTheDay: {
        type: String,
        required: true
    },

    creationDate:{
        type: Date,
        default: Date.now()
    },
});

const CaseObj = mongoose.model('case', caseSchema);
module.exports = CaseObj; 