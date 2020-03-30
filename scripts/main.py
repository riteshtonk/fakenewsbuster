#!/usr/bin/env python3

import twitter_reader
import json

#screen_name='FactCheckIndia'
#screen_name = 'AltNews'
#screen_name = 'QuintFactCheck'
#screen_name = 'boomlive_in'

TWITTER_KEY = 'WnxqjzhCNxm1wqWW5zn1DgfH2'
TWITTER_SECRET = 'vx74JYRbNB4r6j8txNq2iU1U21hegF8sQTONngtHWvHhoug5Kw'
TOKEN_KEY = '17892401-yVDs3opMMA4DSXXFTWEfwg5Ngv6cp6ZAaMYgZpd1j'
TOKEN_SECRET = 'KOfYnPlULd0c1Bh5LKK3rmoWReHWUYP0kqPxnHeWtfoX4'

if __name__ == "__main__":
    tweets = twitter_reader.get_all_tweets(TWITTER_KEY, TWITTER_SECRET, TOKEN_KEY, TOKEN_SECRET, 'FactCheckIndia')
    for tweet in tweets:
        print tweet._json["text"]
    