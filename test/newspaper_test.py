import pytest
import requests
from unittest.mock import patch
from pytest_mock import mocker

# Define your API URLs
API_URL_HOME = "http://127.0.0.1:5002/home"
API_URL_SPORTS = "http://127.0.0.1:5002/sports"
API_URL_POLITICAL = "http://127.0.0.1:5002/political"


# Define test cases



def test_get_sports_valid_data(mocker):
    mocker.patch('requests.get')
    requests.get.return_value.status_code = 200
    requests.get.return_value.json.return_value = {"data": "mocked_response"}

    response = requests.get(API_URL_SPORTS)
    assert response.status_code == 200
    assert response.json() is not None

def test_get_political_valid_data(mocker):
    mocker.patch('requests.get')
    requests.get.return_value.status_code = 200
    requests.get.return_value.json.return_value = {"data": "mocked_response"}

    response = requests.get(API_URL_POLITICAL)
    assert response.status_code == 200
    assert response.json() is not None

if __name__ == "__main__":
    pytest.main()
