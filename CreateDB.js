var MongoClient = require('mongodb').MongoClient;
var url = "mongodb+srv://SB_Admin:RainyDay10@mongoa-ewvkf.mongodb.net/test?retryWrites=true&w=majority";

MongoClient.connect(url, function(err, db){
	if (err) throw err;
	var dbo = db.db("SmartBlinds");
	dbo.createCollection("SB", function(err, res){
		if (err) throw err;
		console.log("Collection created!");
		db.close();
	});
});