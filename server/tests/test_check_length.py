from random import choice
from string import ascii_uppercase
import protocol

import pytest
from datetime import datetime
from protocol import make_response

CODE = 200
ACTION = 'test'
TIME = datetime.now().timestamp()
DATA = 'some client data'

REQUEST = {
    'action': ACTION,
    'time': TIME,
    'data': 'some client data'
}

LENGTH = {
    'action': 15,
    'code': 3,
    'time': 0,
    'data': 500
}

max_len_action = 30
# len_code = 3
max_len_data = 1024

codes = [100, 101, 200, 201, 202, 400, 401, 402, 403, 404, 409, 410, 500]
test_codes = [0, 100, 101, 200, 201, 202, 400, 401, 402, 403, 404, 409, 410, 500, 700]

@pytest.fixture
def len_action():
    return

@pytest.fixture
def len_data():
    return

@pytest.fixture
def code_id():
    return

@pytest.mark.randomize(len_action=int, min_num=1, max_num=max_len_action, ncalls=99)
def test_length_action_make_response(len_action):
    action = ''.join(choice(ascii_uppercase) for i in range(len_action))
    REQUEST['action'] = action
    response = make_response(REQUEST, CODE, DATA, date=TIME)
    action_crop = response.get('action')
    assert len(action_crop) <= max_len_action


@pytest.mark.randomize(len_data=int, min_num=1, max_num=max_len_data, ncalls=99)
def test_length_data_make_response(len_data):
    data = ''.join(choice(ascii_uppercase) for i in range(len_data))
    response = make_response(REQUEST, CODE, data, date=TIME)
    data_crop = response.get('data')
    assert len(data_crop) <= max_len_data


@pytest.mark.randomize(code_id=int, min_num=0, max_num=len(test_codes)-1, ncalls=10)
def test_length_code_make_response(code_id):
    code = test_codes[code_id]
    response = make_response(REQUEST, code, DATA, date=TIME)
    code_crop = response.get('code')
    assert code_crop in codes

