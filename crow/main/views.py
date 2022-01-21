from datetime import datetime, timedelta

from flask import Blueprint, render_template

from crow.data.models import Sentiment

main = Blueprint("main", __name__)

@main.route("/")
@main.route("/home")
def home():
  sentiments = len(Sentiment.query.all())
  predictionDate = datetime.now() + timedelta(hours=1)
  return render_template("main/index.html", sentiments=sentiments, predictionDate=predictionDate)
