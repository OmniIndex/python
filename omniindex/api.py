from api_credentials import APICredentials
from pgbc_credentials import PGBCCredentials
from enums import OmniIndexState
import requests
import json

class OmniIndex:
    """
    A class representing the OmniIndex system.
    mniIndex is your custom class. It has an __init__ method, which is the constructor of the class. 
    This method is called when you create a new instance of the class. 
    The _loadOmniConfig and _retrieveDomainKey methods are used to load the configuration and retrieve the domain key, respectively.

    Attributes:
        debug (bool): Indicates whether debug output should be printed.
        _config_locale (str): The path to the JSON configuration file.
        _credentials (APICredentials): The credentials for the OmniIndex system.
        _state (OmniIndexState): The current state of the OmniIndex system.

    Example:
    ```python
    omniIndex = OmniIndex.withAPICredentials(apiCredentials=APICredentials(aPIServer='test-api-server', seedNode='test-seed-node', localDomain='com.omniindex.test', nodeServer='test-node-server.io'))
    print(omniIndex._credentials.nodeServer)  # Output: test-node-server.io
    ```

    """

    def __init__(self, config_locale=None, debug=False):
        """
        Initializes a new instance of the OmniIndex class.

        Args:
            config_locale (str, optional): The path to the JSON configuration file. Defaults to None.
            debug (bool, optional): Indicates whether debug output should be printed. Defaults to False.

        """
        self.debug = debug
        self._config_locale = config_locale or 'assets/configurations/omniindex.json'
        self._credentials = APICredentials()
        self._state = OmniIndexState.uninitialized

    @property
    def state(self):
        """
        Gets the current state of the OmniIndex system.

        Returns:
            OmniIndexState: The current state of the OmniIndex system.

        """
        return self._state

    @classmethod
    def with_api_credentials(cls, api_credentials, debug=False):
        """
        Creates a new instance of the OmniIndex class with API credentials.

        Args:
            api_credentials (APICredentials): The API credentials for the OmniIndex system.
            debug (bool, optional): Indicates whether debug output should be printed. Defaults to False.

        Returns:
            OmniIndex: A new instance of the OmniIndex class with API credentials.

        """
        instance = cls(debug=debug)
        instance._credentials = api_credentials
        instance._configLocale = ''
        instance._state = OmniIndexState.configured
        return instance

    @classmethod
    def with_pgbc_credentials(cls, pgbc_credentials, debug=False):
        """
        Creates a new instance of the OmniIndex class with pgbc credentials.

        Args:
            pgbc_credentials (PGBCCredentials): The PGBC credentials for the OmniIndex system.
            debug (bool, optional): Indicates whether debug output should be printed. Defaults to False.

        Returns:
            OmniIndex: A new instance of the OmniIndex class with PGBC credentials.

        """
        instance = cls(debug=debug)
        instance._credentials = pgbc_credentials
        instance._configLocale = ''
        instance._state = OmniIndexState.configured
        return instance

    def _load_omni_config(self, authorize=False, nowait=False):
        """
        Loads the configuration for the OmniIndex system from a JSON file.

        Args:
            authorize (bool, optional): Indicates whether to authorize the OmniIndex system after loading the configuration. Defaults to False.
            nowait (bool, optional): Indicates whether to wait for the domain key retrieval to complete before continuing. Defaults to False.

        """
        if self._state == OmniIndexState.uninitialized:
            self._state = OmniIndexState.initialized

        try:
            with open(self._configLocale) as f:
                json_conf = json.load(f)

            self._debugOutput("omniindex.py _loadOmniConfig: " + str(json_conf))

            self._credentials = APICredentials.withDomainKey(
                aPIServer=json_conf["apiServer"],
                seedNode=json_conf["seedNode"],
                nodeServer=json_conf["nodeJS"],
                localDomain=json_conf["localDomain"],
                domainKey=json_conf["domainKey"]
            )

            self._state = OmniIndexState.configured if self._credentials.are_valid() else OmniIndexState.invalid

            if self._credentials.are_valid() and authorize:
                if nowait:
                    self._retrieveDomainKey()
                else:
                    self._retrieveDomainKey().result()
        except Exception:
            self._state = OmniIndexState.invalid

    def _retrieve_domain_key(self):
        """
        Retrieves the domain key for the OmniIndex system by making a POST request to the specified node server.

        """
        if not self._credentials.are_valid():
            self._state = OmniIndexState.invalid
            return

        response = requests.post(
            url=f"{self._credentials.nodeServer}/unit-name",
            headers={"Content-Type": "application/json"},
            data=json.dumps({
                "id": self._credentials.domainKey,
                "unit": self._credentials.localDomain
            })
        )

        self._debugOutput("Unit ID : " + response.text)

        if not response.text:
            self._credentials.domainKey = ""
            self._state = OmniIndexState.invalid

        self._credentials.domainKey = response.text

    def _debug_output(self, message):
        """
        Prints the debug output if debug mode is enabled.

        Args:
            message (str): The debug message to print.

        """
        if self.debug:
            print(message)
