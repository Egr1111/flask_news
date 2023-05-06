from . import db

from datetime import datetime

class News(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), unique=True, nullable=False)
    text = db.Column(db.Text, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey("category.id"), nullable = True)
    created_date = db.Column(db.DateTime, default=datetime.utcnow)
    category = db.relationship("Category", back_populates = "news")
    

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable = False)
    news = db.relationship("News", back_populates = "category")
