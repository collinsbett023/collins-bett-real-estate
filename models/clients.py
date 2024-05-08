from models.connect import CONN, CURSOR
import re


class Client:
    all = {}

    def __init__(self, name, email, id=None):
        self.id = id
        self.name = name
        self.email = email

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name):
            self._name = name
        else:
            raise ValueError(
                "Name must be a non-empty string"
            )

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        # Regular expression pattern to validate email format
        email_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"

        if re.match(email_pattern, email):
            self._email = email
        else:
            raise ValueError("Invalid email format. Please provide a valid email address.")

    @classmethod
    def create_table(cls):
        sql = """CREATE TABLE IF NOT EXISTS clients (id INTEGER PRIMARY KEY, name TEXT, email VARCHAR)"""
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """ Drop the table that persists Department instances """
        sql = """
            DROP TABLE IF EXISTS clients;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        """ Insert a new row with the name and location values of the current Department instance.
        Update object id attribute using the primary key value of new row.
        Save the object in local dictionary using table row's PK as dictionary key"""
        sql = """
            INSERT INTO clients (name, email)
            VALUES (?, ?)
        """

        CURSOR.execute(sql, (self.name, self.email))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, name, email):
        """ Initialize a new Department instance and save the object to the database """
        client = cls(name, email)
        client.save()
        return client

    def update(self):
        sql = """UPDATE properties SET name = ?, email = ? WHERE id = ? """
        CURSOR.execute(sql, (self.name, self.email, self.id))
        CONN.commit()

    def delete(self):
        """Delete the table row corresponding to the current Department instance,
        delete the dictionary entry, and reassign id attribute"""

        sql = """
            DELETE FROM properties
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        # Delete the dictionary entry using id as the key
        del type(self).all[self.id]

        # Set the id to None
        self.id = None

    @classmethod
    def instance_from_db(cls, row):
        """Return a Department object having the attribute values from the table row."""

        # Check the dictionary for an existing instance using the row's primary key
        client = cls.all.get(row[0])
        if client:
            # ensure attributes match row values in case local instance was modified
            client.name = row[1]
            client.email = row[2]
        else:
            # not in dictionary, create new instance and add to dictionary
            client = cls(row[1], row[2])
            client.id = row[0]
            cls.all[client.id] = client
        return client

    @classmethod
    def get_all(cls):
        """Return a list containing a Department object per row in the table"""
        sql = """
            SELECT *
            FROM clients
        """

        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        """Return a Department object corresponding to the table row matching the specified primary key"""
        sql = """
            SELECT *
            FROM clients
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None
