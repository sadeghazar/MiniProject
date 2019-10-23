import os
from datetime import datetime
import pytest
from app import api
import pdb


@pytest.fixture()
def client():
    with api.app.test_client() as client:
        yield client


def test_user_get(client):
    ret = client.get("/user/1")
    assert ret.status_code is 200


def test_create_user(client):
    ret = client.post('/user', data=dict(
        first_name="Sadegh",
        last_name="Azarkaman",
        phone_number="Pass123",
        birth_date=datetime.now().strftime('%Y-%m-%dT%H:%M:%S'),
    ))

    assert ret.status_code is 201


def test_update_user(client):
    ret = client.put('/user/1', data=dict(
        first_name="Sadegh",
        last_name="Azarkaman",
        phone_number="Pass123",
        birth_date=datetime.now().strftime('%Y-%m-%dT%H:%M:%S'),
    ))

    assert ret.status_code is 204


def test_delete_user(client):
    ret = client.delete('/user/1')
    assert ret.status_code is 202
