from models.connect import CONN, CURSOR
import re


class Realtor:
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
        sql = """CREATE TABLE IF NOT EXISTS realtors (id INTEGER PRIMARY KEY, name TEXT, email VARCHAR)"""
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):

        sql = """
            DROP TABLE IF EXISTS realtors;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):

        sql = """
            INSERT INTO realtors (name, email)
            VALUES (?, ?)
        """

        CURSOR.execute(sql, (self.name, self.email))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, name, email):

        realtor = cls(name, email)
        realtor.save()
        return realtor

    def update(self):
        sql = """UPDATE properties SET name = ?, email = ? WHERE id = ? """
        CURSOR.execute(sql, (self.name, self.email, self.id))
        CONN.commit()

    def delete(self):

        sql = """
            DELETE FROM realtors
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

        # Check the dictionary for an existing instance using the row's primary key
        realtor = cls.all.get(row[0])
        if realtor:
            # ensure attributes match row values in case local instance was modified
            realtor.name = row[1]
            realtor.email = row[2]
        else:
            # not in dictionary, create new instance and add to dictionary
            realtor = cls(row[1], row[2])
            realtor.id = row[0]
            cls.all[realtor.id] = realtor
        return realtor

    @classmethod
    def get_all(cls):

        sql = """
            SELECT *
            FROM realtors
        """

        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):

        sql = """
            SELECT *
            FROM realtors
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None
