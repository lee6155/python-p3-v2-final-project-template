from models.__init__ import CONN, CURSOR

class File:
    all = {}
    files_of_users = []

    def __init__(self, file_name, file_type, description, user_id, id=None):
        for file in File.files_of_users:
            if file[0] == file_name and file[1] == user_id:
                raise NameError("This file name already exists for this user")
        self.id = id
        self.file_name = file_name
        self.file_type = file_type
        self.description = description
        self.user_id = user_id
        File.append(file_name, user_id)

    def __repr__(self):
        return f"File {self.id}: {self.file_name}, {self.file_type}, {self.description}, User ID: {self.user_id}"
    
    @property
    def file_name(self):
        return self._file_name
    
    @file_name.setter
    def file_name (self, value):
        if type(value) != str:
            raise TypeError("File name must be a string")
        if len(value) < 1 or len(value) > 30:
            raise ValueError("File name must be between 1 and 30 characters")

        self._file_name = value

    @property
    def file_type(self):
        return self._file_type
    
    @file_type.setter
    def file_type (self, value):
        if type(value) != str:
            raise TypeError("File type must be a string")
        if value != ".doc" or value != ".xls" or value != ".ppt" or value != ".pdf":
            raise TypeError("File type must be .doc, .xls, .ppt or .pdf")
        if hasattr(self, '_file_type'):
            raise AttributeError("This attribute is immutable")

        self._file_type = value

    @property
    def description(self):
        return self._description
    
    @description.setter
    def description (self, value):
        if type(value) != str:
            raise TypeError("The file description must be a string")
        if len(value) < 1 or len(value) > 100:
            raise ValueError("The file description must be between 1 and 100 characters")

        self._description = value

    @classmethod
    def append(cls, file_name, user_id):
        cls.files_of_users.append([file_name, user_id])

    @classmethod
    def create_table(cls):
        sql = """
           CREATE TABLE IF NOT EXISTS files (
           id INTEGER PRIMARY KEY,
           file_name TEXT,
           file_type TEXT,
           description TEXT,
           user_id INTEGER,
           FOREIGN KEY (user_id) REFERENCES users(id))
        """
        CURSOR.execute(sql)
        CONN.commit()
    
    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS files
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def create(cls, file_name, file_type, description, user_id):
        file = cls(file_name, file_type, description, user_id)
        file.save()
        return file

    def save(self):
        sql = """
            INSERT INTO files (file_name, file_type, description, user_id)
            VALUES (?,?,?,?)
        """

        CURSOR.execute(sql, (self.file_name, self.file_type, self.description, self.user_id))
        CONN.commit()

        self.id = CURSOR.lastrowid
        File.all[self.id] = self

    def delete(self):
        sql = """
            DELETE FROM files
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        del File.all[self.id]

    @classmethod
    def get_all(cls):
        sql = """
            SELCT *
            FROM files
        """

        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]

    @classmethod 
    def instance_from_db(cls, row):
        file = cls.all.get(row[0])
        if file:
            file.file_name = row[1]
            file.file_type = row[2]
            file.description = row[3]
            file.user_id = row[4]
        else:
            file = cls(row[1], row[2], row[3], row[4])
            file.id = row[0]
            cls.all[file.id] = file
    
    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT *
            FROM files
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None