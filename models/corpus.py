#!/usr/bin/env python
from datetime import datetime
from database import (
    db,
    ReferenceCol
)


class Corpus(db.Model):
    __tablename__ = 'corpus'
    id = db.Column(db.Integer, primary_key=True)
    user_id = ReferenceCol('users')
    api_key = db.Column(db.String(80), nullable=False)
    title = db.Column(db.String(80), nullable=False)
    type = db.Column(db.String(80), nullable=False)
    seed_url = db.Column(db.String(200), nullable=False)
    description = db.Column(db.String(5000))
    model_file = db.Column(db.String(100), nullable=False)
    corpus_file = db.Column(db.String(100), nullable=False)
    pub_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return '<Corpus %r>' % self.title
