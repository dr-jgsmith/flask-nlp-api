#!/usr/bin/env python
from flask import abort, jsonify
from flask_restful import Resource, reqparse, marshal_with, fields
from ..modern_api import api
from ..models.user import User
from ..nlp.sentiment import sentiment_blob
from ..nlp.topics import get_topics


sent_data = reqparse.RequestParser()
sent_data.add_argument('username')
sent_data.add_argument('api_key')
sent_data.add_argument('text')


class GetSentimentFromText(Resource):

    def get(self):
        args = sent_data.parse_args()
        data = None
        user = User.query.filter_by(username=args['username']).first()
        if user.api_key == args['api_key']:
            topics = get_topics(args['text'])
            sentiment = sentiment_blob(args['text'])
            data = {
                'response': {
                    'topics': topics,
                    'sentiment': sentiment
                }
            }

        else:
            abort(404)
        return data


api.add_resource(GetSentimentFromText, '/sentiment/text/raw')