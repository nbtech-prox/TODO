from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from .models import User, Todo
from . import db
from functools import wraps
from sqlalchemy import func

admin = Blueprint('admin', __name__, url_prefix='/admin')

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_admin:
            flash('You do not have permission to access this page.', 'error')
            return redirect(url_for('main.dashboard'))
        return f(*args, **kwargs)
    return decorated_function

@admin.route('/')
@login_required
@admin_required
def dashboard():
    total_users = User.query.count()
    total_todos = Todo.query.count()
    completed_todos = Todo.query.filter_by(completed=True).count()
    active_todos = total_todos - completed_todos
    completion_rate = (completed_todos / total_todos * 100) if total_todos > 0 else 0
    
    stats = {
        'total_users': total_users,
        'total_todos': total_todos,
        'completed_todos': completed_todos,
        'active_todos': active_todos,
        'completion_rate': round(completion_rate, 1)
    }
    
    return render_template('admin/dashboard.html', stats=stats)

@admin.route('/users')
@login_required
@admin_required
def users():
    users = User.query.order_by(User.created_at.desc()).all()
    return render_template('admin/users.html', users=users)

@admin.route('/todos')
@login_required
@admin_required
def todos():
    todos = Todo.query.order_by(Todo.created_at.desc()).all()
    return render_template('admin/todos.html', todos=todos)

@admin.route('/user/<int:user_id>/toggle-admin', methods=['POST'])
@login_required
@admin_required
def toggle_admin(user_id):
    user = User.query.get_or_404(user_id)
    
    if user.id == current_user.id:
        flash('You cannot change your own admin status.', 'error')
        return redirect(url_for('admin.users'))
    
    user.is_admin = not user.is_admin
    db.session.commit()
    
    action = 'removed from' if not user.is_admin else 'added to'
    flash(f'User {user.full_name} was {action} administrators.', 'success')
    return redirect(url_for('admin.users'))

@admin.route('/user/<int:user_id>/delete', methods=['POST'])
@login_required
@admin_required
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    
    if user.id == current_user.id:
        flash('You cannot delete your own account.', 'error')
        return redirect(url_for('admin.users'))
    
    Todo.query.filter_by(user_id=user.id).delete()
    db.session.delete(user)
    db.session.commit()
    
    flash(f'User {user.full_name} was deleted.', 'success')
    return redirect(url_for('admin.users'))
