from datetime import datetime
from sqlalchemy.dialects.postgresql import UUID
import uuid

from catalyst.app import db, login_manager

@login_manager.user_loader
def load_user(user_id):
  return User.query.filter_by(id=uuid.UUID(user_id).hex).first()

class User(db.Model, UserMixin):
  id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True)
  username = db.Column(db.String(), unique=True, nullable=False)
  password = db.Column(db.String(), nullable=False)

  clearance = db.Column(db.Integer(), nullable=False, default=0)
  ## 0 - User
  ## 1 - Admin