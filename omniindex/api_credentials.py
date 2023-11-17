from enums import OmniIndexAuthenticationType
from credentials import BasicCredentials

class APICredentials(BasicCredentials):
    """
    A class that represents API credentials.
    APICredentials is your custom class that inherits from BasicCredentials. 
    It has an __init__ method, which is the constructor of the class. 
    This method is called when you create a new instance of the class. 
    The are_valid method checks if the attributes are not empty.

    Args:
        api_server (str): The API server for the credentials.
        seed_node (str): The seed node for the credentials.
        node_server (str): The node server for the credentials.
        local_domain (str): The local domain for the credentials.
        username (str): The username for the credentials.
        password (str): The password for the credentials.
        type (OmniIndexAuthenticationType): The authentication type for the credentials.

    Attributes:
        api_server (str): The API server for the credentials.
        seed_node (str): The seed node for the credentials.
        node_server (str): The node server for the credentials.
        local_domain (str): The local domain for the credentials.
        domain_key (str): The domain key for the credentials.

    Methods:
        with_domain_key: Creates an instance of APICredentials with the domain_key attribute.
        are_valid: Checks if all the attributes are not empty.

    Inherits:
        BasicCredentials: The base class for the APICredentials class.
        
    Example:
    ```python
    credentials = APICredentials(aPIServer='test-api-server', seedNode='test-seed-node', localDomain='com.omniindex.test', nodeServer='test-node-server.io')
    print(credentials.nodeServer)  # Output: test-node-server.io
    print(credentials.are_valid())  # Output: False
    ```
    """

    def __init__(self, api_server=None, seed_node=None, node_server=None, local_domain=None, domain_key=None, username='', password='', type=OmniIndexAuthenticationType.api):
        super().__init__(username, password, type)
        self.api_server = api_server
        self.seed_node = seed_node
        self.node_server = node_server
        self.local_domain = local_domain
        self.domain_key = domain_key

    @classmethod
    def with_domain_key(cls, api_server=None, seed_node=None, local_domain=None, node_server=None, domain_key=None, username='', password='', type=OmniIndexAuthenticationType.api):
        """
        Creates an instance of APICredentials with the domain_key attribute.

        Args:
            api_server (str): The API server for the credentials.
            seed_node (str): The seed node for the credentials.
            local_domain (str): The local domain for the credentials.
            node_server (str): The node server for the credentials.
            domain_key (str): The domain key for the credentials.
            username (str): The username for the credentials.
            password (str): The password for the credentials.
            type (OmniIndexAuthenticationType): The authentication type for the credentials.

        Returns:
            APICredentials: An instance of APICredentials with the domain_key attribute.
        """
        instance = cls(api_server, seed_node, node_server, local_domain, domain_key, username, password, type)
        return instance

    def are_valid(self):
        """
        Checks if all the attributes are not empty.

        Returns:
            bool: True if all the attributes are not empty, False otherwise.
        """
        return bool(self.api_server) and bool(self.seed_node) and bool(self.local_domain) and bool(self.node_server) and bool(self.domain_key)
