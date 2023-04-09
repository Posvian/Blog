from flask_login import UserMixin
from sqlalchemy import Column, Integer, String, BOOLEAN

from blog.models.database import db


class User(db.Model, UserMixin):
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    email = Column(String(255), unique=True)
    password = Column(String(255))
