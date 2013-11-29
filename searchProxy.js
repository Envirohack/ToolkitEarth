/* For use on a Node.js server
 * This file will set up a get proxy for the Geoscience Australia API search function
 * specific to Landsat data.
 */
 
var http = require('http');
var querystring = require('querystring');
var url = require('url');

http.createServer(function(request, response) {
    var data = '';
    var getCallback = function(resp) {
        if(resp.statusCode == 200)
        {
            resp.pipe(response);
            resp.on('end', function(){response.end();});
       } 
        else
        {
            console.log("Request failed :( " + resp.statusCode)
        }
    };
    
    var url_parts = url.parse(request.url, true);
    var query = url_parts.query;
    
    try
    {
        var northLat = parseFloat(query['northLat']);
        var southLat = parseFloat(query['southLat']);
        var eastLong = parseFloat(query['eastLong']);
        var westLong = parseFloat(query['westLong']);
        
        if( isNaN(northLat) || isNaN(southLat) || isNaN(eastLong) || isNaN(westLong))
        {
            response.statusCode = "400";
            response.write("All of northLat, southLat, eastLong and westLong must be specified.");
            response.end();
            return;
        }
    }    
    catch(e)
    {
        response.statusCode = "400";
        response.write("All of northLat, southLat, eastLong and westLong must be specified.");
        response.end();
        return;
    }
    
    var parmObj = {"searchTerm":"landsat","northLat":northLat,"southLat":southLat,"westLong":westLong,"eastLong":eastLong,"startPosition":0};
    
    var parameters = JSON.stringify(parmObj);
    
    var options = {
      host: "ga.gov.au",
      path: "http://www.ga.gov.au/search/api/search/results",
      method: 'POST',
      port: 80,
      headers: {"content-type": "application/json", 
                "content-length": parameters.length}
    };
    
    http.request(
        options,
        getCallback).on('error', function(e) {
      console.log("Got error: " + e.message);
    }).write(parameters);   
}).listen(process.env.PORT, process.env.IP);
