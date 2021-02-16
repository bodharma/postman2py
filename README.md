# postman2py

postman2py is a library for [Postman](https://www.getpostman.com/) that run Postman's collections. Originaly was forked from https://github.com/k3rn3l-p4n1c/postpython and updated to Postman collection v2.1 format.
If you are using postman, but collection runner is not flexible enough for you and postman codegen is too boring,
postman2py is here for your continuous integration.

## Why use postman2py instead of postman codegen?

- Postman codegen should be applied one by one for each request and it's boring when your API changes,
  but with Postpy2, you don't need to generate code.
  Just export collection with Postman and use it with Postpy2.
- In code generation, you don't have environment feature anymore and variables are hard coded.

## Why user postman2py instead of Postman collection runner?

- With postman2py, you write your own script. But collection runner just turns all your requests one by one.
  So with postman2py, you can design more complex test suites.

## How to install?

postman2py is available on [PyPI](https://pypi.python.org/pypi?name=postman2py&version=0.0.1&:action=display)
and you can install it using pip:

```bash
$ pip install postpy3
```

## How to use?

Import `postman2py`

```$python
from postpy3.core import PostPython
```

Make an instance from `postman2py` and give the address of postman collection file.

```$python
runner = postman2py('/path/to/collection/Postman echo.postman_collection')
```

Now you can call your request. Folders' name change to upper camel case and requests' name change to lowercase form.
In this example the name of folder is "Request Methods" and it's change to `RequestMethods` and the name of request was
"GET Request" and it's change to `get_request`. So you should call a function like `runner.YourFolderName.you_request_name()`

```$python
response = runner.RequestMethods.get_request()
print(response.json())
print(response.status_code)
```

### Load enviroment variables

In postman2py you can load enviromental variables from postman enviroment files

```$python
pp.environments.load('environments/test.postman_environment.json')
```

### Variable assignment

In postman2py you can assign values to environment variables in runtime.

```$python
runner.environments.update({'BASE_URL': 'http://127.0.0.1:5000'})
runner.environments.update({'PASSWORD': 'test', 'EMAIL': 'you@email.com'})
```

### AttributeError

Since `RequestMethods` and `get_request` does not really exists your intelligent IDE cannot help you.
So postman2py tries to correct your mistakes. If you spell a function or folder wrong it will suggest you the closest name.

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
>>> ...

>>> runner.RequestMethods.help()
>>> runner.RequestMethods.delete_request()
>>> runner.RequestMethods.patch_request()
>>> runner.RequestMethods.get_request()
>>> runner.RequestMethods.put_request()
>>> runner.RequestMethods.post_request()

```

