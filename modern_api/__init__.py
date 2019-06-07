#!/usr/bin/env python

from flask import Blueprint
from flask_restful import Api, fields

api_blueprint = Blueprint("modern_api", __name__, url_prefix='/modern_api')
api = Api(api_blueprint)


# Import the resources to add the routes to the blueprint before the app is
# initialized
from . import user  # NOQA
from . import corpus  # NOQA
from . import topics  # NOQA
from . import sentiment
