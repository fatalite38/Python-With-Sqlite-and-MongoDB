
# DESAFIO DIO - Integrando Python com SQLite e MongoDB

import pymongo
import pprint

print("Iniciando a conexão com o MongoDB")

# Cria a conexão com o MongoDB
connection = pymongo.MongoClient("link-para-o-mongo-db")

# Cria o banco de dados e a collection
db = connection.bank
collection = db.clients

# Define as informações que irão compor o documento
new_clients = [{
            "agency": 1580,
            "name": "Luiz Pedrozo",
            "cpf": "289.569.523.28",
            "address": "Rua Maria, número 456",
            "account": ["cc", "520991"],
            "balance": 20015
            },
            {
            "agency": 1610,
            "name": "Mauro Silva",
            "cpf": "141.606.586.28",
            "address": "Rua zacarias, número 15",
            "account": ["cp", "315080"],
            "balance": 21560
            },
            {
            "agency": 4563,
            "name": "Lais Pirra",
            "cpf": "426.268.789.77",
            "address": "Rua lazaro, número 589",
            "account": ["cc", "155896"],
            "balance": 15001
            },
            {
            "agency": 4563,
            "name": "Carla Moraes",
            "cpf": "125.123.355.88",
            "address": "Rua lazaro, número 489",
            "account": ["cc", "120588"],
            "balance": 13466
            }]


print("Salvando as informações no MongoDB")
clients = db.clients
result = clients.insert_many(new_clients)
print(result.inserted_ids)


print("\n Recuperando as informações da cliente Stan:")
pprint.pprint(db.clients.find_one({"name": "Stan Lee"}))


print("\n Listagem dos clientes presentes na coleção clients:")
for client in clients.find():
    pprint.pprint(client)


print("\n Recuperando informação dos clientes de maneira ordenada pelo nome:")
for client in clients.find({}).sort("name"):
    pprint.pprint(client)


print("\n Clientes da agência 4563:")
for client in clients.find({"agency": 4563}):
    pprint.pprint(client)


print("\n Clientes com conta poupança:")
for client in clients.find({"account": "cp"}):
    pprint.pprint(client)


print("\n Clientes com conta corrente:")
for client in clients.find({"account": "cc"}):
    pprint.pprint(client)
    
