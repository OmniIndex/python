import pytest
import requests
import json
from omniindex.api import OmniIndexClient

import pytest

def test_get_block_schematic_returns_json_string():
    """Test that the get_block_schematic() method returns a valid JSON string."""
    client = OmniIndexClient('https://node1.omniindex.xyz/node', 'NTAzMjcxMjA5NzM1NjYyMg==', 'enronemail', 'Owner', 'enronemail')
    json_string = client.get_block_schematic()
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
