from datetime import datetime
from app import db, login
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


# stu_course_identifier = db.Table('stu_co_identifier',
#     db.Column('course_id', db.Integer, db.ForeignKey('courses.id')),
#     db.Column('user_id', db.Integer, db.ForeignKey('users.id'))
# )

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    courses = db.relationship('Course', backref='user', lazy='dynamic')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User {}>'.format(self.username)


@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    prefix = db.Column(db.String(8), nullable=False)
    number = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text)
    units = db.Column(db.Integer)
    value = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    # prereqs = db.relationship('Course', backref='Course', lazy='dynamic')

    def __repr__(self):
        return f"<Course {self.prefix} {str(self.number)}>"
