
from database import (
    db,
    relationship,
)
from .corpus import Corpus


class User(db.Model):

    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    password_hash = db.Column(db.String, nullable=False)
    api_key = db.Column(db.String, nullable=False)

    corpus = relationship(Corpus, backref=db.backref('user'))

    def __repr__(self):  # pragma: nocover
        return '<User({username!r})>'.format(username=self.username)