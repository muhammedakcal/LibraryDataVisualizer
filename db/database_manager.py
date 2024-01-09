# db/database_manager.py

import mysql.connector
from mysql.connector import Error
from config import Config

class DatabaseManager:
    def __init__(self):
        db_config = Config.DATABASE_CONFIG
        self.host = db_config['host']
        self.database = db_config['database']
        self.user = db_config['user']
        self.password = db_config['password']
        self.connection = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password
            )
        except Error as e:
            print(f"Error connecting to MySQL database: {e}")
            self.connection = None

    def close_connection(self):
        if self.connection and self.connection.is_connected():
            self.connection.close()

    def execute_query(self, query):
        if self.connection is None or not self.connection.is_connected():
            print("Database connection is not established.")
            return None

        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query)
                return cursor.fetchall()
        except Error as e:
            print(f"Failed to execute query: {e}")
            return None
