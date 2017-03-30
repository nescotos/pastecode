import sqlite3
connection = sqlite3.connect('pastecode.db')

c = connection.cursor()

c.execute("""
            CREATE TABLE users
            (_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name NVARCHAR(50) NOT NULL,
            email NVARCHAR(50) NOT NULL,
            password NVARCHAR(250) NOT NULL)
            """)

c.execute("""
            CREATE TABLE languages
            (_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name NVARCHAR(50) NOT NULL)
            """)

c.execute("""
            CREATE TABLE codes
            (_id INTEGER PRIMARY KEY AUTOINCREMENT,
            code TEXT NOT NULL,
            owner INTEGER NOT NULL,
            language INTEGER NOT NULL,
            isPublic BOOLEAN NOT NULL,
            FOREIGN KEY(owner) REFERENCES users(_id),
            FOREIGN KEY(language) REFERENCES languages(_id))
            """)

c.execute("""
            CREATE TABLE private_access
            (_id INTEGER PRIMARY KEY AUTOINCREMENT,
            code INTEGER NOT NULL,
            user INTEGER NOT NULL,
            FOREIGN KEY(user) REFERENCES users(_id),
            FOREIGN KEY(code) REFERENCES codes(_id))
            """)

c.execute("""
            CREATE TABLE passwords_private_access
            (_id INTEGER PRIMARY KEY AUTOINCREMENT,
            password NVARCHAR(250) NOT NULL,
            private_access INTEGER NOT NULL,
            FOREIGN KEY(private_access) REFERENCES private_access(_id))
            """)

c.execute("""
            CREATE UNIQUE INDEX name_email_index_unique ON users (name, email)
            """)

connection.commit()
connection.close()
