import mysql.connector
from mysql.connector import Error

class DBHelper:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None

    def init_db_connection(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            if self.connection.is_connected():
                print("Connection to MySQL DB successful")
        except Error as e:
            print(f"Error: '{e}' occurred while connecting to MySQL DB")

    def fetch_results(self, query, params=None):
        try:
            cursor = self.connection.cursor(dictionary=True)
            cursor.execute(query, params)
            results = cursor.fetchall()
            return results
        except Error as e:
            print(f"Error: '{e}' occurred while fetching results")
        finally:
            cursor.close()

    def update_record(self, query, params):
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, params)
            self.connection.commit()
            print("Record updated successfully")
        except Error as e:
            print(f"Error: '{e}' occurred while updating record")
            self.connection.rollback()
        finally:
            cursor.close()

    def insert_record(self, query, params):
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, params)
            self.connection.commit()
            print("Record inserted successfully")
        except Error as e:
            print(f"Error: '{e}' occurred while inserting record")
            self.connection.rollback()
        finally:
            cursor.close()

    def delete_record(self, query, params):
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, params)
            self.connection.commit()
            print("Record deleted successfully")
        except Error as e:
            print(f"Error: '{e}' occurred while deleting record")
            self.connection.rollback()
        finally:
            cursor.close()

    def close_connection(self):
        if self.connection.is_connected():
            self.connection.close()
            print("MySQL connection is closed")
