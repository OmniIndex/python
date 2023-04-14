import json
from omniindex.api import OmniIndexClient
import os
import time

# define constants

NODE = os.environ['OI_API_TEST_NODE'] # https://node1.omniindex.xyz/node
USER_KEY = os.environ['OI_API_TEST_USER_KEY']
USER_DEMO_KEY = os.environ['OI_API_TEST_DEMO_KEY']
USER_DEMO = os.environ['OI_API_TEST_USER_DEMO']
UNIT_DEMO = os.environ['OI_API_TEST_UNIT_DEMO']
USER_DOC = os.environ['OI_API_TEST_USER_DOC'] # 'demonstration'
USER_DOC_UNIT = os.environ['OI_API_TEST_USER_DOC_UNIT'] # 'demonstration'
USER_DOC_KEY = os.environ['OI_API_TEST_USER_DOC_KEY']
QUERY = "working with google workspace"
REDACT = "Data has been redacted"
# add constant for data added to the block as now
DATE_ADDED = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())

"""
To run these tests
------------------

.. code-block:: bash

    $ python -m pytest tests/

"""

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

def test_get_block_schematic_returns_json_string():
    """Test that the get_block_schematic() method returns a valid JSON string."""
    client = OmniIndexClient(NODE, USER_KEY, 'enronemail', 'Owner', 'enronemail')
    json_string = client.get_block_schematic()
    assert type(json_string) == str
    assert json.loads(json_string) is not None
    assert json.loads(json_string) != {}

def test_json_string_contains_column_string():
    """Test that the get_block_schematic() method returns a valid JSON string containing the string 'column_name'."""
    client = OmniIndexClient(NODE, USER_KEY, 'enronemail', 'Owner', 'enronemail')
    json_string = client.get_block_schematic()
    json_data = json.loads(json_string)
    assert "column_name" in json.dumps(json_data)

def test_get_folders_true_returns_json_string():
    """Test that the get_block_schematic() method returns a valid JSON string when showProtected is set to true."""
    client = OmniIndexClient(NODE, USER_DEMO_KEY, UNIT_DEMO, 'Owner', USER_DEMO)
    json_string = client.get_folders("true")
    assert type(json_string) == str
    assert json.loads(json_string) is not None
    assert json.loads(json_string) != {}

def test_get_folders_false_returns_json_string():
    """Test that the get_block_schematic() method returns a valid JSON string when showProtected is set to false"""
    client = OmniIndexClient(NODE, USER_DEMO_KEY, UNIT_DEMO, 'Owner', USER_DEMO)    
    json_string = client.get_folders("false")
    assert type(json_string) == str
    assert json.loads(json_string) is not None
    assert json.loads(json_string) != {}
    json_data = json.loads(json_string)
    assert "Data has been redacted" in json.dumps(json_data) # check that the data has been redacted

def test_get_searchchain_returns_json_string():
    """Test that the get_search_results() method returns a valid JSON string."""
    client = OmniIndexClient(NODE, USER_DOC_KEY, USER_DOC, 'Owner', USER_DOC_UNIT)
    json_string = client.get_searchchain("true", QUERY , "fulltext")
    assert type(json_string) == str
    assert json.loads(json_string) is not None
    assert json.loads(json_string) != {}
    
def test_get_searchchain_returns_query_with_sentiment():
    """Test that the get_search_results() method returns a valid JSON string containing the query."""
    client = OmniIndexClient(NODE, USER_DOC_KEY, USER_DOC_UNIT, 'Owner',USER_DOC)
    json_string = client.get_searchchain("true", QUERY, "fulltext")
    json_data = json.loads(json_string)
    assert "sentiment" in json.dumps(json_data) # check that the sentiment is in the response

def test_get_searchchain_returns_query_with_redaction():
    """Test that the get_search_results() method returns a valid JSON string containing the query."""
    client = OmniIndexClient(NODE, USER_DOC_KEY, USER_DOC_UNIT, 'Owner',USER_DOC)
    json_string = client.get_searchchain("false", QUERY, "fulltext")
    json_data = json.loads(json_string)
    assert REDACT in json.dumps(json_data) # check that the data has been redacted   

def test_get_searchchain_returns_query_with_files_only():
    """Test that the get_search_results() method returns a valid JSON string containing the query."""
    client = OmniIndexClient(NODE, USER_DOC_KEY, USER_DOC_UNIT, 'Owner',USER_DOC)
    json_string = client.get_searchchain("false", "Simon Bain", "files")
    json_data = json.loads(json_string)
    assert "CA110460FC7B856AF8A445868E25CFD1E07029B79A65B14043C2E186BDA6D0F6" in json.dumps(json_data) # check that the data has been redacted

def test_getfiles_returns_query_with_context():
    """Test that the get_search_results() method returns a valid JSON string containing the query."""
    client = OmniIndexClient(NODE, USER_DOC_KEY, USER_DOC_UNIT, 'Owner',USER_DOC)
    json_string = client.getfiles("true", "Demo_Docs" )
    json_data = json.loads(json_string)
    assert "Happy" in json.dumps(json_data) # check that the sentiment is in the response

def test_getfiles_returns_query_with_redaction():
    """Test that the get_search_results() method returns a valid JSON string containing the query."""
    client = OmniIndexClient(NODE, USER_DOC_KEY, USER_DOC_UNIT, 'Owner',USER_DOC)
    json_string = client.getfiles("false", "Demo_Docs" )
    json_data = json.loads(json_string)
    assert REDACT in json.dumps(json_data) # check that the data has been redacted

def test_run_analytic_query_returns_query():
    """Test that the get_search_results() method returns a valid JSON string containing the query."""
    client = OmniIndexClient(NODE, USER_KEY, 'enronemail', 'Owner', 'enronemail')
    json_string = client.run_analytic_query("true", "SELECT * FROM WHERE contentsearchableowners LIKE '%{enron}%' LIMIT 10 ")
    json_data = json.loads(json_string)
    assert "enron" in json.dumps(json_data) # check that the sentiment is in the response

def test_run_analytic_query_with_redaction():
    """Test that the get_search_results() method returns a redacted, valid JSON string containing the query."""
    client = OmniIndexClient(NODE, USER_KEY, 'enronemail', 'Owner', 'enronemail')
    json_string = client.run_analytic_query("false", "SELECT * FROM WHERE contentsearchableowners LIKE '%{enron}%' LIMIT 10 ")
    json_data = json.loads(json_string)
    assert REDACT in json.dumps(json_data) # check that the data has been redacted


def test_minedata_date_valid():
    """Test that the post_minedata() method has a valid date string"""
    
    assert "2023" in DATE_ADDED # check that the date includes current year
