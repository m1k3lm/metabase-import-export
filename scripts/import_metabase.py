import requests
import json
import os

METABASE_HOST = os.getenv('METABASE_HOST')
METABASE_USERNAME = os.getenv('METABASE_USERNAME')
METABASE_PASSWORD = os.getenv('METABASE_PASSWORD')

def authenticate():
    response = requests.post(f'{METABASE_HOST}/api/session', json={
        'username': METABASE_USERNAME,
        'password': METABASE_PASSWORD
    })
    response.raise_for_status()
    return response.json()['id']

def import_metabase_content():
    session_id = authenticate()
    headers = {
        'Content-Type': 'application/json',
        'X-Metabase-Session': session_id
    }

    # Read from file
    with open('metabase_export.json', 'r') as f:
        data = json.load(f)

    # Import questions
    for question in data['questions']:
        response = requests.post(f'{METABASE_HOST}/api/card', headers=headers, json=question)
        response.raise_for_status()

    # Import dashboards
    for dashboard in data['dashboards']:
        response = requests.post(f'{METABASE_HOST}/api/dashboard', headers=headers, json=dashboard)
        response.raise_for_status()

    # Import queries
    for query in data['queries']:
        response = requests.post(f'{METABASE_HOST}/api/native-query', headers=headers, json=query)
        response.raise_for_status()

if __name__ == '__main__':
    import_metabase_content()
