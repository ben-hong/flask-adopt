"""Forms for adopt app."""

from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField
from wtforms.validators import InputRequired, Optional, Email, URL, AnyOf


class AddPetForm(FlaskForm):
    """Form for adding pets."""

    name = StringField(
      "Pet Name", 
      validators=[InputRequired()])

    species = StringField(
      "Species",
      validators=[InputRequired(), AnyOf(['cat', 'dog', 'porcupine'])])

    photo_url = StringField(
      "Photo URL",
      validators=[URL(), Optional()])

    age = StringField(
      "Age",
      validators=[InputRequired(), AnyOf(['baby', 'young', 'adult','senior'])])

    notes = StringField("Notes")


class EditPetForm(FlaskForm):
    """Form for editing pets."""
    photo_url = StringField(
      "Photo URL",
      validators=[URL(), Optional()])

    notes = StringField("Notes")

    available = BooleanField(
      "Available?",
      default = True,
    )