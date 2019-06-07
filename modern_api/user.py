#!/usr/bin/env python
import uuid
from flask import abort, jsonify
from flask_restful import Resource, reqparse, marshal_with, fields
from werkzeug.security import generate_password_hash, check_password_hash
from modern_api import api
from models.user import User
from extensions import db

add_user_parser = reqparse.RequestParser()
add_user_parser.add_argument('username')
add_user_parser.add_argument('email')
add_user_parser.add_argument('password_hash')
add_user_parser.add_argument('api_key')

validate_user = reqparse.RequestParser()
validate_user.add_argument('username')
validate_user.add_argument('password_hash')

get_user_data = reqparse.RequestParser()
get_user_data.add_argument('username')
get_user_data.add_argument('email')


class AddUser(Resource):

    def post(self):
        args = add_user_parser.parse_args()
        user_test = User.query.filter_by(email=args['email']).first()
        if user_test is None:
            api_key = uuid.uuid4()
            username = args['username']
            email = args['email']
            password_hash = generate_password_hash(args['password_hash'])
            user = User(username=username, email=email,
                        password_hash=password_hash, api_key=str(api_key))
            db.session.add(user)
            db.session.commit()
            response = {'response': 'new user added.'}
        else:
            response = {'response': 'user already exists.'}
        return jsonify(response)


class AuthUser(Resource):

    def post(self):
        args = validate_user.parse_args()
        user = User.query.filter_by(username=args['username']).first()
        data = {'valid_user': False}
        if user:
            valid_user = check_password_hash(user.password_hash, args['password_hash'])
            if valid_user:
                data['valid_user'] = user.api_key
        return data


class UserResource(Resource):

    def get(self):
        args = get_user_data.parse_args()
        data = {'response': 'None'}
        if args['username']:
            username = args['username']
            user = User.query.filter_by(username=username).first()
            if user:
                data['response'] = dict(id=user.id, username=user.username, email=user.email)
            else:
                abort(404)
        elif args['email']:
            email = args['email']
            user = User.query.filter_by(email=email).first()
            if user:
                data['response'] = dict(id=user.id, username=user.username, email=user.email)
            else:
                abort(404)
        else:
            abort(404)
        return jsonify(data)


class UserCollection(Resource):

    def get(self):
        users = User.query.all()
        data = []
        for user in users:
            data.append(dict(id=user.id, username=user.username, email=user.email))
        return jsonify(data)


api.add_resource(AddUser, '/users/add')
api.add_resource(AuthUser, '/login')
api.add_resource(UserResource, '/users/user')
api.add_resource(UserCollection, '/users/list')
