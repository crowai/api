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
    parser.add_argument("source", required=True, type=str, help="Sentiment source")
    args = parser.parse_args()

    with create_app().app_context():
      try:
        author = Author.query.filter_by(id=uuid.UUID(args["author"]).hex).first()
      except ValueError:
        author = Author(name=args["author"])
        db.session.add(author)

      sentiment = Sentiment(content=args["content"].replace("\n", "").encode("ascii", "ignore").decode("ascii"), author=author, source=args["source"])

      db.session.add(sentiment)
      db.session.commit()

    sentiments = Sentiment.query.all()

    return SentimentSchema(many=True).dump(sentiments), 201

class AuthorListResource(Resource):
  def get(self):
    authors = Author.query.all()

    return AuthorSchema(many=True).dump(authors)