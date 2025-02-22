import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

METABASE_PORT = os.getenv('METABASE_PORT')
METABASE_HOST = 'http://127.0.0.1:' + METABASE_PORT
METABASE_API_KEY = os.getenv('METABASE_API_KEY')

def export_metabase_content():
    headers = {
        'Content-Type': 'application/json',
        'x-api-key': METABASE_API_KEY
    }

    # # Export questions
    # questions_response = requests.get(f'{METABASE_HOST}/api/card', headers=headers)
    # questions_response.raise_for_status()
    # questions = questions_response.json()
    # # Save to file
    # with open('metabase_export_questions.json', 'w') as f:
    #     json.dump({
    #         'questions': questions
    #     }, f, indent=4)
        
    # # Export dashboards
    # dashboards_response = requests.get(f'{METABASE_HOST}/api/dashboard', headers=headers)
    # dashboards_response.raise_for_status()
    # dashboards = dashboards_response.json()
    # # Save to file
    # with open('metabase_export_dashboards.json', 'w') as f:
    #     json.dump({
    #         'dashboards': questions
    #     }, f, indent=4)

    # Export queries
    queries_response = requests.get(f'{METABASE_HOST}/api/native-query-snippet', headers=headers)
    queries_response.raise_for_status()
    queries = queries_response.json()
    # Save to file
    with open('metabase_export_query_snippets.json', 'w') as f:
        json.dump({
            'queries': queries
        }, f, indent=4)

if __name__ == '__main__':
    export_metabase_content()
