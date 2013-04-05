from pymongo import MongoClient
import bottle

# this method lets update the names document eg. search where name = Juan an update with the name Camilo
# the first value is the name of the key
# the second one is the current value for this key
# the third one is the new value


#connect to database 
connection = MongoClient('localhost',27020)

db = connection.test1

#use a collection
names = db.names

def updateName(current, new_value):
	data = {
		'name':current
	}
	d = db.names.find_one(data)
	d['name'] = new_value
	db.names.save(d)
	print d


updateName('Juan','Camilo')
