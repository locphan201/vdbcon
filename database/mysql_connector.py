import mysql.connector
from mysql.connector import Error

class MySQLConnector:
    def __init__(self) -> None:
        self.hostname = ''
        self.database = ''
        self.username = ''
        self.password = ''
        self.conn = None
        self.err = None
        self.tables = {}
        
        # self.tables.clear()
        # tables = self.get_tables()
        # for table in tables[:1]:
        #     columns = self.describe_table(table)
            
        #     temp = {}
        #     for column in columns:
        #         temp[column[0]] = column[1]
                
        #     self.tables[table] = temp
        # print(self.tables)

    def configure(self, hostname: str, database: str, username: str, password: str):
        self.hostname = hostname
        self.database = database
        self.username = username
        self.password = password

    def connect(self):
        try:
            self.conn = mysql.connector.connect(
                host=self.hostname,
                database=self.database,
                user=self.username,
                password=self.password
            )
            return None
        except Error as err:
            return err

    def check_connection(self):
        self.err = self.connect()
        if self.err:
            return self.err.msg
    
        self.conn.close()
        return None
    
    def get_tables(self):
        query = '''
            SHOW TABLES;
        '''

        self.connect()
        cursor = self.conn.cursor()
        try:
            cursor.execute(query)
            tables = cursor.fetchall()
            tables = [table[0] for table in tables]
            self.err = None
            return tables
        except Error as e:
            self.err = e
            return []

    def describe_table(self, table):
        query = f'''
            DESCRIBE {table}
        '''

        self.connect()
        cursor = self.conn.cursor()
        try:
            cursor.execute(query)
            columns = cursor.fetchall()
            self.err = None
            return columns
        except Error as e:
            self.err = e
            return []

    def select_query(self, table):
        query = f'''
            SELECT * FROM {table}
        '''

        self.connect()
        cursor = self.conn.cursor()
        try:
            cursor.execute(query)
            rows = cursor.fetchall()
            result = []
            for row in rows:
                temp = []
                for value in row:
                    if isinstance(value, (bytearray, bytes)):
                        temp.append('BINARY')
                    else:
                        temp.append(str(value))
                result.append(temp)

            self.err = None
            return result
        except Error as e:
            self.err = e
            return []

mysql_db = MySQLConnector()

if __name__ == '__main__':
    status = mysql_db.check_connection()
    print(status)