## Path hack
import sys, os
sys.path.insert(0, os.path.abspath('.'))

import sys

from crow.app import create_app, db
from crow.data.models import Sentiment, Author

def newAuthor():
  with create_app().app_context():
    name = input("Name: ")
    author = Author(name=name)
    db.session.add(author)
    db.session.commit()
    print("Author successfully added.")

def newSentiment():
  with create_app().app_context():
    content = input("Content: ")
    authorName = input("Author: ")

    author = Author.query.filter_by(name=authorName).first()
    if author:
      sentiment = Sentiment(content=content, author=author)
      db.session.add(sentiment)
      db.session.commit()
      print("Sentiment successfully added.")
    else:
      print(f"No author found with name ({authorName}).")
      createAuthor = input(f"Create new author with name ({authorName})? (Y/n): ")
      if createAuthor != "n" or createAuthor != "N":
        author = Author(name=authorName)
        sentiment = Sentiment(content=content, author=author, source="https://stocktwits.com/symbol/BTC.X")
        db.session.add(author)
        db.session.add(sentiment)
        db.session.commit()
        print("Sentiment successfully added.")

if __name__ == "__main__":
  if len(sys.argv) > 1:
    if sys.argv[1] == "--author":
      newAuthor()
    if sys.argv[1] == "--sentiment":
      newSentiment()