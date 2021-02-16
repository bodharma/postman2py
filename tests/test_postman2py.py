from postman2py.core import PostPython
import pytest
import json
import os



def test_import_folder_collection():
    pp = PostPython(f'{os.path.abspath(os.curdir)}/collections/tests.postman_collection.json')
    pp.environments.load(f'{os.path.abspath(os.curdir)}/environments/test.postman_environment.json')

    pp.environments.update({
        'server_url': 'https://httpbin.org'
    })

    response = pp.Folder.test1_simple_get()
    assert response.status_code == 200

def test_import_request():
    pp = PostPython(f'{os.path.abspath(os.curdir)}/collections/tests.postman_collection.json', no_folder=True)
    pp.environments.load(f'{os.path.abspath(os.curdir)}/environments/test.postman_environment.json')

    pp.environments.update({
        'server_url': 'https://httpbin.org'
    })

    response = pp.default.test_no_folder()
    assert response.status_code == 200

def test_raw_post():
    pp = PostPython(f'{os.path.abspath(os.curdir)}/collections/tests.postman_collection.json')
    pp.environments.load(f'{os.path.abspath(os.curdir)}/environments/test.postman_environment.json')

    pp.environments.update({
        'server_url': 'https://httpbin.org'
    })

    response = pp.Folder.test2_post_raw()
    assert response.status_code == 200


def test_post_form_with_file():
    pp = PostPython(f'{os.path.abspath(os.curdir)}/collections/tests.postman_collection.json')
    pp.environments.load(f'{os.path.abspath(os.curdir)}/environments/test.postman_environment.json')

    pp.environments.update({
        'server_url': 'https://httpbin.org'
    })

    response = pp.Folder.test_post_form_data_with_file()
    assert response.status_code == 200
