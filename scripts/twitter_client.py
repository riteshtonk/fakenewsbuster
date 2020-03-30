#!/usr/bin/env python3

import twitter
import time

class TwitterClient:
    def __init__(self, twitter_key, twitter_secret, token_key, token_secret):
        self.api = twitter.Api(twitter_key, twitter_secret, token_key, token_secret, tweet_mode='extended')

    def get_all_tweets(self, screen_name):
        timeline = self.api.GetUserTimeline(screen_name=screen_name, count=200)
        earliest_tweet = min(timeline, key=lambda x: x.id).id

        while True:
            tweets = self.api.GetUserTimeline(screen_name=screen_name, max_id=earliest_tweet, count=200)
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