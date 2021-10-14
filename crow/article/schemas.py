from crow.app import ma
from crow.article.models import Article

class ArticleSchema(ma.Schema):
  class Meta:
    fields = (
      "title",
      "date"
    )

    ordered = True
    model = Article