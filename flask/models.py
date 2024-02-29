from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func

db = SQLAlchemy()

# Model for urls table
class URL(db.Model):
    id = db.Column(db.String(6), primary_key=True)
    long_url = db.Column(db.String(2000), nullable=False)

    # string representation function
    def __repr__(self):
        return f'ID: {self.id} | URL: {self.long_url}'

