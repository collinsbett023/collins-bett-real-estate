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
        """ Insert a new row with the name, job title, and department id values of the current Employee object.
        Update object id attribute using the primary key value of new row.
        Save the object in local dictionary using table row's PK as dictionary key"""
        sql = """
                INSERT INTO contracts (property_id, client_id, realtor_id)
                VALUES (?, ?, ?)
        """

        CURSOR.execute(sql, (self.property_id, self.client_id, self.realtor_id))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    def delete(self):
        """Delete the table row corresponding to the current Employee instance,
        delete the dictionary entry, and reassign id attribute"""

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
        """ Initialize a new Employee instance and save the object to the database """
        contract = cls(property_id, client_id, realtor_id)
        contract.save()
        return contract

    @classmethod
    def drop_table(cls):
        """ Drop the table that persists Department instances """
        sql = """
            DROP TABLE IF EXISTS contracts;
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def instance_from_db(cls, row):
        """Return an Employee object having the attribute values from the table row."""

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
        """Return a list containing one Employee object per table row"""
        sql = """
            SELECT *
            FROM contracts
        """

        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        """Return Employee object corresponding to the table row matching the specified primary key"""
        sql = """
            SELECT *
            FROM contracts
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None
