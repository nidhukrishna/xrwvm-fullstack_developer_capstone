# Uncomment the imports below before you add the function code
import requests
import os
from dotenv import load_dotenv

load_dotenv()

backend_url = os.getenv(
    'backend_url', default="http://localhost:3030")
sentiment_analyzer_url = os.getenv(
    'sentiment_analyzer_url',
    default="http://localhost:5050/")

def get_request(endpoint, **kwargs):
    params = ""
    if kwargs:
        for key, value in kwargs.items():
            params += f"{key}={value}&"
        params = "?" + params.rstrip("&")  # Add ? only if there are params

    request_url = backend_url + endpoint + params

    print("GET from", request_url)
    try:
        response = requests.get(request_url)
        return response.json()
    except Exception as e:
        print("Network exception occurred:", e)
        return None


def analyze_review_sentiments(text):
    request_url = sentiment_analyzer_url+"analyze/"+text
    try:
        # Call get method of requests library with URL and parameters
        response = requests.get(request_url)
        return response.json()
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")
        print("Network exception occurred")
# def post_review(data_dict):
def post_review(url, json_payload, **kwargs):
    try:
        response = requests.post(url, json=json_payload, headers={'Content-Type': 'application/json'}, **kwargs)
        return response
    except Exception as e:
        return f"Error: {str(e)}"

# Add code for posting review
