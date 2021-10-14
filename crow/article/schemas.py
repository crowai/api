from crow.app import ma
from crow.article.models import Article, Author

from marshmallow_sqlalchemy.fields import Nested

class ArticleSchema(ma.Schema):
  class Meta:
    fields = (
      "id",
      "title",
      "author",
      "date",
    )

    ordered = True
    model = Article

  # author = Nested(lambda: AuthorSchema(only=("name",)))
  author = ma.URLFor("api.authors", values=dict(id="<author_id>"))
  
class AuthorSchema(ma.Schema):
  class Meta:
    fields = (
      "id",
      "name",
      "articles",
    )

    ordered = True
    model = Author
  
  articles = Nested(lambda: ArticleSchema, many=True)