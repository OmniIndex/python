import psycopg2
import asyncio
from psycopg2 import errors

class Pgbc:
    def __init__(self, server, port, manager_user, user=None, password=None):
        self.server = server
        self.port = port
        self.manager = manager_user
        self.manager_password = password
        self.database_user = 'postgres'
        if user:
            self.database_user = user

    def connect(self, command):
        try:
            conn = psycopg2.connect(
                user=self.database_user,
                host=self.server,
                password=self.manager_password,
                port=self.port
            )
            cursor = conn.cursor()
            cursor.execute(command)
            result = cursor.fetchall()
            conn.close()
            return result
        except errors.DatabaseError as e:
            # Extracting the actual error message
            error_message = str(e).splitlines()[0]
            raise Exception(error_message)
    
    def add_user(self, user_name, password):
        """
        Adds a new user to a PostgreSQL database.

        Args:
            user_name (str): The name of the user to be added.
            password (str): The password for the new user.

        Returns:
            str: The result of the SQL command as a string if the user is successfully added.
            str: The exception message as a string if there is an exception during the execution of the SQL command.

        Raises:
            Exception: If any of the required data is missing.

        Example Usage:
            pgbc = Pgbc(server='localhost', port=5432, manager_user='admin', password='admin123')
            result = pgbc.add_user('john', 'password123')
            print(result)
        """
        if all([user_name, password, self.server, self.port, self.manager, self.manager_password, self.database_user]):
            command = f"SELECT pgbc.add_user('{self.manager}','{self.manager_password}','{user_name}','{password}', '');"
            try:
                results = self.connect(command)
                return str(results[0])
            except Exception as e:
                return str(e)
        else:
            raise Exception("Please check and provide all the required data")

    def modify_user(self, manager_user, manager_password, user_name, password, new_password, to_manager):
        is_manager = bool(manager_user and manager_password)
        
        if not (is_manager or (password and new_password)):
            raise Exception("Your current and new password are required.")

        if not is_manager and to_manager:
            raise Exception("Only a manager can elevate permissions.")

        if all([user_name, password, self.server, self.port, self.manager, self.manager_password, self.database_user]):
            command = f"SELECT pgbc.modify_user('{self.manager}','{self.manager_password}','{user_name}','{password}','{new_password}',{to_manager});"
            try:
                results = self.connect(command)
                return str(results[0])
            except Exception as e:
                return str(e)
        else:
            raise Exception("Please check and provide all the required data")

        if manager_user == self.manager and manager_password == self.manager_password:
            command = "SELECT pgbc.create_block_schema();"
            try:
                results = await self.connect(command)
                return results
            except Exception as err:
                return str(err)
        else:
            print("Authorization failure.")
            return "Authorization failure."
    
    async def create_block_schema(self, manager_user, manager_password):
        if manager_user == self.manager and manager_password == self.manager_password:
            command = "SELECT pgbc.create_block_schema();"
            try:
                results = await self.connect(command)
                return results
            except Exception as err:
                return str(err)
        else:
            print("Authorization failure.")
            return "Authorization failure."

    async def add_block_data(self, manager_user, manager_password, block_data):
        if manager_user == self.manager and manager_password == self.manager_password:
            command = f"SELECT pgbc.add_block_data('{block_data}');"
            try:
                results = await self.connect(command)
                return results
            except Exception as err:
                return str(err)
        else:
            print("Authorization failure.")
            return "Authorization failure."