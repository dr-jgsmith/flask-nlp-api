#!/usr/bin/env python
from flask import abort, jsonify
from flask_restful import Resource, reqparse, marshal_with, fields
from ..config import UPLOAD_FOLDER
from ..modern_api import api
from ..models.corpus import Corpus
from ..models.user import User
from ..extensions import db, scrape_crawl

corpus_parser = reqparse.RequestParser()
corpus_parser.add_argument('username', required=True)
corpus_parser.add_argument('api_key', required=True)
corpus_parser.add_argument('title', type=str, required=True)
corpus_parser.add_argument('type', type=str, required=True)
corpus_parser.add_argument('seed_url', type=str, required=True)
corpus_parser.add_argument('description', type=str)
corpus_parser.add_argument('corpus_file', type=str, required=True)
corpus_parser.add_argument('model_file', type=str, required=True)

load_corpus = reqparse.RequestParser()
load_corpus.add_argument('api_key')
load_corpus.add_argument('title')

corpus_collection = reqparse.RequestParser()
corpus_collection.add_argument('username', required=True)
corpus_collection.add_argument('api_key')


class AddCorpusFromUrl(Resource):

    def post(self):
        args = corpus_parser.parse_args()
        # Pass url here for a scrape and crawl
        user = User.query.filter_by(username=args['username']).first()
        if user.api_key == args['api_key']:
            corpus_test = Corpus.query.filter_by(seed_url=args['seed_url']).first()
            if corpus_test is None:
                scrape_crawl.url = args['seed_url']
                corpus_file = UPLOAD_FOLDER + args['corpus_file']
                model_file = UPLOAD_FOLDER + args['model_file']
                scrape_crawl.crawl(corpus_file, model_file)
                corp = Corpus(
                    user_id=user.id,
                    api_key=args['api_key'],
                    title=args['title'],
                    type=args['type'],
                    seed_url=args['seed_url'],
                    description=args['description'],
                    corpus_file=args['corpus_file'],
                    model_file=args['model_file']
                )
                db.session.add(corp)
                db.session.commit()
                response = {'response': 'new corpus added.'}
            else:
                response = {'response': 'corpus already exists.'}
        else:
            response = {'response': 'user not authorized.'}
        return jsonify(response)


class CorpusResource(Resource):

    def get(self):
        args = load_corpus.parse_args()
        corpa = Corpus.query.filter_by(title=args['title']).first()
        if not corpa:
            abort(404)
        return corpa

    def delete(self):
        corpa = Corpus.delete(**load_corpus.parse_args())
        if not corpa:
            abort(404)
        return 204


class CorpusCollection(Resource):

    def get(self):
        args = corpus_collection.parse_args()
        data = Corpus.query_filter_by(user_id=args['user_id']).first()
        if not data:
            abort(404)
        return data


api.add_resource(AddCorpusFromUrl, '/corpus/add')
api.add_resource(CorpusResource, '/corpus/<corpus_name>', '/corpus/<int:corpus_id>')
api.add_resource(CorpusCollection, '/corpus/list')
