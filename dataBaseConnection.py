import psycopg2

class Database:
    def __init__(self):
        self.connection = psycopg2.connect(
            host="localhost",
            database="postgres",
            user="gaffaell",
            password="1234"
        )
        self.cursor = self.connection.cursor()

    def execute_query(self, query, params=None):
        self.cursor.execute(query, params)
        self.connection.commit()

    def fetch_all(self, query, params=None):
        self.cursor.execute(query, params)
        return self.cursor.fetchall()

    def close(self):
        self.cursor.close()
        self.connection.close()
    
    def loadData(self, params=None):
        query = "SELECT * FROM agenda"
        self.cursor.execute(query, params)
        return self.cursor.fetchall()