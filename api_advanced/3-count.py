#!/usr/bin/python3
"""
function that queries the Reddit API
parses the title of all hot articles
prints a sorted count of given keywords
"""
import requests


def count_words(subreddit, word_list):
    """
    Module
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'myRedditScript/1.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:

        return None
    posts = response.json().get('data').get('children')
    word_count = {}
    for post in posts:
        title = post['data']['title']
        for word in word_list:
            if word.lower() in title.lower():
                word_count[word.lower()] = word_count.get(word.lower(), 0) + 1

    if not word_count:
        return
    for key, value in sorted(word_count.items(), key=lambda x: (-x[1], x[0])):
        print("{}: {}".format(key.lower(), value))
    return count_words(subreddit, word_list)
