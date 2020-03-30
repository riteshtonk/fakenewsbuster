#!/usr/bin/env python3

import twitter
import time

def __get_tweets(api=None, screen_name=None):
    timeline = api.GetUserTimeline(screen_name=screen_name, count=200)
    earliest_tweet = min(timeline, key=lambda x: x.id).id

    while True:
        tweets = api.GetUserTimeline(screen_name=screen_name, max_id=earliest_tweet, count=200)
        if not tweets:
            break
        new_earliest = min(tweets, key=lambda x: x.id).id

        if not tweets or new_earliest == earliest_tweet:
            break
        else:
            earliest_tweet = new_earliest
            timeline += tweets
            time.sleep(2)

    return timeline


def get_all_tweets(twitter_key, twitter_secret, token_key, token_secret, twitter_handle):
    api = twitter.Api(twitter_key, twitter_secret, token_key, token_secret)
    return __get_tweets(api, twitter_handle)
