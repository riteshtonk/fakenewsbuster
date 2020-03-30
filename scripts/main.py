#!/usr/bin/env python3

from twitter_client import TwitterClient
from FactCheckIndia_twitter_feed_handler import FactCheckIndiaTwitterFeedHandler
from db_interface import InMemoryDBInterface
<<<<<<< HEAD
=======
from flask import abort, jsonify, request, Flask
>>>>>>> 412b9fd... Added handler for FactCheckIndia and an in memory store to save results
import json
import spacy

TWITTER_KEY = ''
TWITTER_SECRET = ''
TOKEN_KEY = '-'
TOKEN_SECRET = ''

inmem_db = InMemoryDBInterface()
api = Flask(__name__)
nlp = spacy.load('en_core_web_md')

def validate(message):
    claim_tokens = list()
    words = message.split()
    for word in words:
        if len(word) > 3:
            claim_tokens.append(word)
    claim_tokens.sort()
    print(claim_tokens)
    " ".join(claim_tokens)
    needle = nlp(" ".join(claim_tokens))
    for item in inmem_db.get_items():
        print(item.claim_tokens)
        hay = nlp(" ".join(item.claim_tokens))
        if needle.similarity(hay) > 0.90:
            return '{"result": "' + item.claim_result + '" "source":"' + item.source_url + '"}'
    return '{"result": "Unknown" "source":"www.google.com"}'

@api.route('/message', methods=['POST'])
def post_message():
    print(request)
    if not request.json:
        abort(400)
    return validate(request.json["message"]), 201

if __name__ == "__main__":
    # Initialize feed handlers to popuate the DB
    twitter_client = TwitterClient(TWITTER_KEY, TWITTER_SECRET, TOKEN_KEY, TOKEN_SECRET)
    source1 = FactCheckIndiaTwitterFeedHandler(twitter_client, inmem_db)
    source1.start()

    # Start the web
    api.run()