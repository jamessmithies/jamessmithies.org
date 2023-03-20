import requests
from bs4 import BeautifulSoup
from datetime import datetime

from settings.secrets import *

headers = {'Authorization': f'Bearer {access_token}'}
params = {'limit': 5}
response = requests.get(f'{base_url}/api/v1/accounts/{account_id}/statuses', headers=headers, params=params)

if response.status_code == 200:
    statuses = response.json()
    for status in statuses:
        print(f'Successfully retrieved status update')
else:
    print(f'An error occurred: {response.text}')

with open('templates/blog/mastodon_sidebar.html', 'w') as f:
    # Add a reference to the Bootstrap stylesheet
    f.write('<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.0.0/dist/css/bootstrap.min.css">')
    
    for status in statuses:
        display_name = status['account']['display_name']
        display_name_url = status['account']['url']
        url = status['url']
        
        # Parse the content HTML with BeautifulSoup
        soup = BeautifulSoup(status['content'], 'html.parser')
        
        # Find and remove all span elements with class ellipsis or invisible
        for span in soup.find_all('span', class_=['ellipsis', 'invisible']):
            span.replace_with(span.text)
        
        # Get the modified content as a string
        content = str(soup)

        # Get the date of the status update
        date = status['created_at']

        date_string = status['created_at']
        date = datetime.strptime(date_string, '%Y-%m-%dT%H:%M:%S.%fZ')
        formatted_date = date.strftime('%B %d %Y, %H:%M')
        
        # Add a class to the div element for styling with Bootstrap
        f.write('<div class="toot card mb-3">')
        
        if 'reblog' in status and status['reblog'] is not None:
            reblog_display_name = status['reblog']['account']['display_name']
            reblog_display_name_url = status['reblog']['account']['url']
            reblog_url = status['reblog']['url']
            
            # Parse the Posted content HTML with BeautifulSoup
            soup = BeautifulSoup(status['reblog']['content'], 'html.parser')
            
            # Find and remove all span elements with class ellipsis or invisible
            for span in soup.find_all('span', class_=['ellipsis', 'invisible']):
                span.replace_with(span.text)
            
            # Get the modified Posted content as a string
            reblog_content = str(soup)
            
            f.write(f'<div class="card-body"><h5 class="card-title">Boosted from: <a href="{reblog_display_name_url}">{reblog_display_name}</a></h5><p class="card-text">{formatted_date}</p><p class="card-text">{reblog_content}</p><a href="{reblog_url}" class="btn btn-primary">View original</a></div>')
        else:
            f.write(f'<div class="card-body"><h5 class="card-title">Published by: <a href="{display_name_url}">{display_name}</a></h5><p class="card-text">{formatted_date}</p><p class="card-text">{content}</p><a href="{url}" class="btn btn-primary">View on Mastodon</a></div>')
            
        f.write('</div>')