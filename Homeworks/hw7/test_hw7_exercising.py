import pytest
from Homeworks.hw7.myhw7_api import MyHW7_Api

# base_url = 'http://5.101.50.27:8000'
#
#
# payload = {
#          "username": "harrypotter",
#          "password": "expelliarmus"
#           }

# import requests
# def test_auth():
#     response = requests.post(f'{base_url}/auth/login', json=payload)
#     # print(response.json())
#     print(f'\nToken: {response.json()["user_token"]}')
#     assert response.json()['role'] == 'admin'
#     assert response.json()['display_name'] == 'harrypotter'


@pytest.fixture()
def my_api():
    return MyHW7_Api()

def test_auth_v2(my_api):
    token = my_api.get_token()
    assert token is not None
    print(f'\nToken: {token}')

def test_create_company(my_api):
    created = my_api.create_company()
    assert created['name'] == 'ITCH'
    assert created['description'] == 'курсы'
    print()
    print(created)

def test_get_company(my_api):
    created = my_api.create_company()
    get_this_company = my_api.get_company(created)
    assert get_this_company['name'] == 'ITCH'
    assert get_this_company['description'] == 'курсы'

def test_delete_company(my_api):
    created = my_api.create_company()
    company_id = created['id']
    response = my_api.delete_company(created)
    assert response['detail'] == "Компания успешно удалена"
    assert response['company_id'] == company_id
    print()
    print(response)

##############################################
# def test_delete_unnecessary_residuals(my_api):
#     list_of_ids = [82, 81, 84, 85]
#     for company_id in list_of_ids:
#         my_api.delete_company(company_id)
##############################################

def test_get_all_companies(my_api):
    response = my_api.get_all_companies()
    print()
    print(response)
    print(len(response))

def test_first_company(my_api):
    response = my_api.get_all_companies()
    first_company = response[0]
    assert first_company['name'] == "QA Студия 'ТестировщикЪ'"

def test_active_companies(my_api):
    response = my_api.get_all_companies()
    print()
    print(len(response))
    response = [company for company in my_api.get_all_companies() if company['is_active']]
    print(len(response))
    assert len(response) >= 4

