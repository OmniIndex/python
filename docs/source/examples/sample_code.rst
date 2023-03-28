Sample code
===========

*all these examples use the demonstration API key, which is limited to 100 requests per day.*
If you want to use the API for a project, please contact us at `developer help <mailto:devs@omniindex.io>`_ to get a production API key.

the demonstration uses the Enron email dataset, which is available at `https://www.cs.cmu.edu/~enron/ <https://www.cs.cmu.edu/~enron/>`_ which has been preprocessed and indexed by OmniIndex. The dataset is licensed under the `Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License <https://creativecommons.org/licenses/by-nc-sa/3.0/>`_.

Set up the OmniIndex API client
-------------------------------

- before we dive into the code, firstly, set up your python virtual environment and install the `omniindex` package:

.. code-block:: bash

   python3 -m venv venv
   source venv/bin/activate
   pip install --upgrade omniindex

- to your environment variables, add the api_key you received from OmniIndex.

.. code-block:: bash

   export OMNIINDEX_API_KEY=your_api_key 

- in this example we are using our demonstration api_key = **NTAzMjcxMjA5NzM1NjYyMg==**

.. code-block:: python

   import omniindex as oi
   import os
   import json

   api_key = os.environ['OMNIINDEX_API_KEY']
   client = oi.OmniIndexClient(server="https://node1.omniindex.xyz/node",unit_name="enronemail",api_key=api_key, block_type="Owner", user="enronemail")
   

We can test this by fetching the block schema:

get_block_schematic
-------------------

Now you can use the `get_block_schematic` method to fetch block schematics from the OmniIndex API:

.. code-block:: python

   block_schematic = client.get_block_schematic()
   data = json.loads(block_schematic)
   print(data)

You will now have a JSON output of the block schematic:

.. code-block:: bash

   {'0': {'column_name': 'bodyowners', 'data_type': 'text'}, '1': {'column_name': 'bodysearchableowners', 'data_type': 'text'}, '2': {'column_name': 'contentsearchableowners', 'data_type': 'text'}, '3': {'column_name': 'context', 'data_type': 'text'}, '4': {'column_name': 'context2', 'data_type': 'text'}, '5': {'column_name': 'folder', 'data_type': 'text'}, '6': {'column_name': 'fromowners', 'data_type': 'text'}, '7': {'column_name': 'fromsearchableowners', 'data_type': 'text'}, '8': {'column_name': 'hash', 'data_type': 'character varying'}, '9': {'column_name': 'message_id', 'data_type': 'text'}, '10': {'column_name': 'oidxid', 'data_type': 'integer'}, '11': {'column_name': 'prevhash', 'data_type': 'character varying'}, '12': {'column_name': 'priorhash', 'data_type': 'text'}, '13': {'column_name': 'recieveddate', 'data_type': 'timestamp without time zone'}, '14': {'column_name': 'sentiment', 'data_type': 'text'}, '15': {'column_name': 'sentiment2', 'data_type': 'text'}, '16': {'column_name': 'subject', 'data_type': 'text'}, '17': {'column_name': 'toowners', 'data_type': 'text'}, '18': {'column_name': 'tosearchableowners', 'data_type': 'text'}}

Tests
=====

API endpoint tests
------------------

- to run the tests, first install the `pytest` package:

.. code-block:: bash

   pip install pytest   

- then run the tests:

.. code-block:: python

   def test_ssl_api_endpoint():
    # import the requests library
    import requests
    
    endpoint = "https://api.omniindex.xyz/api_v1" # set the api endpoint
    response = requests.get(endpoint, verify=True) # make a request to the endpoint
    
    assert response.status_code == 200 # assert that the response is successful
