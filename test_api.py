import os.path
from io import BytesIO

import pytest

import api


@pytest.fixture
def client():
    return api.app.test_client()


def _file_for_test_client(filename, directory_name='files'):
    with open(os.path.join(directory_name, filename), 'rb') as infile:
        contents = infile.read()
        _file = (BytesIO(contents), filename)
        return _file


@pytest.fixture
def data():
    return {
        'file': _file_for_test_client('budget.csv'),
        'schema': _file_for_test_client('table_schema.json'),
    }


def test_api_exists(client, data):
    resp = client.post('/', data=data)
    assert resp.status_code == 200
    assert resp.json


def test_errors_found(client, data):
    resp = client.post('/', data=data)
    assert resp.json['error-count'] == 4


def test_works_without_schema(client, data):
    data.pop('schema')
    resp = client.post('/', data=data)
    assert resp.json['error-count'] == 2
