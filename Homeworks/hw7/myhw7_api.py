import requests


class MyHW7Api:

    class Params:
        USERNAME = "harrypotter"
        PASSWORD = "expelliarmus"

    def __init__(self):
        self.base_url = 'http://5.101.50.27:8000'

    def __get_login_pswd(self):
        return {"username": self.Params.USERNAME, "password": self.Params.PASSWORD}

    @staticmethod
    def __get_company_data():
        return {"name": "ITCH", "description": "курсы"}

    def get_token(self):
        response = requests.post(f'{self.base_url}/auth/login', json=self.__get_login_pswd())
        assert response.status_code == 200, f'Invalid code, expected: 200, actual: {response.status_code}'
        return response.json()['user_token']

    def create_company(self):
        created = requests.post(f'{self.base_url}/company/create', json=self.__get_company_data())
        assert created.status_code == 201, f'Invalid code, expected: 201, actual: {created.status_code}'
        return created.json()

    def try_create_with_empty_body(self):
        created = requests.post(f'{self.base_url}/company/create', json={})
        assert created.status_code == 422, f'Invalid code, expected: 422, actual: {created.status_code}'
        return created.json()

    def get_company(self, your_company: dict):
        company_id = your_company['id']
        response = requests.get(f'{self.base_url}/company/{company_id}')
        assert response.status_code == 200, f'Invalid code, expected: 200, actual: {response.status_code}'
        return response.json()

    def delete_company(self, your_company: dict | int):
        if isinstance(your_company, dict):
            company_id = your_company['id']
        elif isinstance(your_company, int):
            company_id = your_company
        else:
            raise ValueError('Only dict structure or str are allowed!')
        response = requests.delete(f'{self.base_url}/company/{company_id}?client_token={self.get_token()}')
        assert response.status_code == 200, f'Invalid code, expected: 200, actual: {response.status_code}'
        return response.json()

    def get_all_companies(self):
        response = requests.get(f'{self.base_url}/company/list')
        assert response.status_code == 200, f'Invalid code, expected: 200, actual: {response.status_code}'
        assert response.headers["Content-Type"] == "application/json"
        return response.json()

