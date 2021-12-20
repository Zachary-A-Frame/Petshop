from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField

class AddPetForm(FlaskForm):
    """Form for adding pets."""

    name = StringField("Pet Name")
    species = StringField("Species")
    photo_url = StringField("Photo url (Optional)")
    age = IntegerField("Age")
    notes = TextAreaField("Note (Optional)")

