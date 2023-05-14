import json
import requests
import os
import pandas as pd


# Load the environment variables from the .env file

# Get the value of the API_KEY environment variable
#api_key = os.environ.get('API_KEY')


def wipo_pearl_api(title):
    url = f'https://doaj.org/api/search/journals/patent'
    API_KEY = "734b9056f1904287bfab9ad38bffd2b2"

    headers = {
        'x-api-key':API_KEY
    }
    params = {

        'term': title,
        'sourceLanguages': 'EN',
        'targetLanguages': 'EN',
        'exactSearch': 'true',
        'count':1
    }

    response = requests.get(url, params=params,headers = headers)
    json_response = json.loads(response.text)
    records = json_response["Record"]
    

    return records







