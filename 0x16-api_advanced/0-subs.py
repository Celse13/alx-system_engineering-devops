#!/usr/bin/python3
"""Getting data using API"""
import requests


def number_of_subscribers(subreddit):
    """Returning the number of subsribers"""
    headers = {'User-Agent': 'my-app/0.0.1'}
    response = requests.get(f'https://www.reddit.com/r/{subreddit}/about.json',
                            headers=headers,
                            allow_redirects=False)

    if response.status_code == 404:
        return 0
    if 'error' in response.json():
        return 0
    return response.json()['data']['subscribers']
