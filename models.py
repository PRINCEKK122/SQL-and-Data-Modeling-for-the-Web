from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime

app = Flask(__name__)
app.config.from_object("config")
db = SQLAlchemy(app)
migrate = Migrate(app=app, db=db)

class Venue(db.Model):
    __tablename__ = "Venue"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    city = db.Column(db.String(120), nullable=False)
    state = db.Column(db.String(120), nullable=False)
    address = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(120), nullable=False)
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))
    genres = db.Column(db.String(120))
    website_link = db.Column(db.String(120))
    seeking_talent = db.Column(db.Boolean, default=False, nullable=False)
    description = db.Column(db.String(120))
    shows = db.relationship("Show", backref="venues", lazy="select")

    def __repr__(self) -> str:
        return f"id: {self.id} Venue name: {self.name}"


class Artist(db.Model):
    __tablename__ = "Artist"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    genres = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))
    website_link = db.Column(db.String(120))
    seeking_venue = db.Column(db.Boolean, default=False, nullable=False)
    description = db.Column(db.String(120))
    shows = db.relationship("Show", backref="artists", lazy="select")

    def __repr__(self) -> str:
        return f"id: {self.id} Artist name: {self.name}"
    

class Show(db.Model):
    __tablename__ = "Show"

    id = db.Column(db.Integer, primary_key=True)
    artist_id = db.Column(db.Integer, db.ForeignKey("Artist.id"))
    venue_id = db.Column(db.Integer, db.ForeignKey("Venue.id"))
    start_time = db.Column(db.Date, nullable=False, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"id: {self.id}, start_time: {self.start_time}"
