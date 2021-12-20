from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


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
    photo_url = db.Column(db.Text, nullable=True, unique=False)
    age = db.Column(db.Integer, nullable=True, unique=False)
    notes = db.Column(db.Text, nullable=True, unique=False)
    available = db.Column(db.Boolean, nullable=False, unique=False, default=True)
