from models.clients import Client
from models.contracts import Contract
from models.property import Property
from models.realtors import Realtor


# Exit from program
def exit_program():
    print("\nExiting.....")
    exit()


# list data from db
def list_properties():
    houses = Property.get_all()
    if houses:
        for house in houses:
            print(f'\tName: {house.name}, Address: {house.address}, Price{house.price}, Status: {house.status}\n')
    else:
        print("\nNo Property Found\n")


def list_clients():
    clients = Client.get_all()
    if clients:
        for client in clients:
            print(f'\tName: {client.name}\n')
    else:
        print("\tNo clients\n")


def list_realtors():
    realtors = Realtor.get_all()
    if realtors:
        for realtor in realtors:
            print(f'\tName:{realtor.name}\n')
    else:
        print("\n\tNo realtors\n")


def list_contracts():
    contracts = Contract.get_all()
    if contracts:
        for contract in contracts:
            print(contract.id)
    else:
        print("\n\tNo contracts\n")


# Check by id
def find_property_by_id():
    item_id = input("Enter the property id: ")
    property_item = Property.find_by_id(item_id)
    print(f'\n\tName: {property_item.name}, {property_item.address}') if property_item \
        else print(f'\n\tProperty with id {item_id} not found\n')


def find_client_by_id():
    item_id = input("Enter the client id: ")
    client_item = Client.find_by_id(item_id)
    print(f'\n\tName:{client_item.name}') if client_item else print(f'\t\nClient with id {item_id} not found\n')


def find_contract_by_id():
    item_id = input("Enter the contract id: ")
    contract_item = Contract.find_by_id(item_id)
    print(contract_item.property_id, contract_item.client_id, contract_item.realtor_id) if contract_item else print(
        f'Contract with id {item_id} not found')


def find_realtor_by_id():
    item_id = input("Enter the realtor id: ")
    realtor_item = Realtor.find_by_id(item_id)
    print(f'\n\tName{realtor_item.name}') if realtor_item else print(f'\t\nRealtor with id {item_id} not found\n')


# Create object
def create_property():
    name = input("Enter the property name: ")
    address = input("Enter the address: ")
    price = int(input("Enter the price: "))
    status = input("Select the state of the property: ")
    owner = input("Enter the client id: ")

    try:
        Property.create(name, address, price, status, owner)
        print("\n\tProperty has been created\n")
    except Exception as ex:
        print(f'\n\tAn error occurred: {ex} \n')


def create_realtor():
    name = input("Enter name: ")
    email = input("Enter email: ")
    try:
        Realtor.create(name, email)
        print("\n\tRealtor has been created\n")
    except Exception as ex:
        print(f'\n\tAn error occurred {ex}\n')


def create_client():
    name = input("Enter name: ")
    email = input("Enter email: ")
    try:
        Client.create(name, email)
        print("\n\tClient has been added\n")
    except Exception as ex:
        print(f'\n\tAn error occurred {ex}\n')


def create_contract():
    property_id = int(input("Enter property id: "))
    client_id = int(input("Enter client id: "))
    realtor_id = int(input("Enter realtor id: "))
    try:
        Contract.create(property_id, client_id, realtor_id)
        print("\n\tContract as been added\n")
    except Exception as ex:
        print(f'\n\tAn error occurred {ex}\n')


# Delete object
def delete_property():
    item_id = input("Provide property id: ")
    if property_item := Property.find_by_id(item_id):
        property_item.delete()
        print("\n\tProperty has been deleted\n")
    else:
        print("\n\tProperty id has not been found\n")


def delete_client():
    item_id = input("Provide client id: ")
    if client_item := Client.find_by_id(item_id):
        client_item.delete()
        print("\n\tClient has been deleted\n")
    else:
        print("\n\tClient has not been found\n")


def delete_realtor():
    item_id = input("Provide realtor id: ")
    if realtor_item := Realtor.find_by_id(item_id):
        realtor_item.delete()
        print("\n\tRealtor has been removed\n")
    else:
        print("\n\tRealtor has not been found\n")


def delete_contract():
    item_id = input("Provide contract id: ")
    if contract_item := Contract.find_by_id(item_id):
        contract_item.delete()
        print("\n\tContract has been removed\n")
    else:
        print("\n\tContract has not been found\n")


# Get property owner name
def owner_name():
    owner_id = input("Enter the Property owner id: ")
    if name := Property.return_client_name(owner_id):
        print(f'\n\t{name}')
    else:
        raise ValueError("\n\tOwner doesnt exist\t")


# Get contract details
def contract_details():
    id_contract = input("Enter the contract id: ")
    if details := Contract.get_contract_details(id_contract):
        for key, value in details.items():
            print(f"\t{key}: {value}")
    else:
        raise ValueError("No Contract Found")
