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
  sentiment = db.Column(db.Float(), nullable=False, default=0.5)

  date = db.Column(db.DateTime(), nullable=False, default=datetime.utcnow())

  author_id = db.Column(UUID(as_uuid=True), db.ForeignKey("author.id"), nullable=False)

class Author(db.Model):
  """
  Model used for storing sentiment authors.
  """
  id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True)
  name = db.Column(db.String(128), nullable=False)

  sentiments = db.relationship("Sentiment", backref="author", lazy=True)