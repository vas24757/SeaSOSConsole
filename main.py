import pprint
from pymongo import MongoClient

connection_string = f"mongodb+srv://sanabria:sanabria123@seasos.klfvhka.mongodb.net/Prueba?retryWrites=true&w=majority"

client = MongoClient(connection_string)

dbs = client.list_database_names()
test_db = client.test
collections = test_db.list_collection_names()


def find_users():
    all_users = users.find()
    
    for user in all_users:
        printer.pprint(user)



def insert_test_doc():
    collection = test_db.test
    test_document = {
        "name": "Carlos",
        "type": "Test"
    }
    inserted_id = collection.insert_one(test_document).inserted_id
    print(inserted_id)
    
user = client.user
users = user.users

def create_documents():
    while True:
        first_name = input("Ingrese el primer nombre del usuario: ")
        last_name = input("Ingrese el apellido del usuario: ")
        age = int(input("Ingrese la edad del usuario: "))
        
        doc = {"first_name": first_name, "last_name": last_name, "age": age}
        users.insert_one(doc)
        
        another = input("¿Desea ingresar otro usuario? (s/n): ")
        if another.lower() != 's':
            break

create_documents()
    
printer = pprint.PrettyPrinter()
        

def find_user():
    user =  users.find_one({"first_name": "Pablo"})
    printer.pprint(user)
    
    
def count_users():
    count = users.count_documents(filter={})
    print("El número de usuarios existentes es: " + str(count))
    

def get_by_id(user_id):
    from bson.objectid import ObjectId
    
    _id = ObjectId(user_id)
    user = users.find_one({"_id": _id})
    printer.pprint(user)
    
