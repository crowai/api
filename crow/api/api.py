from flask import Blueprint, render_template
from flask_restful import Api

from crow.data.resources import SentimentListResource, AuthorListResource

api_bp = Blueprint("api", __name__)
api = Api(api_bp)

pre = "/api/v1/"

api.add_resource(SentimentListResource, pre + "sentiments", endpoint="sentiments")
api.add_resource(AuthorListResource, pre + "authors", endpoint="authors")