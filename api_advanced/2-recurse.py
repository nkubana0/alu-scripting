#!/usr/bin/python3
"""
Script that queries the reddit API
returns a list containing the titles of all hot articles for a given subreddit
"""

import json
import requests
import sys


def recurse(subreddit, hot_list=None, after=None):
    if hot_list is None:
        hot_list = []

    url = "https://www.reddit.com/r/{}/hot.json?limit=100".format(subreddit)
    headers = {"User-agent": "myRedditScript/1.0"}
    params = {'after': after} if after else {}

    response = requests.get(url, headers=headers,
                            params=params, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        if 'data' in data and 'children' in data['data']:
            new_posts = data['data']['children']
            hot_list.extend([post['data']['title'] for post in new_posts])

            after = data['data']['after']
            if after:
                return recurse(subreddit, hot_list, after)
            else:
                return hot_list
        else:
            return None

    else:
        return None


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please pass an argument")
    else:
        result = recurse(sys.argv[1])
        if result is not None:
            print(len(result))
        else:
            print("None")
