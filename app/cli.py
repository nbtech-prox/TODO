import click
from flask.cli import with_appcontext
from .models import User, db
from datetime import datetime

@click.command('create-admin')
@with_appcontext
def create_admin():
    admin = User.query.filter_by(email='admin@example.com').first()
    if admin:
        click.echo('Admin user already exists')
        return

    admin = User(
        email='admin@example.com',
        full_name='Admin User',
        is_admin=True,
        created_at=datetime.utcnow()
    )
    admin.set_password('admin123')
    
    db.session.add(admin)
    db.session.commit()
    
    click.echo('Admin user created successfully')

@click.command('init-db')
@with_appcontext
def init_db_command():
    if click.confirm('This will delete all data. Continue?'):
        db.drop_all()
        db.create_all()
        click.echo('Database initialized.')
