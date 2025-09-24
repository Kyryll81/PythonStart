from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

notes = [
    {'id': 1, 'title': 'Перша нотатка', 'content': 'Це моя перша нотатка.'},
    {'id': 2, 'title': 'Плани на тиждень', 'content': 'Вивчити Flask, створити CRUD.'}
]

next_id = 3


@app.get('/')
def index():
    return render_template('index.html', notes=notes)


@app.post('/delete/<int:note_id>')
def delete_note(note_id: int):
    global notes
    notes = [note for note in notes if note['id'] != note_id]
    
    return redirect(url_for('index'))


@app.get('/note/<int:note_id>')
def view_note(note_id):
    note: list = list(filter(lambda i: i["id"] == note_id, notes))
    if note is None:
        return "Нотатка не знайдена", 404
    return render_template('view_note.html', note=note[-1])


@app.get('/edit/<int:note_id>')
def edit_note_form(note_id):
    note: list = list(filter(lambda i: i["id"] == note_id, notes))
    if note is None:
        return "Нотатка не знайдена", 404
    return render_template('edit_note.html', note=note[0])



@app.post('/edit/<int:note_id>')
def edit_note(note_id):
    note: list = list(filter(lambda i: i["id"] == note_id, notes))
    if note is None:
        return "Нотатка не знайдена", 404
    
    note[-1]['title'] = request.form.get('title')
    note[-1]['content'] = request.form.get('content')
    
    return redirect(url_for('index'))


@app.get('/add')
def add_note_form():
    return render_template('add_note.html')


@app.post('/add')
def add_note():
    global notes
    global next_id
    title = request.form.get('title')
    content = request.form.get('content')
    
    new_note = {'id': next_id, 'title': title, 'content': content}
    notes.append(new_note)
    next_id += 1
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
