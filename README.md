[![Build Status](https://github.com/vincetse/t-service/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/vincetse/t-service/actions/workflows/ci.yml)
[![Maintainability](https://qlty.sh/gh/vincetse/projects/t-service/maintainability.svg)](https://qlty.sh/gh/vincetse/projects/t-service)
[![Coverage Status](https://coveralls.io/repos/github/vincetse/t-service/badge.svg?branch=main)](https://coveralls.io/github/vincetse/t-service?branch=main)
[![Code Coverage](https://qlty.sh/gh/vincetse/projects/t-service/coverage.svg)](https://qlty.sh/gh/vincetse/projects/t-service)

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
