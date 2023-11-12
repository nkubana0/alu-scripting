#!/usr/bin/python3
"""
Script that queries the Reddit API,
parses the title of hot articles in a subreddit,
and prints a sorted count of given keywords.

"""

import requests

def count_words(subreddit, word_list, after=None, results=None):
    """
    Count occurrences of keywords in the titles of hot articles in a subreddit.

    """
    if results is None:
        results = {}

    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    params = {'limit': 10, 'after': after} if after else {'limit': 10}

    # Make a request to the Reddit API
    response = requests.get(url, params=params, headers={'User-Agent': 'YOUR_USER_AGENT'})

    # Check if the request was successful
    if response.status_code != 200:
        print(f"Error: HTTP Status Code {response.status_code}")
        return

    # Parse JSON response
    data = response.json()

    # Process the data if it has the expected structure
    if 'data' in data and 'children' in data['data']:
        for child in data['data']['children']:
            title_words = child['data']['title'].lower().split()

            for word in word_list:
                if word.lower() in title_words:
                    results[word.lower()] = results.get(word.lower(), 0) + title_words.count(word.lower())

        # Call the function recursively with the next set of hot articles
        count_words(subreddit, word_list, after=data['data'].get('after'), results=results)

    else:
        print("Error: Unexpected response format")

    if results:
        # Sort and print the results
        sorted_results = sorted(results.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_results:
            print(f"{word}: {count}")

# Example usage:
if __name__ == "__main__":
    subreddit_name = 'python'
    keywords = ['python', 'java', 'javascript']
    count_words(subreddit_name, keywords)
