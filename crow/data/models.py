from datetime import datetime
from sqlalchemy.dialects.postgresql import UUID
import uuid

from crow.app import db

class Sentiment(db.Model):
  """
  Model used for storing sentiments.
  """
  id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True)
  source = db.Column(db.String(), nullable=False)
  content = db.Column(db.String(1024), nullable=False)
  excSentiment = db.Column(db.String()) ## Sentiment either exclaimed by user or determined by NLP algorithm
  sentiment = db.Column(db.Float(), nullable=False, default=0)
  parsed = db.Column(db.Boolean(), default=False, nullable=False)

  date = db.Column(db.DateTime(), nullable=False)

  author_id = db.Column(UUID(as_uuid=True), db.ForeignKey("author.id"), nullable=False)

  def weekPassed(self):
    if (datetime.utcnow() - self.date).days >= 7:
      return True
    else:
      return False

class Word(db.Model):
  """
  Model used for storing word objects.
  """
  id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True)
  word = db.Column(db.String(), nullable=False)
  weight = db.Column(db.Float(precision=3), nullable=False, default=0)
  accuracy = db.Column(db.Float(precision=3), nullable=False, default=0)
  frequency = db.Column(db.Float(precision=3), nullable=False, default=1)

class Author(db.Model):
  """
  Model used for storing sentiment authors.
  """
  id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True)
  name = db.Column(db.String(128), nullable=False)

  sentiments = db.relationship("Sentiment", backref="author", lazy=True)