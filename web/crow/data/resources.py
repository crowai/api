import uuid

from flask_restful import Resource, reqparse

from crow.app import create_app, db
from crow.data.models import Sentiment, Author
from crow.data.schemas import SentimentSchema, AuthorSchema

parser = reqparse.RequestParser()

class SentimentListResource(Resource):
  def get(self):
    sentiments = Sentiment.query.all()

    return SentimentSchema(many=True).dump(sentiments)

  def post(self):
    parser.add_argument("content", required=True, type=str, help="Sentiment content")
    parser.add_argument("author", required=True, type=str, help="Sentiment author id")
    args = parser.parse_args()

    with create_app().app_context():
      author = Author.query.filter_by(id=uuid.UUID(args["author"]).hex).first()
      sentiment = Sentiment(content=args["content"], author=author)

      db.session.add(sentiment)
      db.session.commit()

    sentiments = Sentiment.query.all()

    return SentimentSchema(many=True).dump(sentiments), 201

class AuthorListResource(Resource):
  def get(self):
    authors = Author.query.all()

    return AuthorSchema(many=True).dump(authors)