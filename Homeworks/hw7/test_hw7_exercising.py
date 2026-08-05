import pytest
from Homeworks.hw7.myhw7_api import MyHW7Api

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
    return MyHW7Api(base_url='http://5.101.50.27:8000')

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
    assert get_this_company['name'] == 'ITCH' and get_this_company['name'] == created['name']
    assert get_this_company['description'] == 'курсы' and get_this_company['description'] == created['description']

def test_delete_company(my_api):
    created = my_api.create_company()
    company_id = created['id']
    companies_before = list(my_api.get_all_companies())
    response = my_api.delete_company(created)
    companies_after = list(my_api.get_all_companies())
    assert len(companies_after) == len(companies_before) - 1
    assert response['detail'] == "Компания успешно удалена"
    assert response['company_id'] == company_id
    deleted = my_api.get_company(created)
    assert deleted['detail'] == 'Компания не найдена'
    print()
    print(response)

def test_put_company(my_api):
    created = my_api.create_company()
    print(created)
    new_data ={'name': 'HELLO', 'description': 'курсы UPDATED', 'is_active': False}
    updated = my_api.update_company(created, new_data, 'patch')
    print(updated)
    assert 'HELLO' in updated['name']
    assert 'курсы UPDATED' in updated['description']

def test_company_status(my_api):
    created = my_api.create_company()
    print(f"Active?: {created['is_active']}")
    my_api.update_status(created, False)
    updated = my_api.get_company(created)
    print(f"Active?: {updated['is_active']}")

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

def test_try_create_company_empty_body(my_api):
    response = my_api.try_create_with_empty_body()
    assert response['detail'][0]['msg'] == 'Field required'
    print()
    print(response)

def test_creation(my_api):
    before_creation = my_api.get_all_companies()
    print(len(before_creation))
    my_api.create_company()
    after_creation = my_api.get_all_companies()
    print(len(after_creation))
    assert len(after_creation) == len(before_creation) + 1

