var express = require("express");
var app     = express();
var path    = require("path");
app.use(express.static(path.join(__dirname, './public')));

app.use(function(req, res, next) {
    res.header("Access-Control-Allow-Origin", "*");
    res.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept");
    next();
  });

app.get('/',function(req,res){
  res.sendFile(path.join(__dirname+'/templates/price-prediction.html'));
});

app.listen(9000);

console.log("Running at Port 9000");