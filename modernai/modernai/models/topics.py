#!/usr/bin/env python
from database import (
    db,
    ReferenceCol
)


class Topics(db.Model):
    __tablename__ = 'topics'
    id = db.Column(db.Integer, primary_key=True)
    user_id = ReferenceCol('users')
    api_key = db.Column(db.String(80), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    type = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(5000))
    url = db.Column(db.String(200))
    topic = db.Column(db.String(200), nullable=False)
    occurrence = db.Column(db.String, nullable=False)
    sentiment = db.Column(db.Integer)
    polaritity = db.Column(db.Integer)

    def __repr__(self):
        return '<Corpus %r>' % self.title
