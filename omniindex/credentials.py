from .enums import OmniIndexAuthenticationType

class BasicCredentials:
    """
    Represents basic authentication credentials.
    
    In this script, BasicCredentials is your custom class. 
    It has an __init__ method, which is the constructor of the class. 
    This method is called when you create a new instance of the class. 
    The are_valid method checks if the username and password attributes are not empty
    

    Args:
        username (str): The username for the credentials. Default is an empty string.
        password (str): The password for the credentials. Default is an empty string.
        type (OmniIndexAuthenticationType): The authentication type for the credentials. Default is `OmniIndexAuthenticationType.omniindex`.

    Attributes:
        username (str): The username for the credentials.
        password (str): The password for the credentials.
        type (OmniIndexAuthenticationType): The authentication type for the credentials.

    Methods:
        are_valid: Checks if the username and password are not empty.

    Example Usage:
        credentials = BasicCredentials(username='admin', password='password')
        print(credentials.are_valid())  # Output: True
    """

    def __init__(self, username='', password='', type=OmniIndexAuthenticationType.omniindex):
        self.username = username
        self.password = password
        self.type = type

    def are_valid(self):
        """
        Checks if the username and password are not empty.

        Returns:
            bool: True if both the username and password are not empty, False otherwise.
        """
        return bool(self.username) and bool(self.password)
