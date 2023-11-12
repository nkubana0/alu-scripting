#!/usr/bin/python3
"""
function that queries the Reddit API
parses the title of all hot articles
prints a sorted count of given keywords
"""

import json
import requests
import sys


import requests

def count_words(subreddit, word_list, counts=None, after=None):
    """
    Count occurrences of keywords in the titles of hot articles in a subreddit.

    """
    if counts is None:
        counts = {}

    url = "https://www.reddit.com/r/{}/hot.json?limit=100".format(subreddit)
    headers = {'User-agent': 'myRedditScript/1.0'}
    params = {'after': after} if after else {}

    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        if 'data' in data and 'children' in data['data']:
            new_posts = data['data']['children']

            for post in new_posts:
                title = post['data']['title']
                for word in word_list:
                    count = title.lower().count(word.lower())
                    counts[word.lower()] += count

            after = data['data']['after']
            if after:
                return count_words(subreddit, word_list, counts, after)
            else:
                sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
                for word, count in sorted_counts:
                    if count > 0:
                        print(f"{word}: {count}")
        else:
            print("No posts found")
    else:
        print("Invalid subreddit or no posts match")

if __name__ == '__main__':
    import sys
    if len(sys.argv) < 3:
        print("Usage: {} <subreddit> <list of keywords>".format(sys.argv[0]))
        print("Ex: {} programming 'python java javascript'".format(sys.argv[0]))
    else:
        count_words(sys.argv[1], [x.lower() for x in sys.argv[2].split()])
