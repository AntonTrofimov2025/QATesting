import requests


class HW7Api:

    class Params:
        USERNAME = "admin"
        PASSWORD = "password123"
        BOOKING_DATA = {
                        "firstname" : "Jim",
                        "lastname" : "Brown",
                        "totalprice" : 111,
                        "depositpaid" : True,
                        "bookingdates" : {
                            "checkin" : "2018-01-01",
                            "checkout" : "2019-01-01"
                        },
                        "additionalneeds" : "Breakfast"
                       }
        BAD_PAYLOAD = {
                        "firstname": None,
                        "lastname": None,
                        "totalprice": None,
                        "depositpaid": None,
                        "bookingdates": {
                            "checkin": None,
                            "checkout": None
                        }
                      }

    def __init__(self, base_url):
        self.base_url = base_url

    def __get_login_pswd(self):
        return {"username": self.Params.USERNAME, "password": self.Params.PASSWORD}

    def get_token(self):
        response = requests.post(f'{self.base_url}/auth', json=self.__get_login_pswd())
        assert response.status_code == 200, f'Invalid code, expected: 200, actual: {response.status_code}'
        return response.json()['token']

    def create_booking(self):
        created = requests.post(f'{self.base_url}/booking', json=self.Params.BOOKING_DATA)
        assert created.status_code == 200, f'Invalid code, expected: 200, actual: {created.status_code}'
        return created.json()

    def try_create_with_bad_body(self):
        created = requests.post(f'{self.base_url}/booking', json=self.Params.BAD_PAYLOAD)
        assert created.status_code == 500, f'Invalid code, expected: 500, actual: {created.status_code}'
        return created.text

    def update_booking(self, your_booking: dict, new_data: dict, method: str='patch'):
        if not isinstance(your_booking, dict) or not isinstance(new_data, dict):
            raise TypeError('Only dict structure is allowed!')
        if method not in ['put', 'patch']:
            raise ValueError('Only put and patch methods are allowed!')
        booking_id = your_booking['bookingid']
        url_with_token = f'{self.base_url}/booking/{booking_id}'
        headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Cookie': f"token={self.get_token()}"}
        response = requests.put(url_with_token, json=new_data, headers=headers) if method == 'put'\
            else requests.patch(url_with_token, json=new_data, headers=headers)
        assert response.status_code == 200, f'Invalid code, expected: 200, actual: {response.status_code}'
        return response.json()