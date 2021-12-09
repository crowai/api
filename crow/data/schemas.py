from crow.app import ma
from crow.data.models import Sentiment, Author, Word

from marshmallow_sqlalchemy.fields import Nested

class SentimentSchema(ma.Schema):
  class Meta:
    fields = (
      "id",
      "content",
      "author",
      "sentiment",
      "excSentiment",
      "source",
      "date",
      "parsed",
    )
    
    ordered = True
    model = Sentiment

  # author = Nested(lambda: AuthorSchema(only=("name",)))
  author = ma.URLFor("api.authors", values=dict(id="<author_id>"))

class WordSchema(ma.Schema):
  class Meta:
    fields = (
      "id",
      "word",
      "weight",
      "accuracy",
      "frequency",
    )

    ordered = True
    model = Word

  words = ma.URLFor("api.words", values=dict(id="<word_id>"))
  
class AuthorSchema(ma.Schema):
  class Meta:
    fields = (
      "id",
      "name",
      "sentiments",
    )

    ordered = True
    model = Author
  
  sentiments = Nested(lambda: SentimentSchema(exclude=("author",)), many=True)