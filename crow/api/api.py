from flask import Blueprint, render_template

api = Blueprint("api", __name__)

@api.route("/api/v1/test")
def test():
  return "test"