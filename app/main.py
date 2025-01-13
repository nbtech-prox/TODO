from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from .models import Todo, User
from . import db
from datetime import datetime
from .forms import TodoForm

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/dashboard')
@login_required
def dashboard():
    todos = Todo.query.filter_by(user_id=current_user.id).order_by(Todo.created_at.desc()).all()
    return render_template('dashboard.html', todos=todos)

@main.route('/todo/new', methods=['GET', 'POST'])
@login_required
def new_todo():
    form = TodoForm()
    if form.validate_on_submit():
        todo = Todo(
            title=form.title.data,
            description=form.description.data,
            priority=form.priority.data,
            user_id=current_user.id,
            created_at=datetime.utcnow()
        )

        db.session.add(todo)
        db.session.commit()

        flash('Todo created successfully!', 'success')
        return redirect(url_for('main.dashboard'))

    return render_template('todo/new.html', form=form)

@main.route('/todo/<int:id>/edit', methods=['GET', 'POST'])
@login_required
def edit_todo(id):
    todo = Todo.query.get_or_404(id)
    form = TodoForm(obj=todo)
    
    if todo.user_id != current_user.id and not current_user.is_admin:
        flash('You do not have permission to edit this todo.', 'error')
        return redirect(url_for('main.dashboard'))

    if form.validate_on_submit():
        todo.title = form.title.data
        todo.description = form.description.data
        todo.priority = form.priority.data
        todo.completed = 'completed' in request.form

        db.session.commit()
        flash('Todo updated successfully!', 'success')
        return redirect(url_for('main.dashboard'))

    return render_template('todo/edit.html', form=form, todo=todo)

@main.route('/todo/<int:id>/delete', methods=['POST'])
@login_required
def delete_todo(id):
    todo = Todo.query.get_or_404(id)
    
    if todo.user_id != current_user.id and not current_user.is_admin:
        flash('You do not have permission to delete this todo.', 'error')
        return redirect(url_for('main.dashboard'))

    db.session.delete(todo)
    db.session.commit()
    
    flash('Todo deleted successfully!', 'success')
    return redirect(url_for('main.dashboard'))

@main.route('/todo/<int:id>/toggle', methods=['POST'])
@login_required
def toggle_todo(id):
    todo = Todo.query.get_or_404(id)
    
    if todo.user_id != current_user.id and not current_user.is_admin:
        flash('You do not have permission to update this todo.', 'error')
        return redirect(url_for('main.dashboard'))

    todo.completed = not todo.completed
    if todo.completed:
        todo.completed_at = datetime.utcnow()
    else:
        todo.completed_at = None

    db.session.commit()
    flash('Todo status updated successfully!', 'success')
    return redirect(url_for('main.dashboard'))
