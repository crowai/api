from flask import Blueprint, render_template, redirect, url_for

auth = Blueprint("auth", __name__)

@auth.route("/auth/login")
def login():
  return render_template("user/auth/login.html")

@auth.route("/auth/register")
def register():
  return render_template("user/auth/register.html")