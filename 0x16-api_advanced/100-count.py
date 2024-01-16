#!/usr/bin/python3
"""Getting data using API"""
import requests
from collections import Counter


def count_words(subreddit, word_list, counts=None, after=None):
    if counts is None:
        counts = Counter()

    headers = {'User-Agent': 'my-app/0.0.1'}
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'

    if after:
        url += f'?after={after}'

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return

    data = response.json()
    for post in data['data']['children']:
        title = post['data']['title'].lower().split()
        counts.update(word for word in title if word in word_list)

    after = data['data']['after']
    if after is not None:
        count_words(subreddit, word_list, counts, after)
    else:
        sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_counts:
            print(f'{word}: {count}')
