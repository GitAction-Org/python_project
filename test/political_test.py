def test_get_home_invalid_route(mocker):
    mocker.patch('requests.get')
    requests.get.return_value.status_code = 404

    response = requests.get(API_URL_HOME)
    assert response.status_code == 404

def test_get_sports_invalid_route(mocker):
    mocker.patch('requests.get')
    requests.get.return_value.status_code = 404

    response = requests.get(API_URL_SPORTS)
    assert response.status_code == 404

def test_get_political_invalid_route(mocker):
    mocker.patch('requests.get')
    requests.get.return_value.status_code = 404

    response = requests.get(API_URL_POLITICAL)
    assert response.status_code == 404

def test_get_home_empty_response(mocker):
    mocker.patch('requests.get')
    requests.get.return_value.status_code = 200
    requests.get.return_value.json.return_value = {}

    response = requests.get(API_URL_HOME)
    assert response.status_code == 200
    assert not response.json()

def test_get_sports_empty_response(mocker):
    mocker.patch('requests.get')
    requests.get.return_value.status_code = 200
    requests.get.return_value.json.return_value = {}

    response = requests.get(API_URL_SPORTS)
    assert response.status_code == 200
    assert not response.json()

def test_get_political_empty_response(mocker):
    mocker.patch('requests.get')
    requests.get.return_value.status_code = 200
    requests.get.return_value.json.return_value = {}

    response = requests.get(API_URL_POLITICAL)
    assert response.status_code == 200
    assert not response.json()

def test_get_home_invalid_method(mocker):
    mocker.patch('requests.post')
    requests.post.return_value.status_code = 405

    response = requests.post(API_URL_HOME)
    assert response.status_code == 405

def test_get_sports_invalid_method(mocker):
    mocker.patch('requests.post')
    requests.post.return_value.status_code = 405

    response = requests.post(API_URL_SPORTS)
    assert response.status_code == 405

def test_get_political_invalid_method(mocker):
    mocker.patch('requests.post')
    requests.post.return_value.status_code = 405

    response = requests.post(API_URL_POLITICAL)
    assert response.status_code == 405

def test_get_home_valid_data(mocker):
    mocker.patch('requests.get')
    requests.get.return_value.status_code = 200
    requests.get.return_value.json.return_value = {"data": "mocked_response"}

    response = requests.get(API_URL_HOME)
    assert response.status_code == 200
    assert response.json() is not None