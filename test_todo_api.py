import pytest
import requests
from pytest_bdd import scenario, given, then, parsers
import pandas as pd

@pytest.fixture()
def test_data():
    df = pd.read_excel("D:\PythonBDDTest.xlsx")
    return df.to_dict('records')

@pytest.fixture()
def make_get_request():
    def _make_get_request(UserId, PostId, CommentDesc, URL, Sentiment, endpoint):
        full_url = f"http://3.27.18.54/index.php/{endpoint}"
        response = requests.get(full_url)
        return response
    return _make_get_request

@given(parsers.parse('I make a GET request with user "{UserId}", post "{PostId}", comment "{CommentDesc}", URL "{URL}", sentiment "{Sentiment}", and endpoint "{endpoint}"'))
def make_request(make_get_request, UserId, PostId, CommentDesc, URL, Sentiment, endpoint):
    response = make_get_request(UserId, PostId, CommentDesc, URL, Sentiment, endpoint)
    return response

@then('the response status code should be 200')
def check_status_code(make_request):
    assert make_request.status_code == 200

@scenario('test_api_endpoints.feature', 'Test API endpoints with different user actions')
def test_api_endpoints():
    pass
