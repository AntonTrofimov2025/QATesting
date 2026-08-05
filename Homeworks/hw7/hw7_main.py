import pytest
from Homeworks.hw7.hw7_main_api import HW7Api

@pytest.fixture()
def my_api():
    return HW7Api(base_url='http://restful-booker.herokuapp.com')

def test_auth(my_api):
    token = my_api.get_token()
    assert token is not None
    print(f'\nToken: {token}')

def test_create(my_api):
    created = my_api.create_booking()
    assert 'firstname' in created['booking']
    assert 'lastname' in created['booking']
    print(created)

def test_create_negative_scenario(my_api):
    is_created = my_api.try_create_with_bad_body()
    print(is_created)

def test_update_company(my_api):
    created = my_api.create_booking()
    assert created['booking']['firstname'] == 'Jim'
    assert created['booking']['lastname'] == 'Brown'
    print(created)
    updated = my_api.update_booking(created, {"firstname" : "Ivan", "lastname" : "Green",}, 'patch')
    assert updated['firstname'] == 'Ivan'
    assert updated['lastname'] == 'Green'
    print(updated)

