from .credentials import BasicCredentials

class PGBCCredentials(BasicCredentials):
    """
    A class that represents PostgreSQL database credentials.
    
    PGBCCredentials is your custom class that inherits from BasicCredentials. It has an __init__ method, which is the constructor of the class. 
    This method is called when you create a new instance of the class. The are_valid method checks if the attributes are not empty.

    Args:
        data_source (str): The data source name for the PostgreSQL database.
        username (str, optional): The username for the credentials. Default is an empty string.
        password (str, optional): The password for the credentials. Default is an empty string.
        server (str, optional): The server name for the PostgreSQL database. Default is 'localhost'.
        port (int, optional): The port number for the PostgreSQL database. Default is 5434.

    Raises:
        ValueError: If the port number is not within the valid range of 5430 to 5435.

    Attributes:
        dataSource (str): The data source name for the PostgreSQL database.
        server (str): The server name for the PostgreSQL database.
        port (int): The port number for the PostgreSQL database.

    Methods:
        are_valid(): Checks if all the attributes are valid.
        __str__(): Returns a string representation of the PGBCCredentials object.
        __repr__(): Returns a string representation of the PGBCCredentials object.

    Example:
        credentials = PGBCCredentials(data_source='my_db', username='admin', password='password', server='localhost', port=5432)
        print(credentials.are_valid())  # Output: True
        print(credentials)  # Output: PGBCCredentials(dataSource=my_db, username=admin, password=password, server=localhost, port=5432)
    """

    def __init__(self, data_source: str, username: str = '', password: str = '', server: str = 'localhost', port: int = 5434):
        super().__init__(username, password)
        self.dataSource = data_source
        self.server = server
        if isinstance(port, int) and 5430 <= port <= 5435:
            self.port = port
        else:
            raise ValueError("Invalid port number")

    def are_valid(self):
        """
        Checks if all the attributes are valid.

        Returns:
            bool: True if all the attributes are valid, False otherwise.
        """
        if not isinstance(self.port, int) or self.port < 5430 or self.port > 5435:
            return False
        return bool(self.server) and bool(self.dataSource) and bool(self.port) and bool(self.username) and bool(self.password) and super().are_valid()

    def __str__(self):
        """
        Returns a string representation of the PGBCCredentials object.

        Returns:
            str: A string representation of the PGBCCredentials object.
        """
        return f"PGBCCredentials(dataSource={self.dataSource}, username={self.username}, password={self.password}, server={self.server}, port={self.port})"

    def __repr__(self):
        """
        Returns a string representation of the PGBCCredentials object.

        Returns:
            str: A string representation of the PGBCCredentials object.
        """
        return f"PGBCCredentials(dataSource={self.dataSource}, username={self.username}, password={self.password}, server={self.server}, port={self.port})"
