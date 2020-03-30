import feed_interface
import re
from db_interface import InMemoryDBInterface

class FactCheckIndiaTwitterFeedHandler(feed_interface.FeedInterface):
    def __init__(self, api, dbinterface):
        self.api = api
        self.dbinterface = dbinterface
        self.pattern = re.compile("Claim:(.*.\n)Fact:([^.]*)")

    def start(self):
        tweets = self.api.get_all_tweets('FactCheckIndia')
        for tweet in tweets:
            tweet_text = tweet._json["full_text"]
            if "Claim:" in tweet_text and "Fact:" in tweet_text:
                match = self.pattern.search(tweet_text)
                if match != None and len(match.group()) >= 2:
                    source = "https://twitter.com/{0}/status/{1}".format(tweet._json["user"]["screen_name"], tweet._json["id_str"])
                    self.dbinterface.write(match.group(1), match.group(2), source)


                    
            


