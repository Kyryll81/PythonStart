from datetime import datetime

from sqlalchemy import select
from flask import render_template, request, redirect, url_for, flash

from forms import RecordForm

from db import Record, SerializedRecord


def init_routes(app, db):
    @app.get("/")
    def list_records_view():
        """
        Get list of all grades.
        ---
        tags:
            - HTML Pages
        responses:
            200:
                description: HTML page with list of grades
                content:
                    text/html:
                        schema:
                            type: string
        """
        records: list[Record] = Record.query.all()
        return render_template("index.html", records=records)


    @app.route("/add", methods=["GET", "POST"])
    def add_edit_record_view():
        """
        Add and a new record.
        ---
        tags:
            - Records
        parameters:
          - in: formData
            name: subject
            required: true
            type: string
          - in: formData
            name: teacher
            required: true
            type: string
            type: string
          - in: formData
            name: grade
            required: true
            type: integer
            type: string
          - in: formData
            name: date
            required: true
            type: string
            format: date
        responses:
            200:
                description: Redirect to records list.
                headers:
                  Location:
                    type: string
                    description: Redirect URL
        """
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
        return render_template('journal_form.html', form=form)


    @app.route("/edit/<int:record_id>", methods=["GET", "POST"])
    def edit_record_view(record_id: int):
        """
        Edit record view.
        ---
        tags:
          - HTML Pages
        parameters:
          - in: path
            name: record_id
            type: integer
            required: True
          - in: formData
            name: subject
            required: true
            type: string
          - in: formData
            name: teacher
            required: true
            type: string
            type: string
          - in: formData
            name: grade
            required: true
            type: integer
            type: string
          - in: formData
            name: date
            required: true
            schema:
              type: string
              format: date  
        responses:
            200:
                description: Edit record view.
                content:
                    text/html:
                        schema:
                            type:string
        """
        edit_record: Record = db.session.get(Record, record_id)
        
        edit_data: dict = SerializedRecord.model_validate(edit_record).model_dump()

        form: RecordForm = RecordForm(data=edit_data)

        if form.validate_on_submit():
            edit_record.subject = request.form['subject']
            edit_record.teacher = request.form['teacher']
            edit_record.grade = int(request.form['grade'])
            edit_record.date = datetime.strptime(request.form['date'], '%Y-%m-%d')
            db.session.commit()
            
            flash('Form successfuly saved!', 'success')
            return redirect(url_for('list_records_view'))
        return render_template('journal_form.html', form=form, record_id=record_id)


    @app.post("/delete/<int:record_id>")
    def delete_record_view(record_id: int):
        """
        Delete record view.
        ---
        tags:
          - HTML Pages
        parameters:
          - in: path
            name: record_id
            type: integer
            required: True
        responses:
          200:
            description: Delete record view.
            content:
                    text/html:
                        schema:
                            type:string
        """
        record: Record = db.session.get(Record, record_id)
        db.session.delete(record)
        db.session.commit()
        return redirect(url_for('list_records_view'))
