#!/usr/bin/python3
"""
Module
"""

import json
import requests
import sys


def top_ten(subreddit):
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {'User-agent': 'myRedditScript/1.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        if 'data' in data and 'children' in data['data']:
            top_posts = [post['data']['title']
                         for post in data['data']['children']]
            for post_title in top_posts:
                print(post_title)
        else:
            print("No posts found")
    else:
        print("None")


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        top_ten(sys.argv[1])
