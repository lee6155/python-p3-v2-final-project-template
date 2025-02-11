from models.__init__ import CONN, CURSOR

class User:
    usernames = []

    def __init__(self, username, user_type, id=None):
        self.id = id
        self.username = username
        self.user_type = user_type
        User.append(self.username)

    def __repr__(self):
        return f"User {self.id}: {self.username}, {self.user_type}"
    
    @property
    def username(self):
        return self._username
    
    @username.setter
    def username (self, value):
        if type(value) != str:
            raise TypeError("Username must be a string")
        if len(value) < 3 or len(value) > 30:
            raise ValueError("Username must be between 3 and 30 characters")
        if hasattr(self, '_username'):
            raise AttributeError("This attribute is immutable")
        if value in User.usernames:
            raise NameError("This username already exists. Please choose another.")
        
        self._username = value

    @property
    def user_type(self):
        return self._user_type
    
    @user_type.setter
    def user_type (self, value):
        if type(value) != str:
            raise TypeError("The user type must be a string")
        if value != "personal" or value != "business":
            raise ValueError("The user type must be either personal or business")
        
        self._user_type = value

    @classmethod
    def append(cls, username):
        cls.usernames.append(username)
    
    @classmethod
    def create_table(cls):
        sql = """
           CREATE TABLE IF NOT EXISTS users (
           id INTEGER PRIMARY KEY,
           username TEXT,
           user_type TEXT)
        """
        CURSOR.execute(sql)
        CONN.commit()
    
    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS users
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def create(cls, username, user_type):
        file = cls(username, user_type)
        file.save()

    def save(self):
        sql = """
            INSERT INTO users (username, user_type)
            VALUES (?,?)
        """

        CURSOR.execute(sql, (self.username, self.user_type))
        CONN.commit()

        self.id = CURSOR.lastrowid

    def delete(self):
        sql = """
            DELETE FROM users
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()