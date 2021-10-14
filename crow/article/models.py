from datetime import datetime
from sqlalchemy.dialects.postgresql import UUID
import uuid

from crow.app import db

class Article(db.Model):
  """
  Model used for storing articles.
  """
  id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True)
  title = db.Column(db.String(128), nullable=False)
  date = db.Column(db.DateTime(), nullable=False, default=datetime.utcnow())

  author_id = db.Column(UUID(as_uuid=True), db.ForeignKey("author.id"), nullable=False)

class Author(db.Model):
  """
  Model used for storing article authors.
  """
  id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True)
  name = db.Column(db.String(128), nullable=False)

  articles = db.relationship("Article", backref="author", lazy=True)