Introduction
============

Welcome to the `OmniIndex Python API` library documentation! This library provides a simple and easy-to-use Python interface for interacting with the OmniIndex API. With `omniindex`, you can quickly retrieve block schematics and perform various tasks related to the OmniIndex blockchain.
With the OmniIndex suite of tools, data is protected with our patented 360° encryption, stored in hybrid-blockchains, and then made usable in your favorite collaboration, productivity, and analytics tools with no risk of exposure. Our patented FHE (Fully Homomorphic Encryption) means search and analytics can happen on the data while it is encrypted, and there is tiered access using two encryption keys with configurable access rights. 
In other words: **Your data is secure and private at all times**


Getting Started
---------------

To use the library, start by importing the `OmniIndexClient` and `os` class:
**assumes you have already set an environmental variable for your API key using your os.** If you have not, you can set it using the following command: 

For Linux and Mac OS

.. code-block:: bash 

   export OMNIINDEX_API_KEY=your_api_key

For Windows

.. code-block:: doscon

   setx OMNIINDEX_API_KEY your_api_key

Usage

.. code-block:: python

   import os 
   from omniindex import OmniIndexClient

Next, create an instance of the `OmniIndexClient` class with your API credentials and desired parameters: We strongly recommend you *never* use typed strings for your API credentials. Instead, use environment variables to store your API credentials and retrieve them using the `os` class.
Refer to your OmniIndex API credentials for the following parameters which are required to create an instance of the `OmniIndexClient` class:

.. code-block:: python

   your_api_key = os.environ.get("OMNIINDEX_API_KEY")

   client = OmniIndexClient(
       server="https://omniindex.node", # the OmniIndex API blockchain node
       api_key="your_api_key", # your OmniIndex API key
       unit_name="your_unit_name", # your unit name 
       block_type="your_block_type", # your block type 
       user="your_user" # your user 
   )

For more information on the available classes, methods, and their usage, refer For more information on the client object and elements refer to the `OmniIndex Documentation <https://omniindex.io/docs/>`_..