from pytest_bdd import given, when, then
import requests

@given('I make a GET request with user "{UserId}", post "{PostId}", comment "{CommentDesc}", URL "{URL}", sentiment "{Sentiment}", and endpoint "{endpoint}"')
def step_make_get_request(request, UserId, PostId, CommentDesc, URL, Sentiment, endpoint):
    full_url = f"http://3.27.18.54/index.php/{endpoint}"
    response = requests.get(full_url)
    return response