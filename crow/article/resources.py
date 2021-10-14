from flask_restful import Resource, reqparse

from crow.article.models import Article, Author
from crow.article.schemas import ArticleSchema, AuthorSchema

class ArticleListResource(Resource):
  def get(self):
    parser = reqparse.RequestParser()
    parser.add_argument("title", type=str, help="Title of article")
    args = parser.parse_args()

    ## Filters
    if args["title"]:
      articles = Article.query.filter(Article.title == args["title"]).all()
      print(0)
    else:
      articles = Article.query.all()
      print(1)

    return ArticleSchema(many=True).dump(articles)

class AuthorListResource(Resource):
  def get(self):
    authors = Author.query.all()

    return AuthorSchema(many=True).dump(authors)