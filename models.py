from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

GENERIC_IMAGE = "data:image/jpeg;base64,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"

def connect_db(app):
    db.app = app
    db.init_app(app)

# Models Go Below!

class Pet(db.Model):
    __tablename__ = "pets"

    def __repr__(self):
        s = self
        return

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False,unique=False)
    species = db.Column(db.Text, nullable=False, unique=False)
    photo_url = db.Column(db.Text)
    age = db.Column(db.Integer, nullable=True, unique=False)
    notes = db.Column(db.Text, nullable=True, unique=False)
    available = db.Column(db.Boolean, nullable=False, unique=False, default=True)

    def image_url(self):
        """bespoke or generic image return for pet"""
        return self.photo_url or GENERIC_IMAGE
