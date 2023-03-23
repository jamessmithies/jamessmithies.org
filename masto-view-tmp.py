from django.shortcuts import render
import requests
from bs4 import BeautifulSoup

def mastodon(request):
    base_url = 'https://hachyderm.io/'
    access_token = 'MGNDL9BVcuZrlxC0-z4E4wZPbQirb7scdz6GY4T-KlM'
    account_id = '109349626053208125'

    headers = {'Authorization': f'Bearer {access_token}'}
    params = {'limit': 5}
    response = requests.get(f'{base_url}/api/v1/accounts/{account_id}/statuses', headers=headers, params=params)

    context = {
        'statuses': []
    }

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

        context['statuses'].append({
            'display_name': display_name,
            'display_name_url': display_name_url,
            'url': url,
            'content': content,
            })

    return render(request, 'blog/mastodon_sidebar.html', context)