import json
from flask import Flask,jsonify
import pytest
import disk_api




@pytest.fixture               # setting up resources that are needed by the tests.
def client():                 # creating instance for testing
    app = disk_api.app
    app.testing = True
    client = app.test_client()
    yield client               # remembers the state

def test_func_get_name(client):
    result = client.get('/')
    assert result.status_code == 200   # Status 200 means successfully answered the requests.


def test_func_get_doj(client):
    result = client.get('/func_1')
    assert result.status_code == 200

def test_func_get_tree(client):
    result = client.get('/func_2')
    assert result.status_code == 200

#Test case: To check Key-value pair in result
def test_func_get_tree_two(client):
    result = client.get('/func_2')
    assert result.status_code == 200
    data =json.loads(result.data)
    print(type(data))
    for num, row in enumerate(data):
        assert row['id_1'] == num+1


#Test case: To check certain str is not present
def test_func_get_name_two(client):
    result = client.get('/').data
    print(type(result))
    # data = str(result)
    # print(type(data))
    assert b"A" in result
    assert b"B" in result
    assert b"C" in result
    assert b"D" in result
    assert b"E" in result
    assert b"Z" not in result



def test_func_get_name_m(client, monkeypatch):
    dummy_str = 'XYZ'
    monkeypatch.setattr('disk_api.get_info', lambda : dummy_str)
    result = client.get('/').data
    result = result.decode("utf-8")
    assert "X" in result
    assert "A" not in result







