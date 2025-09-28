from os import environ

from flask import Flask, render_template, redirect, url_for, request, flash

from dotenv import load_dotenv

from utils import Record
from utils import get_records, save_record, get_form_template, delete_record
from forms import RecordForm

load_dotenv()

app = Flask(__name__)

app.config['SECRET_KEY'] = environ['FLASK_SECRET_KEY']


@app.get("/")
def list_records_view():
    records: list[Record] = get_records()
    return render_template("index.html", records=records)


@app.route("/add", methods=["GET", "POST"])
def add_edit_record_view():
    form: RecordForm = RecordForm()


    if form.validate_on_submit():
        record: Record = Record(
            id=max([r.id for r in get_records()]) + 1,
            subject=request.form['subject'],
            teacher=request.form['teacher'],
            grade=int(request.form['grade']),
            date=request.form['date']
        )
        
        if save_record(record):
            flash('Form successfuly saved!', 'success')
            return redirect(url_for('list_records_view'))
    return render_template('journal_form.html', form=form)


@app.route("/edit/<int:record_id>", methods=["GET", "POST"])
def edit_record_view(record_id: int):
        records: list[Record] = list(filter(lambda r: r.id==record_id, get_records()))
        edit_record: Record = records[0]
           
        if not records:
            return "Record is not found", 404
        
        form: RecordForm = RecordForm(data=edit_record.model_dump())
        
        if form.validate_on_submit():
            record: Record = Record(
                id=record_id,
                subject=request.form['subject'],
                teacher=request.form['teacher'],
                grade=int(request.form['grade']),
                date=request.form['date']
                )
            delete_record(edit_record)

            if save_record(record):
                flash('Form successfuly saved!', 'success')
                return redirect(url_for('list_records_view'))
        return render_template('journal_form.html', form=form, record_id=record_id)


@app.post("/delete/<int:record_id>")
def delete_record_view(record_id: int):
    records: list[Record] = [record for record in get_records() if record.id == record_id]
    if records:
        delete_record(records[0])
        return redirect(url_for('list_records_view'))
    else:
        return "Record is not found", 404
