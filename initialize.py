from models.connect import CONN, CURSOR
from models.clients import Client
from models.contracts import Contract
from models.property import Property
from models.realtors import Realtor


def reset_db():
    Property.drop_table()
    Realtor.drop_table()
    Contract.drop_table()
    Client.drop_table()

    Property.create_table()
    Realtor.create_table()
    Contract.create_table()
    Client.create_table()

    house1 = Property.create("3-Bedroom House", "973-00618, Nairobi", 40000, "On Sale")
    house2 = Property.create("Grassland Ranch", "999-00710, Mombasa", 50000, "On Sale")

    client1 = Client.create("John Wick", "jwick@gmail.com")
    client2 = Client.create("Narco Wick", "nwick@gmail.com")

    realtor1 = Realtor.create("Ndungu Kamau", "Nkamau@gmail.com")
    realtor2 = Realtor.create("Njeri Kamau", "NjeriKamau@gmail.com")

    contract1 = Contract.create(1, 1, 1)
    contract2 = Contract.create(2, 2, 2)


reset_db()
