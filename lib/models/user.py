from models.__init__ import CONN, CURSOR

class User:
    all = {}
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
    def username(self, value):
        if type(value) != str:
            raise TypeError("Username must be a string")
        if len(value) < 2 or len(value) > 20:
            raise ValueError("Username must be between 2 and 20 characters")
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
        if value != "personal" and value != "business":
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
        user = cls(username, user_type)
        user.save()
        return user

    def save(self):
        sql = """
            INSERT INTO users (username, user_type)
            VALUES (?,?)
        """

        CURSOR.execute(sql, (self.username, self.user_type))
        CONN.commit()

        self.id = CURSOR.lastrowid
        User.all[self.id] = self

    def delete(self):
        sql = """
            DELETE FROM users
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        
        del User.all[self.id]
        User.usernames.remove(self.username)

    @classmethod
    def get_all(cls):
        sql = """
            SELECT *
            FROM users
        """

        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]

    @classmethod 
    def instance_from_db(cls, row):
        user = cls.all.get(row[0])
        if user:
            # user.username = row[1]
            user.user_type = row[2]
            return user
        else:
            user = cls(row[1], row[2])
            user.id = row[0]
            cls.all[user.id] = user
            return user
    
    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT *
            FROM users
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def users_by_type(cls, user_type):
        sql = """
            SELECT *
            FROM users
            WHERE user_type = ?
        """

        rows = CURSOR.execute(sql, (user_type,)).fetchall()

        users = []
        for row in rows:
            users.append(row[1])
        
        return users
    
    @classmethod
    def number_users_by_type(cls, user_type):
        sql = """
            SELECT COUNT(user_type)
            FROM users
            WHERE user_type = ?
        """

        number = CURSOR.execute(sql, (user_type,)).fetchone()
        return number[0]