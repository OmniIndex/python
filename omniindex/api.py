import requests
import json

class OmniIndexClient:
    """Instantiate an Omniindex client object to interact with the Omniindex API.
    Parameters are:
    :param server: The server to connect to. This can be either "testnet" or "mainnet".
    :type server: str
    :param api_key: The API key to use for authentication.
    :type api_key: str
    :param unit_name: The name of the unit to use for the transaction.
    :type unit_name: str
    :param user: The user to use for the transaction.
    :type user: str
    :param block_type: The type of block to use for the transaction.
    """
    def __init__(self, server, api_key, unit_name, block_type, user):
        self.server = server
        self.api_key = api_key
        self.unit_name = unit_name
        self.block_type = block_type
        self.user = user

    def get_block_schematic(self):
        """Omniindex API call to get the schematic of a block.

        Returns:
            str: JSON string containing the block schematic.
        """
        url = "https://api.omniindex.xyz/api_v1/getblockschematic"

        payload = json.dumps({
            "unitName": self.unit_name,
            "server": self.server,
            "Type": self.block_type,
            "user": self.user,
            "password": self.api_key
        })
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        return response.text
