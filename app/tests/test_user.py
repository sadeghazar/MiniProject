import json
import os
import random
import string
from datetime import datetime
import pytest
from app import api
from models.user import UserModel


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
    # user_id = json.loads(ret.get_data(as_text=True))["user_id"]
    # print(user_id)
    # ret = client.get("/user/{}".format(user.id))
    #
    # assert int(user_id) > 0
    #
    # print('/user/{}'.format(user_id))
    # ret = client.put('/user/{}'.format(user_id), data=dict(
    #     first_name=rname,
    #     last_name="Azarkaman",
    #     phone_number="Pass123",
    #     birth_date=datetime.now().strftime('%Y-%m-%dT%H:%M:%S'),
    # ))
    # assert ret.status_code == 204
    # ret = client.get("/user/MAzarkamanTest")
    # name = json.loads(ret.get_data(as_text=True))["first_name"]
    # assert name == rname
    # userid = json.loads(ret.get_data(as_text=True))["id"]
    # ret = client.delete('/user/{}'.format(userid))
    # assert ret.status_code is 202


def randomString(stringLength=10):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))
