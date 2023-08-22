from flask_login import UserMixin
from app import db

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    last_booking_date = db.Column(db.Date)
    user_type = db.Column(db.String(10), default='user')

class Doubt(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(500), nullable=False)
    replies = db.relationship('Reply', backref='doubt', lazy=True)

class Reply(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(500), nullable=False)
    doubt_id = db.Column(db.Integer, db.ForeignKey('doubt.id'), nullable=False)

class ComputerBooking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    computer = db.Column(db.String(120), nullable=False)
    slot = db.Column(db.String(120), nullable=False)
    booking_date = db.Column(db.Date, nullable=False)
    booked_by = db.Column(db.String(120))

    user = db.relationship('User', backref='bookings')

class Staff(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    department = db.Column(db.String(50), nullable=False)
    phone_number = db.Column(db.String(20), nullable=False)
    user_type = db.Column(db.String(10), default='staff')

class Query(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    staff_id = db.Column(db.Integer, db.ForeignKey('staff.id'), nullable=False)
    query_text = db.Column(db.String(500), nullable=False)
    response_text = db.Column(db.String(500))

    user = db.relationship('User', backref='queries')
    staff = db.relationship('Staff', backref='queries')
