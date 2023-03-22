import requests
import json

# Constants
_API_KEY = None
_SERVER = None

# Functions

def api_key(api_key):
    global _API_KEY
    _API_KEY = api_key

def server(server_name):
    global _SERVER
    _SERVER = server_name

def unit_name(unit_name):
    global _UNIT_NAME
    _UNIT_NAME = unit_name

def get_block_schematic(unitName, Type, user)):
    url = "https://api.omniindex.xyz/api_v1/getblockschematic"

    payload = json.dumps({
        "unitName": _UNIT_NAME,
        "server": _SERVER,
        "Type": Type,
        "user": user,
        "password": _API_KEY
    })
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    return response.text

