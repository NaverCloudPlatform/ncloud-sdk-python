# ncloud-apikey

- API version: 2018-06-22T02:34:44Z
- Package version: 1.0.0

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com//.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com//.git`)

Then import the package:
```python
import ncloud_apikey
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import ncloud_apikey
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import ncloud_server
from ncloud_server.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_server.V2Api(ncloud_server.ApiClient(configuration))
add_nas_volume_access_control_request = ncloud_server.AddNasVolumeAccessControlRequest() # AddNasVolumeAccessControlRequest | addNasVolumeAccessControlRequest

try:
    api_response = api_instance.add_nas_volume_access_control(add_nas_volume_access_control_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->add_nas_volume_access_control: %s\n" % e)

```
