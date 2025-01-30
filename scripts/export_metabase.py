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

def export_metabase_content():
    session_id = authenticate()
    headers = {
        'Content-Type': 'application/json',
        'X-Metabase-Session': session_id
    }

    # Export questions
    questions_response = requests.get(f'{METABASE_HOST}/api/card', headers=headers)
    questions_response.raise_for_status()
    questions = questions_response.json()

    # Export dashboards
    dashboards_response = requests.get(f'{METABASE_HOST}/api/dashboard', headers=headers)
    dashboards_response.raise_for_status()
    dashboards = dashboards_response.json()

    # Export queries
    queries_response = requests.get(f'{METABASE_HOST}/api/native-query', headers=headers)
    queries_response.raise_for_status()
    queries = queries_response.json()

    # Save to file
    with open('metabase_export.json', 'w') as f:
        json.dump({
            'questions': questions,
            'dashboards': dashboards,
            'queries': queries
        }, f, indent=4)

if __name__ == '__main__':
    export_metabase_content()
