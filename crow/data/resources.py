import uuid

from flask_restful import Resource, reqparse

from crow.app import create_app, db
from crow.data.models import Sentiment, Author, Word
from crow.data.schemas import SentimentSchema, AuthorSchema, WordSchema


class SentimentListResource(Resource):
  def get(self):
    parser = reqparse.RequestParser()

    parser.add_argument("parsed", required=False, type=str, help="Is sentiment parsed.")
    parser.add_argument("limit", type=int)
    args = parser.parse_args()

    sentiments = Sentiment.query.all()

    if args["parsed"]:
      if args["parsed"] == "true":
        sentiments = Sentiment.query.filter_by(parsed=True).all()
      elif args["parsed"] == "false":
        sentiments = Sentiment.query.filter_by(parsed=False).all()
    if args["limit"]:
      sentiments = Sentiment.query.limit(args["limit"]).all()

    return SentimentSchema(many=True).dump(sentiments), 200

  def patch(self):
    parser = reqparse.RequestParser()

    parser.add_argument("id", type=str)
    parser.add_argument("parsed", type=str)
    args = parser.parse_args()

    if args["parsed"] == "true":
      sentiment = Sentiment.query.filter_by(id=uuid.UUID(args["id"]).hex).first()
      sentiment.parsed = True
      db.session.commit()

    return SentimentSchema(many=True).dump(sentiments), 200

  def post(self):
    parser = reqparse.RequestParser()

    parser.add_argument("content", required=True, type=str, help="Sentiment content")
    parser.add_argument("author", required=True, type=str, help="Sentiment author id")
    parser.add_argument("source", required=True, type=str, help="Sentiment source")
    parser.add_argument("excSentiment", type=str, help="Sentiment value (optional)")
    args = parser.parse_args()

    with create_app().app_context():
      try:
        author = Author.query.filter_by(id=uuid.UUID(args["author"]).hex).first()
      except ValueError:
        author = Author(name=args["author"])
        db.session.add(author)

      sentiment = Sentiment(content=args["content"].replace("\n", "").encode("ascii", "ignore").decode("ascii"), author=author, source=args["source"])

      if args["excSentiment"]:
        sentiment.excSentiment = args["excSentiment"]

      db.session.add(sentiment)
      db.session.commit()

    sentiments = Sentiment.query.all()

    return SentimentSchema(many=True).dump(sentiments), 201

class WordListResource(Resource):
  def get(self):
    parser = reqparse.RequestParser()

    parser.add_argument("word", type=str)
    args = parser.parse_args()
    if args["word"]:
      words = Word.query.filter_by(word=args["word"]).all()
    else:
      words = Word.query.all()

    return WordSchema(many=True).dump(words), 200

  def post(self):
    parser = reqparse.RequestParser()

    parser.add_argument("word", type=str)
    args = parser.parse_args()

    with create_app().app_context():
      word = Word(word=args["word"])
      db.session.add(word)
      db.session.commit()

    words = Word.query.all()

    return WordSchema(many=True).dump(words), 201

  def patch(self):
    # Make own endpoint /api/v1/words/<str:word> later
    parser = reqparse.RequestParser()

    parser.add_argument("word", type=str)
    parser.add_argument("weight", type=float)
    args = parser.parse_args()
    word = Word.query.filter_by(word=args["word"]).first()
    if args["weight"]:
      word.weight = args["weight"]
    word.frequency += 1
    db.session.commit()

class AuthorListResource(Resource):
  def get(self):
    authors = Author.query.all()

    return AuthorSchema(many=True).dump(authors), 200