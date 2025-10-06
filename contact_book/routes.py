from flask import Blueprint, render_template, redirect, url_for, request, flash

from forms import ContactForm
from models import Contact, db
from serializers import SerializedContact

routes: Blueprint = Blueprint("routes", __name__)


@routes.route('/' , methods=['GET'])
def list_contacts_view():
    title: str = 'Contact list'
    contacts: list[Contact] = Contact.query.all()
    return render_template('index.html', contacts=contacts, title=title)


@routes.route('/create', methods=['GET', 'POST'])
def create_contact_view():
    """
    Add a new item
    ---
    tags:
      - Create contact
    post:
      summary: New contact.
      description: Creates a new contact.
      parameters:
        - in: formData
          required: true
          type: string
          name: name
        - in: formData
          required: true
          type: string
          name: phone
        - in: formData
          required: true
          type: string
          name: email
    responses:
      200:
        description: Successfuly contact created.
        content:
          text/html
      400:
        description:
          Not found.
        content:
          text/html
    """
    title: str = "Contact form"
    form: ContactForm = ContactForm()

    if form.validate_on_submit():
        contact: Contact = Contact(
            name=request.form['name'],
            phone=request.form['phone'],
            email=request.form['email']
        )
        db.session.add(contact)
        db.session.commit()
        flash("Contact is created!")
        return redirect(url_for('routes.list_contacts_view'))
    return render_template('form.html', form=form, title=title)


@routes.route('/update/<int:contact_id>', methods=["GET", "POST"])
def update_contact_view(contact_id: int):
    """
    Update cpntact.
    ---
    tags:
      - Update contact
    post:
      summary: Update contact
      description: Updates contact if exsists.
      parameters:      
        - in: path
          required: true
          type: integer
          name: contact_id
        - in: formData
          required: true
          type: string
          name: name
        - in: formData
          required: true
          type: string
          name: phone
        - in: formData
          required: true
          type: string
          name: email
    responses:
      200:
        description: Successfuly contact changed.
        content:
          text/html
      400:
        description:
          Not found.
        content:
          text/html
    """
    title: str = "Edit form"
    contact: Contact | None = db.session.get(Contact, contact_id)
    serialized_contact: dict = SerializedContact.model_validate(contact).model_dump()
     
    form: ContactForm = ContactForm(data=serialized_contact)
    
    if form.validate_on_submit():
        contact.name = request.form['name']
        contact.phone = request.form['phone']
        contact.email = request.form['email']
        db.session.commit()
        flash("Contact is updated!")
        return redirect(url_for('routes.list_contacts_view'))
    
    return render_template('form.html', title=title, form=form, contact_id=contact_id)
        

@routes.post('/delete/<int:contact_id>')
def delete_contact_view(contact_id: int):
    """
    Delete contact.
    ---
    tags: 
      - Delete contact.
    post:
      summary: Delete contact.
      description: Delete contacts if exsists.
      parameters:
        - in: path
          required: true
          type: integer
          name: contact_id
    responses:
          200:
            description: Successfuly contact deleted.
            content:
              text/html
          400:
            description: Not found.
            content:
              text/html
    """
    contact: Contact | None = db.session.get(Contact, contact_id)
    db.session.delete(contact)
    db.session.commit()
    flash("Contact is deleted!")
    
    return redirect(url_for('routes.list_contacts_view'))
