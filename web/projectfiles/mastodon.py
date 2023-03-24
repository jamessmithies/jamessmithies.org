import requests, re
from bs4 import BeautifulSoup
from datetime import datetime

base_url = 'https://hachyderm.io/'
account_id = '109349626053208125'

params = {'limit': 4}
response = requests.get(f'{base_url}/api/v1/accounts/{account_id}/statuses', params=params)

if response.status_code == 200:
    statuses = response.json()
    for status in statuses:
        print(f'Successfully retrieved status update')
else:
    print(f'An error occurred: {response.text}')

with open('templates/blog/mastodon_sidebar.html', 'w') as f:
    # Add a reference to the stylesheet
    f.write('<link rel="stylesheet" href="https://jsorg-docker-static.s3.amazonaws.com/static/shared/css/style.css">')
    
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
        text_content = str(soup)

        def truncate_text(text, max_length=250):
            soup = BeautifulSoup(text, 'html.parser')
            text_content = soup.get_text()
            if len(text_content) > max_length:
                return text_content[:max_length] + '...'
            else:
                return text_content
            
        # Get the modified content as a string
        content = truncate_text(text_content)

        # Get the date of the status update
        date = status['created_at']

        date_string = status['created_at']
        date = datetime.strptime(date_string, '%Y-%m-%dT%H:%M:%S.%fZ')
        formatted_date = date.strftime('%B %d %Y, %H:%M')
        
        # Add a class to the div element for styling 
        f.write('<ul class="list-unstyled main-menu">')
        
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
            
            f.write(f'<li>Boosted from: <a href="{reblog_display_name_url}">{reblog_display_name}</a><p class="post-meta">{formatted_date}</p><p>{reblog_content}</p><button type="button" class="btn btn-light"><a href="{reblog_url}">View original</a></button></p></li>')
        else:
            f.write(f'<li>Published by: <a href="{display_name_url}">{display_name}</a></h5><p class="post-meta">{formatted_date}</p><p>{content}</p><button type="button" class="btn btn-light"><a href="{url}">View on Mastodon</a></button></p></li>')
            
        f.write('</ul>')