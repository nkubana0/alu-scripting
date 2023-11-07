#!/usr/bin/python3
"""
This script defines a function to retrieve the number of subscribers for a subreddit from the Reddit API.
It also provides a command-line interface for using this function.

Author: Your Name

Usage:
    python3 reddit_subscribers.py <subreddit_name>

Arguments:
    <subreddit_name> - The name of the subreddit for which you want to retrieve the number of subscribers.

Example:
    python3 reddit_subscribers.py programming

Dependencies:
    - You need the 'requests' module installed to make HTTP requests. You can install it using 'pip install requests'.

Note:
    - Make sure you have the 'requests' module installed.
    - You need to pass the name of the subreddit as a command-line argument.

"""

import sys
import requests

def number_of_subscribers(subreddit):
    """
    Retrieve the number of subscribers for a subreddit from the Reddit API.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: The number of subscribers for the given subreddit, or 0 if the subreddit does not exist.

    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "MyRedditBot/1.0 (by YourUsername)"}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        subscribers = data["data"]["subscribers"]
        return subscribers
    else:
        return 0

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit = sys.argv[1]
        num_subscribers = number_of_subscribers(subreddit)
        print(num_subscribers)
