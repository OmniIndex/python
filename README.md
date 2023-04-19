## Project description

# OmniIndex Python Library

The OmniIndex Python library provides convenient access to the OmniIndex API from applications written in the Python language. It includes a pre-defined set of classes for API resources that initialize themselves dynamically from API responses which makes it compatible with a wide range of versions of the OmniIndex API.

You can find usage examples for the OmniIndex Python library in our [Python Library reference](https://omniindex.readthedocs.io/) which includes code samples etc
For just the [API reference](https://app.swaggerhub.com/apis-docs/OmniIndexAPI/OmniIndex/1.0.0)

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

The library needs to be configured with your account's secret keys which are available from your account onboarding packet. Set them as the OMNIINDEX_API_PASSWORD environment variable before using the library:
We would recommed you set these for

* OMNIINDEX_API_PASSWORD
* OMNIINDEX_API_USER
* OMNIINDEX_API_NODE
* OMNIINDEX_API_TYPE
* OMNIINDEX_API_UNIT

Linux / bash etc

```bash
export OMNIINDEX_API_PASSWORD='sk-...'
```

Windows

```bash
setx OMNIINDEX_API_PASSWORD 'sk-...'
```
