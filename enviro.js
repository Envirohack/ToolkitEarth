var mongodb = require('mongodb');

var db;

db = new mongodb.Db('toolkit_earth', new mongodb.Server('ds053638.mongolab.com', 53638, {auto_reconnect:true}), {});

  db.open(function(err, db) {

    db.authenticate('rdengate', 'envirohacK_427', function(err) {
      if(!err) {
        console.log("Connected to toolkit_earth database");
    }
  });
});
  
exports.findById = function(req, res) {
    var id = req.params.id;
    console.log('Retrieving: ' + id);
    db.collection('weather_at_point', function(err, collection) {
        collection.findOne({'_id':id}, function(err, item) {
            res.send(item);
        });
    });
};
 
exports.findAll = function(req, res) {
    console.log('finding...');
    db.collection('weather_at_point', function(err, collection) {
        console.log('finding col...');
        collection.find().toArray(function(err, items) {
            console.log('find()...');
            res.send(items);
        });
    });
};
 
exports.addEnv = function(req, res) {
    var envBody = req.body;
    console.log('Adding : ' + JSON.stringify(envBody));
    db.collection('weather_at_point', function(err, collection) {
        collection.insert(envBody, {safe:true}, function(err, result) {
            if (err) {
                res.send({'error':'An error has occurred'});
            } else {
                console.log('Success: ' + JSON.stringify(result[0]));
                res.send(result[0]);
            }
        });
    });
};
 
