## Project description
# OmniIndex Python Library

The OmniIndex Python library provides convenient access to the OmniIndex API from applications written in the Python language. It includes a pre-defined set of classes for API resources that initialize themselves dynamically from API responses which makes it compatible with a wide range of versions of the OmniIndex API.

You can find usage examples for the OmniIndex Python library in our [API reference](https://something) and the [OmniIndex Cookbook](https://www.omniindex.io)

## Installation
You don't need this source code unless you want to modify the package. If you just want to use the package, just run:
```bash
pip install --upgrade omniindex
```
Install from source with:
```bash
pip setup.py install
```
## Usage
The library needs to be configured with your account's secret keys which are available from your account website. Either set them as the OMNIINDEX_API_PASSWORD environment variable before using the library:

```bash
export OMNIINDEX_API_PASSWORD='sk-...'
```
It is also useful to set a few other variables that will be used with the API
- server
- unitname
- user
- type
Should all be set

```python
import omniindex as oi
oi.api_key = "sk-..."

# add a server
oi.server = "https://node1..."

# add unitname
oi.unit_name = 

# create a completion
completion = openai.Completion.create(model="ada", prompt="Hello world")

# print the completion
print(completion.choices[0].text)

