import requests
import json

# define constants
HEADERS = {'Content-Type': 'application/json',
            'Accept': 'application/json'
        }


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
        This POST method will bring back the schematic of a block that the user has access to

        :param method: (hard coded) HTTP request method (POST)
        :param url: (hard coded) URL to the Omniindex API endpoint 
        :param payload: JSON string containing the unit name, server, block type, user and API key.
        :param headers: (hard coded) Content-Type and Accept headers.
        :param response: Response from the API call.
        :type method: str
        :type url: str
        :type payload: str
        :type headers: dict
        :type response: str
        :type response: str
        
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
        

        response = requests.request("POST", url, headers=HEADERS, data=payload)
        return response.text

    def get_folders(self, show_protected):
        """
        Omniindex API call to get the folders in a block. This POST method will bring back the folders in a block that the user has access to.
        OmniIndex allows you to save ‘file structure’ to the blockchain. This capability allows you to securely encrypt your critical data as a file system from a variety of tools. 
        We built the Dropblock Add-on for Google Workspace and BigQuery as a perfect implementation of this capability. And it is further enhanced by the ability to redact (partially encrypt) data from within a document into a separate block. (We’ll see more of that later in the documentation. But you can do this from any tool you wish via the API.)
        **Notice the extra key in this JSON object: ‘showProtected’. You must declare ‘true’, or the default value false will be used.**    

        This API allows an authorized user to view the folder structure of a block they have the required permissions to inspect:

        :param method: (hard coded) HTTP request method (POST)
        :param url: (hard coded) URL to the Omniindex API endpoint
        :param showProtected: str value to show protected folders. 
        :param payload: JSON string containing the unit name, server, block type, user and API key.
        :param headers: (hard coded) Content-Type and Accept headers.
        :param response: Response from the API call.
        :type method: str
        :type url: str
        :type showProtected: str
        :type payload: str
        :type headers: dict
        :type response: str
        :type response: str
        
        Returns:
            str: JSON string containing the folders in the block.

        Reference to :func:`omniindex.api.OmniIndexClient.get_folders`.
        
        """
        url = "https://api.omniindex.xyz/api_v1/getfolders"

        payload = json.dumps({
            "unitName": self.unit_name,
            "server": self.server,
            "showProtected": show_protected,
            "user": self.user,
            "password": self.api_key
        })

        response = requests.request("POST", url, headers=HEADERS, data=payload)
        return response.text
