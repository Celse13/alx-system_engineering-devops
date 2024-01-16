#!/usr/bin/python3
"""Getting data using API"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """recurse"""
    headers = {'User-Agent': 'my-app/0.0.1'}
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'

    if after:
        url += f'?after={after}'

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return None

    data = response.json()
    hot_list += [post['data']['title'] for post in data['data']['children']]

    after = data['data']['after']
    if after is not None:
        return recurse(subreddit, hot_list, after)

    return hot_list
