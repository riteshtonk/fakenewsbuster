#!/usr/bin/env python3

from flask import abort, jsonify, request, Flask

api = Flask(__name__)

@api.route('/message', methods=['POST'])
def post_message():
    if not request.json:
        abort(400)
    print(request.json)
    return jsonify({}), 201

if __name__ == '__main__':
    api.run()