from datetime import datetime

from sqlalchemy import select
from flask import render_template, request, redirect, url_for, flash

from forms import RecordForm

from db import Record, SerializedRecord


def init_routes(app, db):
    @app.get("/")
    def list_records_view():
        records: list[Record] = Record.query.all()
        return render_template("index.html", records=records)


    @app.route("/add", methods=["GET", "POST"])
    def add_edit_record_view():
        form: RecordForm = RecordForm()

        if form.validate_on_submit():
            record: Record = Record(
                subject=request.form['subject'],
                teacher=request.form['teacher'],
                grade=int(request.form['grade']),
                date=request.form['date']
            )
            db.session.add(record)
            db.session.commit()
            
            last_record: Record = Record.query.all()[-1]
            if last_record:
                flash('Form successfuly saved!', 'success')
                return redirect(url_for('list_records_view'))
        return render_template('journal_form.html', form=last_record)


    @app.route("/edit/<int:record_id>", methods=["GET", "POST"])
    def edit_record_view(record_id: int):
            edit_record: Record = db.session.get_or_404(Record, record_id)
            
            edit_data: dict = SerializedRecord.model_validate(edit_record).model_dump()

            form: RecordForm = RecordForm(data=edit_data)

            if form.validate_on_submit():
                record: Record = Record(
                    id=record_id,
                    subject=request.form['subject'],
                    teacher=request.form['teacher'],
                    grade=int(request.form['grade']),
                    date=request.form['date']
                    )
                record.subject = request.form['subject']
                record.teacher = request.form['teacher']
                record.grade = int(request.form['grade'])
                record.date = datetime.strptime(request.form['date'], '%Y-%m-%d')
                db.session.commit()

                flash('Form successfuly saved!', 'success')
                return redirect(url_for('list_records_view'))
            return render_template('journal_form.html', form=form, record_id=record_id)


    @app.post("/delete/<int:record_id>")
    def delete_record_view(record_id: int):
        record: Record = db.session.get_or_404(Record, record_id)
        db.session.delete(record)
        db.session.commit()
        return redirect(url_for('list_records_view'))
