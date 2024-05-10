from models.connect import CONN, CURSOR
from models.property import Property
from models.realtors import Realtor
from models.clients import Client


class Contract:
    all = {}

    def __init__(self, property_id, client_id, realtor_id, id=None):
        self.id = id
        self.property_id = property_id
        self.client_id = client_id
        self.realtor_id = realtor_id

    @property
    def property_id(self):
        return self._property_id

    @property_id.setter
    def property_id(self, property_id):
        if type(property_id) is int and Property.find_by_id(property_id):
            self._property_id = property_id
        else:
            raise ValueError(
                "property_id must reference a Prop in the database")

    @property
    def client_id(self):
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        if type(client_id) is int and Client.find_by_id(client_id):
            self._client_id = client_id
        else:
            raise ValueError(
                "client_id must reference a Prop in the database")

    @property
    def realtor_id(self):
        return self._realtor_id

    @realtor_id.setter
    def realtor_id(self, realtor_id):
        if type(realtor_id) is int and Realtor.find_by_id(realtor_id):
            self._realtor_id = realtor_id
        else:
            raise ValueError(
                "realtor_id must reference a Prop in the database")

    @classmethod
    def create_table(cls):
        sql = """
                CREATE TABLE IF NOT EXISTS contracts ( 
                id INTEGER PRIMARY KEY, 
                property_id INTEGER, 
                client_id INTEGER, 
                realtor_id INTEGER,
                FOREIGN KEY (property_id) REFERENCES properties(id),
                FOREIGN KEY (client_id) REFERENCES clients(id),
                FOREIGN KEY (realtor_id) REFERENCES realtors(id)
                )
                """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):

        sql = """
                INSERT INTO contracts (property_id, client_id, realtor_id)
                VALUES (?, ?, ?)
        """

        CURSOR.execute(sql, (self.property_id, self.client_id, self.realtor_id))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    def delete(self):

        sql = """
            DELETE FROM contracts
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        # Delete the dictionary entry using id as the key
        del type(self).all[self.id]

        # Set the id to None
        self.id = None

    @classmethod
    def create(cls, property_id, client_id, realtor_id):

        contract = cls(property_id, client_id, realtor_id)
        contract.save()
        return contract

    @classmethod
    def drop_table(cls):

        sql = """
            DROP TABLE IF EXISTS contracts;
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def instance_from_db(cls, row):

        # Check the dictionary for  existing instance using the row's primary key
        contract = cls.all.get(row[0])
        if contract:
            # ensure attributes match row values in case local instance was modified
            contract.property_id = row[1]
            contract.client_id = row[2]
            contract.realtor_id = row[3]
        else:
            # not in dictionary, create new instance and add to dictionary
            contract = cls(row[1], row[2], row[3])
            contract.id = row[0]
            cls.all[contract.id] = contract
        return contract

    @classmethod
    def get_all(cls):

        sql = """
            SELECT *
            FROM contracts
        """

        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):

        sql = """
            SELECT *
            FROM contracts
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def get_contract_details(cls, contract_id):
        selected_contract = Contract.find_by_id(contract_id)
        client_id = selected_contract.client_id
        realtor_id = selected_contract.realtor_id
        property_id = selected_contract.property_id

        p = Property.find_by_id(property_id)
        r = Realtor.find_by_id(realtor_id)
        c = Client.find_by_id(client_id)

        return {"Property Name": p.name, "Realtor Name": r.name, "Client Name": c.name}
