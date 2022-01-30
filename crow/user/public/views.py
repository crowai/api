from flask import Blueprint, render_template, redirect, url_for

user = Blueprint("user", __name__)

@user.route("/p/<string:username>")
def profile(username):
  return render_template("user/public/profile.html")