## Path hack
import sys, os
sys.path.insert(0, os.path.abspath('.'))

from crow.app import create_app, db

def recreateDB():
  app = create_app()
  with app.app_context():
    db.create_all()

if __name__ == "__main__":
  recreateDB()