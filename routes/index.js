var express = require('express');
var path = require('path');
var fs = require('fs');
var crypto = require('crypto');

var router = express.Router();

/* GET home page. */
router.get('/', function(req, res, next) {
    
    
    res.render('index', { title: '' });
});
    
module.exports = router;
