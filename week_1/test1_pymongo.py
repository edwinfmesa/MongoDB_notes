from pymongo import MongoClient

#connect to database 

connection = MongoClient('localhost',27020)

db = connection.test1

#create a collection
names = db.names

#create an array with json objects
json_list = [
	{'name':'Juan','lastname':'Lopez'},
	{'name':'Carlos','lastname':'Gil'},
	{'name':'Juan','lastname':'Mesa'},
	{'name':'Felipe','lastname':'Lopez'},
	{'name':'Andres','lastname':'Toro'}
]

#insert the data
for j in json_list:
	names.insert(j)

#show the data
print names.find()