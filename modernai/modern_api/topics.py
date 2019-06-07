#!/usr/bin/env python
from flask import abort, jsonify
from flask_restful import Resource, reqparse, marshal_with, fields
from ..modern_api import api
from ..models.topics import Topics
from ..models.user import User
from ..extensions import db, scrape_crawl, text_process

topic_parser = reqparse.RequestParser()
topic_parser.add_argument('username', required=True)
topic_parser.add_argument('api_key', required=True)
topic_parser.add_argument('title', type=str, required=True)
topic_parser.add_argument('type', type=str, required=True)
topic_parser.add_argument('url', type=str, required=True)
topic_parser.add_argument('description', type=str)

load_topics = reqparse.RequestParser()
load_topics.add_argument('username', required=True)
load_topics.add_argument('api_key')
load_topics.add_argument('title')

topic_collection = reqparse.RequestParser()
topic_collection.add_argument('username', required=True)
topic_collection.add_argument('api_key')

text_topics = reqparse.RequestParser()
text_topics.add_argument('username', required=True)
text_topics.add_argument('api_key')
text_topics.add_argument('title')
text_topics.add_argument('text')


class AddTopicsFromWebCrawl(Resource):

    def post(self):
        args = topic_parser.parse_args()
        # Pass url here for a scrape and crawl
        topic_test = None
        user = User.query.filter_by(username=args['username']).first()
        if user.api_key == args['api_key']:
            topic_test = Topics.query.filter_by(url=args['url']).first()
        else:
            abort(404)

        if topic_test is None:
            scrape_crawl.url = args['url']
            x = scrape_crawl.topic_crawl()
            for d in x[0]:
                for topic in d.items():
                    new_topic = Topics(
                        user_id=user.id,
                        api_key=args['api_key'],
                        title=args['title'],
                        type=args['type'],
                        description=args['description'],
                        url=args['url'],
                        topic=topic[0],
                        occurrence=topic[1]
                        #sentiment='',
                        #polaritity=''
                    )
                    db.session.add(new_topic)
                   
                db.session.commit()

            response = {'response': 'topic corpus added.'}
        else:
            response = {'response': 'topic corpus already exists.'}

        return jsonify(response)


class AddTopicsFromUrl(Resource):

    def post(self):
        args = topic_parser.parse_args()
        # Pass url here for a scrape and crawl
        user = User.query.filter_by(username=args['username']).first()
        if user.api_key == args['api_key']:
            topic_test = Topics.query.filter_by(url=args['url']).first()
            if topic_test is None:
                scrape_crawl.url = args['url']
                text = scrape_crawl.page_scrape()
                topics = scrape_crawl.parse_topics(text)
                for topic in topics.items():
                    new_topic = Topics(
                        user_id=user.id,
                        api_key=args['api_key'],
                        title=args['title'],
                        type=args['type'],
                        description=args['description'],
                        url=args['url'],
                        topic=topic[0],
                        occurrence=topic[1],
                        # sentiment='',
                        # polaritity=''
                    )
                    db.session.add(new_topic)
                db.session.commit()
                response = {'response': 'new topics added.'}
            else:
                response = {'response': 'corpus already exists.'}
        else:
            response = {'response': 'user not authorized.'}
        return jsonify(response)


class TopicResource(Resource):

    def get(self):
        args = load_topics.parse_args()
        user = User.query.filter_by(username=args['username']).first()
        if user.api_key == args['api_key']:
            topic = Topics.query.filter_by(title=args['title']).first()
            if not topic:
                abort(404)
            return topic
        else:
            abort(404)

    def delete(self):
        topic = Topics.delete(**load_topics.parse_args())
        if not topic:
            abort(404)
        return 204


class TopicCollection(Resource):

    def get(self):
        args = topic_collection.parse_args()
        user = User.query.filter_by(username=args['username']).first()
        if user.api_key == args['api_key']:
            data = Topics.query_filter_by(username=args['username'])
            if not data:
                abort(404)
            return data
        else:
            abort(404)


class ExtractTopicsFromTxt(Resource):

    def post(self):
        args = text_topics.parse_args()
        # Pass url here for a scrape and crawl
        user = User.query.filter_by(username=args['username']).first()
        if user.api_key == args['api_key']:
            text_process.load_sequence(args['text'])
            topics = text_process.rank_words_phrases()
            return {'response': topics}
        else:
            abort(404)

api.add_resource(AddTopicsFromWebCrawl, '/topics/seed/add')
api.add_resource(AddTopicsFromUrl, '/topics/url/add')
api.add_resource(TopicResource, '/topics/<topic>', '/topics/<int:topic_id>')
api.add_resource(TopicCollection, '/topics/list')
api.add_resource(ExtractTopicsFromTxt, '/topics/extract_from_text')

