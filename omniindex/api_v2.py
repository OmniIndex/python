import logging
import requests
import csv
from .api_credentials import APICredentials
from .pgbc_credentials import PGBCCredentials
from .enums import OmniIndexState
import requests
import json

class OmniIndexAPI:
    """
    A class representing the OmniIndex system.
    mniIndex is your custom class. It has an __init__ method, which is the constructor of the class. 
    This method is called when you create a new instance of the class. 
    The _loadOmniConfig and _retrieveDomainKey methods are used to load the configuration and retrieve the domain key, respectively.

    Attributes:
        debug (bool): Indicates whether debug output should be printed.
        _credentials (APICredentials): The credentials for the OmniIndex system.
        _state (OmniIndexState): The current state of the OmniIndex system.

    Example:

    """


    def __init__(self, input_key: str, username: str = "some_name", password: str = "some_password"):
        """
        Initializes the DatabaseAPI with an input key, username, and password.

        Args:
            input_key (str): The input key for the API.
            username (str, optional): The username for authentication. Defaults to "some_name".
            password (str, optional): The password for authentication. Defaults to "some_password".
        """
        self.input_key = input_key
        self.username = username
        self.password = password
        self.base_url = "http://api.pgbc.info/cgi-bin/pgbc_api/"

    def add_block_data(self, ddl: str) -> str:
        """
        Sends a POST request to the API to add block data.

        Args:
            ddl (str): The Data Definition Language parameter to be added.

        Returns:
            str: The response from the API as text.
        """
        url = f"{self.base_url}add_block_data?"
        encoded_ddl = ddl.replace(" ", "%20")
        url = url + f"username={self.username}&password={self.password}&ddl={encoded_ddl}"

        headers = {
            "AUTHORIZATION": f"Basic {self.input_key}",
            "Referer": "OmniIndex Python Connector",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        }

        try:
            response = requests.post(url, headers=headers)
            response.raise_for_status()
            return response.text
        except requests.exceptions.RequestException as err:
            logging.error("Error: %s", err)
            return None  # Updated return type hint to indicate it can return None


