var express = require('express');
var path = require('path');
var fs = require('fs');
var crypto = require('crypto');

var router = express.Router();

/* GET home page. */
router.get('/', function(req, res, next) {
    var ip = req.headers['x-forwarded-for'] || req.connection.remoteAddress || req.socket.remoteAddress || req.connection.socket.remoteAddress;
    var md5 = crypto.createHash('md5').update(ip).digest("hex");
    var array = fs.readFileSync('ips.txt').toString().split("\n");
    var contains = false;
    
    for(i in array) {
	if (i == md5) {
	    contains = true;
	    break;
	}
    }
    if (!contains) {
	fs.writeFileSync('ips.txt', md5 + "\n");
    }
    
    res.render('index', { title: '' });
});
    
module.exports = router;
