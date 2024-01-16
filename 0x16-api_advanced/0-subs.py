#!/usr/bin/python3
"""Getting data using API"""
import requests


def number_of_subscribers(subreddit):
    """Returning the number of subsribers"""
    headers = {"User-Agent": "MyCustomUserAgent/1.0"}
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(url, allow_redirects=False, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return data["data"]["subscribers"]
    else:
        return 0
