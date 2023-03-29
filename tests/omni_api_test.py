import pytest
import requests
import json
from omniindex.api import OmniIndexClient

import pytest

# define constants

NODE = 'https://node1.omniindex.xyz/node'
USER_KEY = 'NTAzMjcxMjA5NzM1NjYyMg==' # enronemail

"""
To run these tests
------------------

.. code-block:: bash

    $ python -m pytest tests/

"""
def test_get_block_schematic_returns_json_string():
    """Test that the get_block_schematic() method returns a valid JSON string."""
    client = OmniIndexClient(NODE, USER_KEY, 'enronemail', 'Owner', 'enronemail')
    json_string = client.get_block_schematic()
    assert type(json_string) == str
    assert json.loads(json_string) is not None
    assert json.loads(json_string) != {}

def test_get_folders_true_returns_json_string():
    """Test that the get_block_schematic() method returns a valid JSON string when showProtected is set to true."""
    client = OmniIndexClient(NODE, USER_KEY, 'enronemail', 'Owner', 'enronemail')
    json_string = client.get_folders("true")
    assert type(json_string) == str
    assert json.loads(json_string) is not None
    assert json.loads(json_string) != {}

def test_get_folders_false_returns_json_string():
    """Test that the get_block_schematic() method returns a valid JSON string when showProtected is set to false"""
    client = OmniIndexClient('https://node1.omniindex.xyz/node', 'NTAzMjcxMjA5NzM1NjYyMg==', 'enronemail', 'Owner', 'enronemail')
    json_string = client.get_folders("false")
    assert type(json_string) == str
    assert json.loads(json_string) is not None
    assert json.loads(json_string) != {}
@pytest.fixture
def client():
    return OmniIndexClient(
        server="https://node1.omniindex.xyz",
        api_key="NTAzMjcxMjA5NzM1NjYyMg==",
        unit_name="enronemail",
        block_type="Owner",
        user="enronemail"
    )

def test_init(client):
    assert client.server == "https://node1.omniindex.xyz"
    assert client.api_key == "NTAzMjcxMjA5NzM1NjYyMg=="
    assert client.unit_name == "enronemail"
    assert client.block_type == "Owner"
    assert client.user == "enronemail"

def test_ssl_api_endpoint():
    # import the requests library
    import requests
    
    endpoint = "https://api.omniindex.xyz/api_v1" # set the api endpoint
    response = requests.get(endpoint, verify=True) # make a request to the endpoint
    
    assert response.status_code == 200 # assert that the response is successful

def test_ssl_api_endpoint_getblockschema():
    # import the requests library
    import requests
    
    endpoint = "https://api.omniindex.xyz/api_v1/getblockschema" # set the api endpoint
    response = requests.get(endpoint, verify=True) # make a request to the endpoint
    
    assert response.status_code == 200 # assert that the response is successful