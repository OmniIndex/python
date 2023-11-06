import requests
import json
import logging

# define constants
DEBUG = False
HEADERS = {'Content-Type': 'application/json',
            'Accept': 'application/json',
            'User-Agent': 'OmniIndex Python Lib',
            'Connection': 'keep-alive'
        }

# Configure logging
if DEBUG:
    logging.basicConfig(filename='omni_api_log_file.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
else:
    logging.basicConfig(filename='omni_api_log_file.log', level=logging.WARNING, format='%(asctime)s - %(levelname)s - %(message)s')

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
    :type block_type: str
    :param base_url: The base_url of the OmniIndex API Server. Default is https://api.omniindex.xyz/api_v1/
    :type block_type: str

    For more information on the client object and elements refer to the `OmniIndex Documentation <https://omniindex.io/docs/>`_.
    
    """
    def __init__(self, server, api_key, unit_name, block_type, user, base_url):
        self.server = server
        self.api_key = api_key
        self.unit_name = unit_name
        self.block_type = block_type
        self.user = user
        self.base_url = base_url

    def get_block_schematic(self):
        """
        Omniindex API call to get the schematic of a block. Before you can do any work with Omniindex you must first get the schematic of the block you want to use. This will return a JSON string containing the schematic of the block. You can then use this schematic to create a block object.
        This POST method will bring back the schematic of a block that the user has access to

        :param method: (hard coded) HTTP request method (POST)
        :param url: URL to the Omniindex API endpoint. default is https://api.omniindex.xyz/api_v1/getblockschematic 
        :param payload: JSON string containing the unit name, server, block type, user and API key.
        :param headers: (hard coded) Content-Type and Accept headers.
        :param response: Response from the API call.
        :type method: str
        :type url: str
        :type payload: str
        :type headers: dict
        :type response: str
        :type response: str
        
        :returns: JSON string containing the block schematic.

        Reference to :func:`omniindex.api.OmniIndexClient.get_block_schematic`.
        
        """
        url = self.base_url + "/getblockschematic"

        payload = json.dumps({
            "unitName": self.unit_name,
            "server": self.server,
            "Type": self.block_type,
            "user": self.user,
            "password": self.api_key
        })
        

        try: 
            response = requests.request("POST", url, headers=HEADERS, data=payload)
            return response.text
        except Exception as e:
            logging.error(e)
            response = "{ \"Success\" : \"Fail\", \"Message\" : \"" + e + "\" }"
            return response.text

    def get_folders(self, show_protected):
        """
        Omniindex API call to get the folders in a block. This POST method will bring back the folders in a block that the user has access to.
        OmniIndex allows you to save ‘file structure’ to the blockchain. This capability allows you to securely encrypt your critical data as a file system from a variety of tools. 
        We built the Dropblock Add-on for Google Workspace and BigQuery as a perfect implementation of this capability. And it is further enhanced by the ability to redact (partially encrypt) data from within a document into a separate block. (We’ll see more of that later in the documentation. But you can do this from any tool you wish via the API.)
        **Notice the extra key in this JSON object: ‘showProtected’. You must declare ‘true’, or the default value false will be used.**    

        .. note::
            When set ‘true’, the full folder name will be returned in the result set.
            When  set ‘false’, the folder name is redacted. However, you can see that one exists.
            [case sensitive, default is false]

        This API allows an authorized user to view the folder structure of a block they have the required permissions to inspect:

        :param method: (hard coded) HTTP request method (POST)
        :param url: URL to the Omniindex API endpoint. default is https://api.omniindex.xyz/api_v1/getblockschematic 
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
        
        :returns: JSON string containing the folders in the block.

        Reference to :func:`omniindex.api.OmniIndexClient.get_folders`.
        
        """
        url = self.base_url +"/getfolders"

        payload = json.dumps({
            "unitName": self.unit_name,
            "server": self.server,
            "showProtected": show_protected,
            "user": self.user,
            "password": self.api_key
        })

        response = requests.request("POST", url, headers=HEADERS, data=payload)
        return response.text

    def get_searchchain(self, show_protected, search_phrase, search_type): 
        
        """
        Omniindex API call to search the entire unitname in the blockchain. This POST method will bring back documents in a block that the user has access to.
        Using showProtected, you can search the entire blockchain for a specific phrase. This is a powerful capability that allows you to search for documents that contain a specific phrase including redacted data.
        Using searchType, you can search for a specific type of search, either of just the document contents or of the titles, filenames and contents.
        With this API Call, we can return datasets using familiar, natural language search techniques of the encrypted data on the blockchain. 

        .. note::
            This is an API call that demonstrates the power of OmniIndex. In this result set, you can see that the document is redacted. However, the search phrase is still visible. This is a powerful capability that allows you to search for documents that contain a specific phrase including redacted data without ever needing to decrypt the data.
            As well as that you can see the sentiment analysis of the document as well as the context (as analysed against the machine learning (narrow AI) ontology)

        :param show_protected: "true" or "false" (default is "false") sets if the search will include redacted content.
        :param search_phrase: a string to search for.
        :param search_type: "fulltext" or "files" (default is "fulltext") FullText will search the file names, folder names, content, and dates, while files will only search within the content of the files:
        :param method: (hard coded) HTTP request method (POST)
        :param url: URL to the Omniindex API endpoint. default is https://api.omniindex.xyz/api_v1/getblockschematic 
        :param payload: JSON string containing the unit name, server, block type, user and API key.
        :param headers: (hard coded) Content-Type and Accept headers.
        :param response: Response from the API call.
        :type show_protected: str
        :type search_phrase: str
        :type search_type: str
        :type method: str
        :type url: str
        :type payload: str
        :type headers: dict
        :type response: str

        :returns: JSON string containing the search results.

        reference to :func:`omniindex.api.OmniIndexClient.get_searchchain`.
        
        """
        url = self.base_url +"/searchchain"

        payload = json.dumps({
            "unitName": self.unit_name,
            "server": self.server,
            "showProtected": show_protected,
            "phrase": search_phrase,
            "searchType": search_type,
            "user": self.user,
            "password": self.api_key,
            "type": self.block_type
        })

        response = requests.request("POST", url, headers=HEADERS, data=payload)
        return response.text

    def getfiles(self, show_protected, folder_name):
        """

        Omniindex API call to get the files in a given `folder_name` in a block. This POST method will bring back the files in a block that the user has access to.
        OmniIndex allows you to save ‘file structure’ to the blockchain. This capability allows you to securely encrypt your critical data as a file system from a variety of tools. 
        We built the Dropblock Add-on for Google Workspace and BigQuery as a perfect implementation of this capability. And it is further enhanced by the ability to redact (partially encrypt) data from within a document into a separate block. (We’ll see more of that later in the documentation. But you can do this from any tool you wish via the API.)

        **Notice the extra key in this JSON object: ‘showProtected’. You must declare ‘true’, or the default value false will be used.**    

        .. note::
            When set ‘true’, the full file name will be returned in the result set.
            When  set ‘false’, the file name is redacted. However, you can see that one exists.
            [case sensitive, default is false]

        This API allows an authorized user to view the files within a folder structure of a block they have the required permissions to inspect:

        :param show_protected: "true" or "false" (default is "false") sets if the search will include redacted content.
        :param folder_name: a string to search for.
        :param method: (hard coded) HTTP request method (POST)
        :param url: URL to the Omniindex API endpoint. default is https://api.omniindex.xyz/api_v1/getblockschematic 
        :param payload: JSON string containing the unit name, server, block type, user and API key.
        :param headers: (hard coded) Content-Type and Accept headers.
        :param response: Response from the API call.
        :type method: str
        :type url: str
        :type showProtected: str
        :type folder_name: str
        :type payload: str
        :type headers: dict
        :type response: str

        :returns: JSON string containing the files in the block.

        Reference to :func:`omniindex.api.OmniIndexClient.getfiles`.

        .. todo: 
            should we return a JSON object instead of a string?
            maybe we could be consistent re get_folders and getfiles (use of underscore)

        """
        url = self.base_url +"/getfiles"

        payload = json.dumps({
            "unitName": self.unit_name,
            "server": self.server,
            "showProtected": show_protected,
            "folder": folder_name,
            "user": self.user,
            "password": self.api_key,
            "type": self.block_type
        })

        response = requests.request("POST", url, headers=HEADERS, data=payload)
        return response.text
    def run_analytic_query(self, show_protected, query):
        """
        This POST method will run a query on the Blockchain. To use it you are required to know the definition of the blocks that you are querying. 
        If your `where` syntax includes data that has been encrypted for searching you need to use curly braces around your search string. 
        EG: SELECT X FROM Y where thissearchableowners LIKE '%{what am i searching for}%'. The API will then convert this into a searchable ciphered stream.
        
        Unlike standard SQL, there is no need to include the name of the datastore because that is defined by the unitName that we are working with. Similarly, there are no joins in ‘runanalyticquery’, but you can ‘SELECT’, ‘ORDER’, ‘LIMIT’ and set parameters including ‘LIKE’ to return the data that you want to query

        .. note::
                when returning ‘data objects’ as opposed to ‘file objects’, these will be base64 encoded and you will need to handle decoding in your own scripts. This is standard practice for all major data store providers
                

        :param show_protected: "true" or "false" (default is "false") sets if the search will include redacted content.
        :param query: a string to search for.
        :param method: (hard coded) HTTP request method (POST)
        :param url: URL to the Omniindex API endpoint. default is https://api.omniindex.xyz/api_v1/getblockschematic 
        :param payload: JSON string containing the unit name, server, block type, user and API key.
        :param headers: (hard coded) Content-Type and Accept headers.
        :param response: Response from the API call.
        :type method: str
        :type url: str
        :type showProtected: str
        :type query: str
        :type payload: str
        :type headers: dict
        :type response: str

        :returns: JSON string containing the matches for the query.

        Reference to :func:`omniindex.api.OmniIndexClient.run_analytic_query`.
        """	
        url = self.base_url +"/runanalyticquery"

        payload = json.dumps({
            "unitName": self.unit_name,
            "server": self.server,
            "showProtected": show_protected,
            "analyticQuery": query,
            "user": self.user,
            "password": self.api_key,
            "type": self.block_type
        })

        response = requests.request("POST", url, headers=HEADERS, data=payload)
        return response.text

    def post_minedata(self, key, data):
        """
        This POST method will add a block to the chain. This is a very dynamic call, that requires a json object with the data to be sent to the server. 
        As of version 0.1.11, the JSON parser will not allow anything other than a string to be sent to the server. We will be adding INT and FLOAT support in the future.
        
        This object MUST follow the follwing rules: Any object that needs to be encrypted, the key must have the word 'Encrypt' added to it. 
        EG: fileContentsEncrypt. 
        
        This will ensure that the SDK encrypts the value in all methods available prior to it being sent to a node. 
        
        All things OmniIndex, tend to make incredibly complex things, for which we hold multiple patents, very simple indeed. `minedata` is no exception, indeed it is the poster child for simplicity. To create an OmniIndex Blockchain you simply need to create a 
        master encryption key, declare the unit_name of your choice, a user and their api key / passphrase / password (whatever you want).
        

        :param data: a string of JSON which is merged with the credentials payload to form the new block.
        :param method: (hard coded) HTTP request method (POST)
        :param url: URL to the Omniindex API endpoint. default is https://api.omniindex.xyz/api_v1/getblockschematic 
        :param payload: JSON string containing the unit name, server, block type, user and API key.
        :param headers: (hard coded) Content-Type and Accept headers.
        :param response: Response from the API call.
        :param key: the base encryption key to use for the new block.
        :type method: str
        :type url: str
        :type data: str
        :type payload: str
        :type headers: dict
        :type response: str
        :type key: str

        :returns: JSON string containing new block.

        Reference to :func:`omniindex.api.OmniIndexClient.post_minedata`.
        """
        url = self.base_url +"/minedata"

        # Load the JSON strings into Python dictionaries
        pre_payload1 = json.loads(data)

        pre_payload2 = json.dumps({
            "unitName": self.unit_name,
            "server": self.server,
            "user": self.user,
            "password": self.api_key,
            "Type": self.block_type,
            "key": key
        })

        # Merge the two dictionaries
        merged_payload = { **json.loads(pre_payload2), **pre_payload1}
        payload = json.dumps(merged_payload)

        if DEBUG:
            logging.debug(f"payload value = {payload}")
        

        response = requests.request("POST", url, headers=HEADERS, data=payload)
        return response.text
