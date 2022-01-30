from flask import Blueprint, render_template, redirect, url_for

from crow.user.auth.forms import LoginForm, RegisterForm

auth = Blueprint("auth", __name__)

@auth.route("/auth/login", methods=["GET", "POST"])
def login():
  form = LoginForm()

  return render_template("user/auth/login.html", form=form)

@auth.route("/auth/register")
def register():
  form = RegisterForm()

  return render_template("user/auth/register.html", form=form)