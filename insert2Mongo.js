var MongoClient = require('mongodb').MongoClient;
var url = "mongodb+srv://SB_Admin:RainyDay10@mongoa-ewvkf.mongodb.net/test?retryWrites=true&w=majority";

MongoClient.connect(url, function(err, db){
	if (err) throw err;
	var dbo = db.db("SmartBlinds");
	var myDoc = {Object: "SmartBlinds", Sensor: "Light", Reading: 20000};
	dbo.collection("SB").insertOne(myDoc, function(err, res){
		if (err) throw err;
		console.log("1 Document Inserted");
		db.close();
	});
});