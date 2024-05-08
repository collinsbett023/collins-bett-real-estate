from models.clients import Client
from models.contracts import Contract
from models.property import Property
from models.realtors import Realtor


# Exit from program
def exit_program():
    print("Exiting.....")
    exit()


# list data from db
def list_properties():
    houses = Property.get_all()
    if houses:
        for house in houses:
            print(house.name, house.address, house.price, house.status)
    else:
        print("No houses")


def list_clients():
    clients = Client.get_all()
    if clients:
        for client in clients:
            print(client.name)
        else:
            print("No clients")


def list_realtors():
    realtors = Realtor.get_all()
    if realtors:
        for realtor in realtors:
            print(realtor.name)
    else:
        print("No realtors")


def list_contracts():
    contracts = Contract.get_all()
    if contracts:
        for contract in contracts:
            print(contract)
    else:
        print("No contracts")


# Check by id
def find_property_by_id():
    item_id = input("Enter the property id: ")
    property_item = Property.find_by_id(item_id)
    print(property_item.address) if property_item else print(f'Property with id {item_id} not found')


def find_client_by_id():
    item_id = input("Enter the client id: ")
    client_item = Client.find_by_id(item_id)
    print(client_item.name) if client_item else print(f'Client with id {item_id} not found')


def find_contract_by_id():
    item_id = input("Enter the contract id: ")
    contract_item = Contract.find_by_id(item_id)
    print(contract_item.name) if contract_item else print(f'Contract with id {item_id} not found')


def find_realtor_by_id():
    item_id = input("Enter the realtor id: ")
    realtor_item = Realtor.find_by_id(item_id)
    print(realtor_item.name) if realtor_item else print(f'Client with id {item_id} not found')


# Create object
def create_property():
    name = input("Enter the property name: ")
    address = input("Enter the address: ")
    price = int(input("Enter the price: "))
    status = input("Select the state of the property: ")

    try:
        Property.create(name, address, price, status)
        print("Property has been created")
    except Exception as ex:
        print(f'An error occurred: {ex} ')


def create_realtor():
    name = input("Enter name: ")
    email = input("Enter email: ")
    try:
        Realtor.create(name, email)
        print("Realtor has been created")
    except Exception as ex:
        print(f'An error occurred {ex}')


def create_client():
    name = input("Enter name: ")
    email = input("Enter email: ")
    try:
        Client.create(name, email)
        print("Client has been added")
    except Exception as ex:
        print(f'An error occurred {ex}')


def create_contract():
    property_id = input("Enter property id: ")
    client_id = input("Enter client id: ")
    realtor_id = input("Enter realtor id: ")
    try:
        Contract.create(property_id, client_id, realtor_id)
        print("Contract as been added")
    except Exception as ex:
        print(f'An error occurred {ex}')


# Delete object
def delete_property():
    item_id = input("Provide property id: ")
    if property_item := Property.find_by_id(item_id):
        property_item.delete()
        print("Property has been deleted")
    else:
        print("Property id has not been found")


def delete_client():
    item_id = input("Provide client id: ")
    if client_item := Client.find_by_id(item_id):
        client_item.delete()
        print("Client has been deleted")
    else:
        print("Client has not been found")


def delete_realtor():
    item_id = input("Provide realtor id: ")
    if realtor_item := Realtor.find_by_id(item_id):
        realtor_item.delete()
        print("Realtor has been removed")
    else:
        print("Realtor has not been found")


def delete_contract():
    item_id = input("Provide contract id: ")
    if contract_item := Contract.find_by_id(item_id):
        contract_item.delete()
        print("Contract has been removed")
    else:
        print("Contract has not been found")
