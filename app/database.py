import psycopg2
from psycopg2.extras import RealDictCursor

class Database:
    def __init__(self,dbname,user,password,host="localhost",port=5432):
        self.dbname = dbname
        self.user =user
        self.password = password
        self.host = host
        self.port = port

    def connect(self):
        try:
            conn = psycopg2.connect(
                dbname = self.dbname,
                user = self.user,
                password = self.password,
                host = self.host,
                port = self.port,
                cursor_factory=RealDictCursor
            )
            return conn
        except Exception as e:
            print(f"Error connecting to the data base: {e}")


# db = Database()
# db.connect()