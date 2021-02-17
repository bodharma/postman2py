# postman2py

postman2py is a library for [Postman](https://www.getpostman.com/) that run Postman's collections. 

Originaly was forked from https://github.com/k3rn3l-p4n1c/postpython and https://github.com/matkapi/postpy2
Added few updates related to Postman collection import and urlencoded request type.

## Why use postman2py instead of postman codegen?

- No hardcoded variables
- If your team use postman collection for testing and you want to extend testing by integrating some calculation or etc.


## How to install?

postman2py is available on [PyPI](https://pypi.python.org/pypi?name=postman2py&version=0.0.1&:action=display)
and you can install it using pip:

```bash
$ pip install postman2py
```

## How to use?

Import `postman2py`

```$python
from postman2py.core import PostPython

runner = postman2py('/path/to/collection/postman_collection.json')

# runner.default.<request_name> # if no folders in collection
# runner.<folder_name>.<request_name> # if folders exist in collection

response = runner.default.get_request()
print(response.json())
print(response.status_code)
```

### Load enviroment variables

In postman2py you can load enviroment variables from postman enviroment files

```$python
pp.environments.load('environments/postman_environment.json')
```

### Set environment variable

```$python
runner.environments.update({'BASE_URL': 'http://127.0.0.1:5000'})
runner.environments.update({'PASSWORD': 'test', 'EMAIL': 'you@email.com'})
```

### AttributeError

postman2py try to correct your mistake if you spell a function or folder wrong it will suggest you the closest name.

```$python
>>> response = runner.RequestMethods.get_requasts()

Traceback (most recent call last):
File "test.py", line 11, in <module>
response = runner.RequestMethods.get_requasts()
File "/usr/local/lib/python3.5/site-packages/postman2py/core.py", line 73, in **getattr**
'Did you mean %s' % (item, self.name, similar))

AttributeError: get_requasts request does not exist in RequestMethods folder.
Did you mean get_request

```

You can also use `help()` method to print all available requests.

```$python

>>> runner.help()
>>> Posible requests:
>>> runner.AuthOthers.hawk_auth()
>>> runner.AuthOthers.basic_auth()
>>> runner.AuthOthers.oauth1_0_verify_signature()
>>> runner.RequestMethods.get_request()
>>> runner.RequestMethods.put_request()
>>> runner.RequestMethods.delete_request()
>>> runner.RequestMethods.post_request()
>>> runner.RequestMethods.patch_request()

or

>>> runner.RequestMethods.help()
>>> runner.RequestMethods.delete_request()
>>> runner.RequestMethods.patch_request()
>>> runner.RequestMethods.get_request()
>>> runner.RequestMethods.put_request()
>>> runner.RequestMethods.post_request()

```

