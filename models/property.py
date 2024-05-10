from models.connect import CONN, CURSOR


class Property:
    all = {}

    def __init__(self, name, address, price, status, id=None):

        self.id = id
        self.name = name
        self.address = address
        self.price = price
        self.status = status

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

    def address(self):
        return self.address

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        if isinstance(price, int):
            self._price = price
        else:
            raise ValueError("You have not provided a number")

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        if value in ["BUY", "SOLD", "buy", "sold", "On Sale"]:
            self._status = value
        else:
            raise ValueError("Invalid word")

    @classmethod
    def create_table(cls):
        sql = """CREATE TABLE IF NOT EXISTS properties (id INTEGER PRIMARY KEY, name TEXT, address VARCHAR, 
        price INTEGER, 
        status TEXT )"""
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """ Drop the Property table """
        sql = """
            DROP TABLE IF EXISTS properties;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        """ Insert a new row with Property values"""
        sql = """
            INSERT INTO properties (name, address, price, status )
            VALUES (?, ?, ?, ?)
        """

        CURSOR.execute(sql, (self.name, self.address, self.price, self.status))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, name, address, price, status):

        property_item = cls(name, address, price, status)
        property_item.save()
        return property_item

    def update(self):
        sql = """UPDATE properties SET name = ?, address = ?, price = ?, status = ? WHERE id 
        = ?"""
        CURSOR.execute(sql, (self.name, self.address, self.price, self.status, self.id))
        CONN.commit()

    def delete(self):
        """Deletes property row"""

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
        """Return a Property object having the from the table row."""

        # Check the dictionary for an existing instance using the row's primary key
        property_item = cls.all.get(row[0])
        if property_item:
            # ensure attributes match row values in case local instance was modified
            property_item.name = row[1]
            property_item.address = row[2]
            property_item.price = row[3]
            property_item.status = row[4]
        else:
            # not in dictionary, create new instance and add to dictionary
            property_item = cls(row[1], row[2], row[3], row[4])
            property_item.id = row[0]
            cls.all[property_item.id] = property_item
        return property_item

    @classmethod
    def get_all(cls):

        sql = """
            SELECT *
            FROM properties
        """

        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):

        sql = """
            SELECT *
            FROM properties
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None
