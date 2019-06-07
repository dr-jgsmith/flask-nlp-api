# -*- coding: utf-8 -*-
"""Extensions module. Each extension is initialized in the app factory located
in __init__.py
"""
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

from flask_httpauth import HTTPBasicAuth
auth = HTTPBasicAuth()

from .nlp.txtprocessor import TxtProcessor
text_process = TxtProcessor()

from .nlp.scrape import Scrape
scrape_crawl = Scrape()

from textblob import TextBlob