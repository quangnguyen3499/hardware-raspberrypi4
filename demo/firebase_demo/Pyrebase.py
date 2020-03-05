import pyrebase
config = {
	"apiKey":"",
	"authDomain":"",
	"databaseURL":""
	"storageBucket":"",
}
firebase = pyrebase.initialize_app(config)
db = firebase.database()
data = {"" : "Elnino"}
db.child("").child().update(data)