#!/usr/bin/env python3

from twitter_client import TwitterClient
from FactCheckIndia_twitter_feed_handler import FactCheckIndiaTwitterFeedHandler
from db_interface import InMemoryDBInterface
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
    inmem_db = InMemoryDBInterface()
    twitter_client = TwitterClient(TWITTER_KEY, TWITTER_SECRET, TOKEN_KEY, TOKEN_SECRET)
    source1 = FactCheckIndiaTwitterFeedHandler(twitter_client, inmem_db)
    source1.start()
    