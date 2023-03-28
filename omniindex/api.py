import requests
import json

class OmniIndexClient:
    """
    Instantiate an Omniindex client object to interact with the Omniindex API.
    
    :param server: The server to connect to. This is the node server for your blockchain, refer to the Omniindex documentation for more information.
    :type server: str
    :param api_key: The API key to use for authentication.
    :type api_key: str
    :param unit_name: The name of the unit to use for the transaction.
    :type unit_name: str
    :param user: The user to use for the transaction.
    :type user: str
    :param block_type: The type of block to use for the transaction.

    For more information on the client object and elements refer to the `OmniIndex Documentation <https://omniindex.io/docs/>`_.
    
    """
    def __init__(self, server, api_key, unit_name, block_type, user):
        self.server = server
        self.api_key = api_key
        self.unit_name = unit_name
        self.block_type = block_type
        self.user = user

    def get_block_schematic(self):
        """
        Omniindex API call to get the schematic of a block. Before you can do any work with Omniindex you must first get the schematic of the block you want to use. This will return a JSON string containing the schematic of the block. You can then use this schematic to create a block object.

        Returns:
            str: JSON string containing the block schematic.

        Reference to :func:`omniindex.api.OmniIndexClient.get_block_schematic`.
        
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
