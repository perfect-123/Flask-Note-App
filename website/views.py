from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for
from markupsafe import Markup
from flask_login import login_required, current_user
from .models import Note, Todo
from . import db
import json
import markdown

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        title = request.form.get('title')
        note = request.form.get('note')
        if len(note) < 1:
            flash('Note is too short!', category='error')
        else:
            new_note = Note(title=title, data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added!', category='success')
    
    # Fetch notes sorted by date in descending order
    notes = Note.query.filter_by(user_id=current_user.id).order_by(Note.date.desc()).all()
    
    # Convert Markdown to HTML for each note
    for note in notes:
        note.html_content = Markup(markdown.markdown(note.data))
    
    return render_template("home.html", user=current_user, notes=notes)


@views.route('/note', methods=['GET', 'POST'])
@views.route('/note/<int:id>', methods=['GET', 'POST'])
@login_required
def note_form(id=None):
    if id:
        note = Note.query.get_or_404(id)
        if request.method == "POST":
            title = request.form.get('title')
            note_data = request.form.get('note')

            if len(note_data) < 1:
                flash('Note is too short!', category='error')
            else:
                note.title = title
                note.data = note_data
                db.session.commit()
                flash('Note updated!', category='success')
                return redirect(url_for('views.home'))
        
        note.html_content = Markup(markdown.markdown(note.data))

    else:
        note = None
        if request.method == "POST":
            title = request.form.get('title')
            note_data = request.form.get('note')
            new_note = Note(title=title, data=note_data, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added!', category='success')
            return redirect(url_for('views.home'))

    return render_template('note_form.html', note=note, user=current_user)



@views.route('settings/<string:page>', methods = ['POST', 'GET'])
@login_required
def settings(page):
    pass


@views.route('/delete-note', methods=['POST'])
@login_required
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()
    return jsonify({})





@views.route('/todo', methods=['GET', 'POST'])
@login_required
def todo():
    if request.method == 'POST':
        todo = request.form.get('todo')
        complete = request.form.get('complete')
        if len(todo) < 1:
            flash("Don't be ridiculous! That is not a Todo Item", category='error')
        else:
            new_todo = Todo(data=todo, user_id=current_user.id)
            db.session.add(new_todo)
            db.session.commit()
            flash('Todo added!', category='success')
    return render_template("todo.html", user=current_user)

@views.route('/delete-todo', methods=['POST'])
@login_required
def delete_todo():
    todo = json.loads(request.data)
    todoId = todo['todoId']
    todo = Todo.query.get(todoId)
    if todo:
        if todo.user_id == current_user.id:
            db.session.delete(todo)
            db.session.commit()
    return jsonify({})
