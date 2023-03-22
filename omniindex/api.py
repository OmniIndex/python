import requests
import json

def get_block_schematic(unitName, server, Type, user, password):
    url = "https://api.omniindex.xyz/api_v1/getblockschematic"

    payload = json.dumps({
        "unitName": unitName,
        "server": server,
        "Type": Type,
        "user": user,
        "password": password
    })
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    return response.text

