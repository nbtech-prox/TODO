from flask_login import UserMixin
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from . import db, login_manager
import os
from flask import current_app
import hashlib

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

def get_static_path(filename):
    try:
        return os.path.join(current_app.root_path, 'static', filename)
    except RuntimeError:
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        return os.path.join(base_dir, 'app', 'static', filename)

def init_db():
    db.create_all()
    
    admin = User.query.filter_by(email='admin@example.com').first()
    if not admin:
        admin = User(
            email='admin@example.com',
            full_name='Admin User',
            is_admin=True,
            created_at=datetime.utcnow()
        )
        admin.set_password('admin123')
        db.session.add(admin)
        db.session.commit()

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(128))
    full_name = db.Column(db.String(200))
    profile_image = db.Column(db.String(100), nullable=True)
    is_admin = db.Column(db.Boolean, default=False, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    last_login = db.Column(db.DateTime)
    todos = db.relationship('Todo', backref='user', lazy=True)

    def set_password(self, password):
        self.password = generate_password_hash(password, method='pbkdf2:sha256')

    def check_password(self, password):
        return check_password_hash(self.password, password)

    @property
    def avatar_url(self):
        if self.profile_image:
            return f'/static/profile_pics/{self.profile_image}'
        
        email_hash = hashlib.md5(self.email.lower().encode('utf-8')).hexdigest()
        return f'https://www.gravatar.com/avatar/{email_hash}?d=mp&s=200'

    def __repr__(self):
        return f"User('{self.email}')"

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    completed = db.Column(db.Boolean, default=False)
    priority = db.Column(db.Integer, default=2)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow)
    completed_at = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
