import datetime
from mongokit import Document, Connection

connection = Connection("localhost",27017)
print "starting database"

@connection.register

class Dog(Document):
    __database__ = "federated(2)"
    __collection__ = "animals"
    structure = {"name":basestring,
                 "color":basestring,
                 "age":int}
    required_fields = ["name"]

for i in range (1000000):

     dog = connection.Dog()
     dog["name"]= "xiaohuang"
     dog["color"]="yellow"
     dog["age"]=3
     dog.save()

connection.animal.find({"name":"xiaohuang"}).count()

connection.animals.drop()
print dog
