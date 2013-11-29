/*

API for weather-at-point https://test_rest-c9-alphillips.c9.io/weather
for toolkit_earth MongoDB at mongolab
*/

var express = require('express'),
    enviro = require('./routes/enviro');
 
var app = express();
 
app.configure(function () {
    app.use(express.logger('dev'));
    app.use(express.bodyParser());
});
 
app.get('/weather', enviro.findAll);
app.get('/weather/:id', enviro.findById);
app.post('/weather', enviro.addEnv);

app.listen(process.env.PORT);
console.log('Listening on port ... ' + process.env.PORT);
