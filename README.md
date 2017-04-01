[![Build Status](https://travis-ci.org/vincetse/t-service.svg?branch=master)](https://travis-ci.org/vincetse/t-service)

# T-Service

A pure-Python implementation of [RFC 2324](https://tools.ietf.org/html/rfc2324).

## Sample Deployment

This application can be accessed at https://t-service.herokuapp.com/.


## Usage

```
# Install Python dependencies
pip install -r requirements.txt

# Run tests
PYTHONPATH=. pytest

# Run app
FLASK_APP=t/__init__.py  flask run
```
