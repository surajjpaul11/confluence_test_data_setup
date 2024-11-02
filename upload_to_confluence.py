import requests
from requests.auth import HTTPBasicAuth

# Replace with user details and Confluence instance URL
confluence_url = 'https://test.qnetconfluence.cms.gov/wiki/rest/api/content'
username = 'test.suraj.paul@mailinator.com'
api_token = 'oGHgvKfXffWXr4e8G3MSKvFOlROr02fVvvhF6w'
space_key = '~test-suraj-pau1'

# Basic page creation payload
page_data = {
    "type": "page",
    "title": "Sample Page Title",
    "space": {"key": space_key},
    "body": {
        "storage": {
            "value": "<p>This is a new page created via API.</p>",
            "representation": "storage"
        }
    }
}

# Make API request
response = requests.post(
    confluence_url,
    json=page_data,
    auth=HTTPBasicAuth(username, api_token),
    headers={"Content-Type": "application/json"}
)

# Check if the page was created successfully
if response.status_code == 200:
    print("Page created successfully:", response.json()['id'])
else:
    print("Failed to create page:", response.text)
