#!/usr/bin/env python3
"""
this module contains the notes i written down whiel studing pymongo module
feel free to read it and add additional info if needed.
"""

# << pymongo >>

# first install it

"""pip install pymongo==3.11.2"""

# first: establishing the connection



from pymongo import MongoClient
client = MongoClient()
"""
print client output
MongoClient(host=['localhost:27017'], document_class=dict, tz_aware=False, connect=True)
"""

client = MongoClient(host="localhost", port=27017)
        # you can use the mongodb url format
client = MongoClient("mongodb://localhost:27017")


# after creating the connection you need to specify the collection using .dot notation
# this command will create the database rptutorials if it is not exist but after the first opertion on the db
db = client.rptutorials


# if the name is not python compatable you can user the dict style
db = client["rptutorials"]

# you add collections in py using dictionaries

tutorial1 = {
    "title": "Working With JSON Data in Python",
    "author": "Lucas",
    "contributors": [
        "Aldren",
        "Dan",
        "Joanna"
    ],
    "url": "https://realpython.com/python-json/"
}

# to chose the collection to work with use the dot notation too

tutorial = db.turorial

# how to insert one tutorial to the collection 
result = tutorial.insert_one(tutorial1)
result


print(f"One tutorial: {result.inserted_id}")

# insert meny records at once
tutorial2 = {
    "title": "Python's Requests Library (Guide)",
    "author": "Alex",
    "contributors": [
        "Aldren",
        "Brad",
        "Joanna"
    ],
    "url": "https://realpython.com/python-requests/"
}

tutorial3 = {
    "title": "Object-Oriented Programming (OOP) in Python 3",
    "author": "David",
    "contributors": [
        "Aldren",
        "Joanna",
        "Jacob"
    ],
    "url": "https://realpython.com/python3-object-oriented-programming/"
}

new_result = tutorial.insert_many([tutorial2, tutorial3])

print(f"Multiple tutorials: {new_result.inserted_ids}")

# to get data from a collection
import pprint

for doc in tutorial.find():
    pprint.pprint(doc)

"""
output
{'_id': ObjectId('600747355e6ea8d224f754ba'),
 'author': 'Jon',
 'contributors': ['Aldren', 'Geir Arne', 'Joanna', 'Jason'],
 'title': 'Reading and Writing CSV Files in Python',
 'url': 'https://realpython.com/python-csv/'}
    ...
{'_id': ObjectId('6008511c87eb0fbf73dbf71f'),
 'author': 'David',
 'contributors': ['Aldren', 'Joanna', 'Jacob'],
 'title': 'Object-Oriented Programming (OOP) in Python 3',
 'url': 'https://realpython.com/python3-object-oriented-programming/'}
"""

# how to find one record in a serten condition
import pprint
# finds the record with author = "Jon"
jon_tutorial = tutorial.find_one({"author": "Jon"})

pprint.pprint(jon_tutorial)
"""
{'_id': ObjectId('600747355e6ea8d224f754ba'),
 'author': 'Jon',
 'contributors': ['Aldren', 'Geir Arne', 'Joanna', 'Jason'],
 'title': 'Reading and Writing CSV Files in Python',
 'url': 'https://realpython.com/python-csv/'}
 """


# create operation

"""
replace_one(filter, replacement, upsert=False, bypass_document_validation=False, collation=None, hint=None, session=None, let=None, comment=None)
"""
for doc in db.test.find({}):
    print(doc)

# {'x': 1, '_id': ObjectId('54f4c5befba5220aa4d6dee7')}
result = db.test.replace_one({'x': 1}, {'y': 1})
result.matched_count
# 1
result.modified_count
# 1
for doc in db.test.find({}):
    print(doc)

# {'y': 1, '_id': ObjectId('54f4c5befba5220aa4d6dee7')}


result = db.test.replace_one({'x': 1}, {'x': 1}, True)
# this will insert the new codument if the matched one doesnt exist


# update operation

"""
update_one(filter, update, upsert=False, bypass_document_validation=False, collation=None, array_filters=None, hint=None, session=None, let=None, comment=None)
"""

result = db.test.update_one({'x': 1}, {'$inc': {'x': 3}})

"""
update_many(filter, update, upsert=False, array_filters=None, bypass_document_validation=None, collation=None, hint=None, session=None, let=None, comment=None)
"""
# Update one or more documents that match the filter.
result = db.test.update_many({'x': 1}, {'$inc': {'x': 3}})

# delete operation

"""
delete_one(filter, collation=None, hint=None, session=None, let=None, comment=None)
"""
# Delete a single document matching the filter.

db.test.count_documents({'x': 1})
# 3
result = db.test.delete_one({'x': 1})
result.deleted_count
# 1
db.test.count_documents({'x': 1})
# 2


"""
delete_many(filter, collation=None, hint=None, session=None, let=None, comment=None)

"""
# Delete one or more documents matching the filter.

db.test.count_documents({'x': 1})

# to close the connection with the database
client.close()

# or if you want to open the db, preform tasks, and close immediatly>> user with statment 
import pprint
from pymongo import MongoClient

with MongoClient() as client:
    db = client.rptutorials
    for doc in db.tutorial.find():
        pprint.pprint(doc)



""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# using mongoEngin insetd of pymongo

from mongoengine import connect
connect(db="rptutorials", host="localhost", port=27017)
# or use the default host an port number
connect(db="database name onely")
