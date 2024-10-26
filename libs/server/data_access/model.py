# libs/server/data_access/model.py
from datetime import datetime
from sqlalchemy import Column, String, DateTime, Boolean
from libs.server.data_access.database import db  # Import db from database module


class Trackable:
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    created_by = Column(String, nullable=True)
    updated_at = Column(DateTime, onupdate=datetime.utcnow, nullable=True)
    updated_by = Column(String, nullable=True)
    archived = Column(Boolean, default=False, nullable=False)
    archived_at = Column(DateTime, nullable=True)
    archived_by = Column(String, nullable=True)

    def track(self, user_id: str):
        now = datetime.utcnow()
        if not self.created_at:
            self.created_at = now
            self.created_by = user_id
        self.updated_at = now
        self.updated_by = user_id

    def archive(self, user_id: str):
        self.archived = True
        self.archived_at = datetime.utcnow()
        self.archived_by = user_id


class ApiKey(db.Model, Trackable):
    __tablename__ = "api_keys"

    id = db.Column(db.String, primary_key=True)
    key = db.Column(db.String, unique=True, nullable=False)
    is_admin = db.Column(Boolean, default=False, nullable=False)
    expiry_date = db.Column(DateTime, nullable=True)
    user_id = db.Column(db.String, db.ForeignKey("users.id", name="fk_api_keys_user_id"), nullable=False)


class User(db.Model, Trackable):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
