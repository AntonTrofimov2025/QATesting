import requests


class MyHW7Api:

    class Params:
        USERNAME = "harrypotter"
        PASSWORD = "expelliarmus"

    def __init__(self, base_url):
        self.base_url = base_url

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
        if not isinstance(your_company, dict):
            raise TypeError('Only dict structure is allowed!')
        company_id = your_company['id']
        response = requests.get(f'{self.base_url}/company/{company_id}')
        assert response.status_code in [200, 404], f'Invalid code, expected: 200 or 404, actual: {response.status_code}'
        return response.json()

    def delete_company(self, your_company: dict | int):
        if isinstance(your_company, dict):
            company_id = your_company['id']
        elif isinstance(your_company, int):
            company_id = your_company
        else:
            raise TypeError('Only dict structure or int are allowed!')
        response = requests.delete(f'{self.base_url}/company/{company_id}?client_token={self.get_token()}')
        assert response.status_code == 200, f'Invalid code, expected: 200, actual: {response.status_code}'
        return response.json()

    def update_company(self, your_company: dict, new_data: dict, method: str='patch'):
        if not isinstance(your_company, dict) or not isinstance(new_data, dict):
            raise TypeError('Only dict structure is allowed!')
        if method not in ['put', 'patch']:
            raise ValueError('Only put and patch methods are allowed!')
        company_id = your_company['id']
        url_with_token = f'{self.base_url}/company/update/{company_id}?client_token={self.get_token()}'
        response = requests.put(url_with_token, json=new_data) if method == 'put'\
            else requests.patch(url_with_token, json=new_data)
        assert response.status_code == 202, f'Invalid code, expected: 202, actual: {response.status_code}'
        return response.json()

    def update_status(self, your_company: dict, activation: bool=True):
        if not isinstance(your_company, dict) or not isinstance(activation, bool):
            raise TypeError('Only bool and dict structure is allowed!')
        company_id = your_company['id']
        url_with_token = f'{self.base_url}/company/status_update/{company_id}?client_token={self.get_token()}'
        response = requests.patch(url_with_token, json={'is_active': activation})
        assert response.status_code == 202, f'Invalid code, expected: 202, actual: {response.status_code}'
        return response.json()

    def get_all_companies(self):
        response = requests.get(f'{self.base_url}/company/list')
        assert response.status_code == 200, f'Invalid code, expected: 200, actual: {response.status_code}'
        assert response.headers["Content-Type"] == "application/json"
        return response.json()


