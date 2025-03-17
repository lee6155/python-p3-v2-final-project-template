from models.__init__ import CONN, CURSOR

from models.user import (
    User
)

class File:
    all = {}
    
    def __init__(self, file_name, file_type, description, user_id, id=None):
        self.id = id
        self.file_name = file_name
        self.file_type = file_type
        self.description = description
        self.user_id = user_id
        # self.check_file_name(file_name, user_id)

    # @classmethod
    # def check_file_name(cls, file_name, user_id):
    #     sql = """
    #         SELECT *
    #         FROM files
    #         WHERE file_name = ? AND user_id = ?
    #     """

    #     row = CURSOR.execute(sql, (file_name, user_id)).fetchall()

    #     if row != []:
    #         raise NameError("This file name already exists for this user")
        
    def get_username_from_user_id(user_id):
        sql = """
            SELECT *
            FROM users
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (user_id,)).fetchone()
        user = User.instance_from_db(row)
        username = user.username
        return username
    
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
        if value != ".doc" and value != ".xls" and value != ".ppt" and value != ".pdf":
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
        def check_file_name_and_user(file_name, user_id):
            sql = """
                SELECT *
                FROM files
                WHERE file_name = ? AND user_id = ?
            """

            row = [CURSOR.execute(sql, (file_name, user_id)).fetchone()]

            if row != [None]:
                raise NameError("This file name for this user already exists. Please choose another.")

        check_file_name_and_user(file_name, user_id)

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
            SELECT *
            FROM files
        """

        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]

    @classmethod 
    def instance_from_db(cls, row):
        file = cls.all.get(row[0])

        if file:
            file.file_name = row[1]
            # file.file_type = row[2]
            file.description = row[3]
            file.user_id = row[4]
            return file
        else:
            file = cls(row[1], row[2], row[3], row[4])
            file.id = row[0]
            cls.all[file.id] = file
            return file

    @classmethod
    def files_by_type(cls, file_type):
        sql = """
            SELECT *
            FROM files
            WHERE file_type = ?
        """

        rows = CURSOR.execute(sql, (file_type,)).fetchall()
        return [cls.instance_from_db(row) for row in rows]
    
    def files_by_user(id):
        sql = """
            SELECT *
            FROM files
            WHERE user_id = ?
        """

        rows = CURSOR.execute(sql, (id,)).fetchall()
        return [File.instance_from_db(row) for row in rows]

    @classmethod
    def files_by_type_and_user(cls, file_type_selected, id_selected):
        user_files = File.files_by_user(id_selected)
        
        user_files_by_type = [file for file in user_files if file.file_type == file_type_selected]
        return user_files_by_type

    @classmethod
    def number_files(cls):
        files = File.get_all()
        count = len(files)
        return count
    
    @classmethod
    def number_files_by_type(cls, file_type):
        files = File.files_by_type(file_type)
        count = len(files)
        return count
    
    @classmethod
    def number_files_by_user(cls, user_id):
        files = File.files_by_user(user_id)
        count = len(files)
        return count

    @classmethod
    def number_files_by_type_and_user(cls, file_type, user_id):
        files = File.files_by_type_and_user(file_type, user_id)
        count = len(files)
        return count

    @classmethod
    def search_file_name(cls, search):
        sql = """
            SELECT *
            FROM files
            WHERE file_name LIKE ?
        """

        rows = CURSOR.execute(sql, ('%' + search + '%',)).fetchall()
        return [File.instance_from_db(row) for row in rows]

    @classmethod
    def search_file_name_and_user(cls, search_term, id):
        searched_file_names = File.search_file_name(search_term)

        searched_by_both = [file for file in searched_file_names if file.user_id == id]
        return searched_by_both
    
    @classmethod
    def count_searched_file_name(cls, search):
        files = File.search_file_name(search)
        count = len(files)
        return count
    
    @classmethod
    def count_searched_file_name_and_user(cls, search_term, id):
        files = File.search_file_name_and_user(search_term, id)
        count = len(files)
        return count