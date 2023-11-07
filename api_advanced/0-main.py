#!/usr/bin/python3
"""
This script is a command-line utility to retrieve the number of subscribers for a subreddit from the Reddit API.

Usage:
    python3 reddit_subscribers.py <subreddit_name>

Arguments:
    <subreddit_name> - The name of the subreddit for which you want to retrieve the number of subscribers.

Example:
    python3 reddit_subscribers.py programming

Note:
    - Make sure you have the '0-subs' module available, which should contain the 'number_of_subscribers' function.
    - You need to pass the name of the subreddit as a command-line argument.

Author: Your Name

"""

import sys

if __name__ == '__main__':
    number_of_subscribers = __import__('0-subs').number_of_subscribers
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        print("{:d}".format(number_of_subscribers(sys.argv[1]))) 

