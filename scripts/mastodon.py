#!/usr/bin/env python3
"""
Fetch recent Mastodon statuses and generate sidebar HTML.
Run from repo root: python3 scripts/mastodon.py
"""

import requests, os, json
from bs4 import BeautifulSoup
from datetime import datetime

base_url = 'https://hachyderm.io/'
account_id = '109349626053208125'

OUTPUT_PATH = 'static/mastodonsidebar/index.html'

params = {'limit': 4}
response = requests.get(f'{base_url}/api/v1/accounts/{account_id}/statuses', params=params)

if response.status_code != 200:
    print(f'An error occurred: {response.text}')
    exit(1)

statuses = response.json()

with open(OUTPUT_PATH, 'w') as f:
    f.write('<link rel="stylesheet" href="/css/style.css">')

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

        # Truncate the text to under 250 char
        def truncate_text(text, max_length=250):
            soup = BeautifulSoup(text, 'html.parser')
            text_content = soup.get_text()
            if len(text_content) > max_length:
                return text_content[:max_length] + '...'
            else:
                return text_content

        content = truncate_text(text_content)

        # Get the date
        date_string = status['created_at']
        date = datetime.strptime(date_string, '%Y-%m-%dT%H:%M:%S.%fZ')
        formatted_date = date.strftime('%B %d %Y, %H:%M')

        if 'reblog' in status and status['reblog'] is not None:
            reblog_display_name = status['reblog']['account']['display_name']
            reblog_display_name_url = status['reblog']['account']['url']
            reblog_url = status['reblog']['url']

            soup = BeautifulSoup(status['reblog']['content'], 'html.parser')
            for span in soup.find_all('span', class_=['ellipsis', 'invisible']):
                span.replace_with(span.text)
            reblog_content = str(soup)

            f.write(f'<p>Boosted from: <a href="{reblog_display_name_url}" target="_blank">{reblog_display_name}</a><p class="post-meta">{formatted_date}</p><p>{reblog_content}</p><button type="button" class="btn btn-light"><a href="{reblog_url}" target="_blank">View on Mastodon</a></button></p></li>')
        else:
            f.write(f'<p>Published by: <a href="{display_name_url}" target="_blank">{display_name}</a></h5><p class="post-meta">{formatted_date}</p><p>{content}</p><button type="button" class="btn btn-light"><a href="{url}" target="_blank">View on Mastodon</a></button></p></li>')

print(f'Mastodon sidebar written to {OUTPUT_PATH}')
