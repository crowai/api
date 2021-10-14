from flask import Blueprint, render_template
from flask_restful import Api

from crow.article.resources import ArticleListResource, AuthorListResource

api_bp = Blueprint("api", __name__)
api = Api(api_bp)

pre = "/api/v1/"

api.add_resource(ArticleListResource, pre + "articles/", endpoint="articles")
api.add_resource(AuthorListResource, pre + "authors/", endpoint="authors")