import json
import os
import random
import string
from datetime import datetime
import pytest
from app import api
from app.models.user import UserModel


@pytest.fixture()
def client():
    with api.app.test_client() as client:
        yield client


def test_user(client):
    uname = randomString(10)

    ret = client.post('/user', data=dict(
        username=uname,
        password="12345",
        first_name="Sadegh",
        last_name="Azarkaman",
        phone_number="12345",
        birth_date=datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
    ))
    user_id = json.loads(ret.get_data(as_text=True))["user_id"]

    assert int(user_id) > 0

    ret = client.put('/user/{}'.format(user_id), data=dict(
        first_name=uname,
        last_name="Azarkaman",
        phone_number="Pass123",
        birth_date=datetime.now().strftime('%Y-%m-%dT%H:%M:%S'),
    ))
    assert ret.status_code == 204
    name = UserModel.find_by_id(user_id).firstName
    assert name == uname
    ret = client.delete('/user/{}'.format(user_id))
    assert ret.status_code is 202


def randomString(stringLength=10):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))
