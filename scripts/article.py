## Path hack
import sys, os
sys.path.insert(0, os.path.abspath('.'))

import sys

from crow.app import create_app, db
from crow.article.models import Article, Author

def newAuthor():
  with create_app().app_context():
    name = input("Name: ")
    author = Author(name=name)
    db.session.add(author)
    db.session.commit()
    print("Author successfully added.")

def newArticle():
  with create_app().app_context():
    title = input("Title: ")
    authorName = input("Author: ")

    author = Author.query.filter_by(name=authorName).first()
    if author:
      article = Article(title=title, author=author)
      db.session.add(article)
      db.session.commit()
      print("Article successfully added.")
    else:
      print(f"No author found with name ({authorName}).")
      createAuthor = input(f"Create new author with name ({authorName})? (Y/n): ")
      if createAuthor != "n" or createAuthor != "N":
        author = Author(name=authorName)
        article = Article(title=title, author=author)
        db.session.add(author)
        db.session.add(article)
        db.session.commit()
        print("Article successfully added.")

if __name__ == "__main__":
  if len(sys.argv) > 1:
    if sys.argv[1] == "--author":
      newAuthor()
    if sys.argv[1] == "--article":
      newArticle()