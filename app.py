"""Flask app for adopt app."""
import requests
from flask import Flask, redirect, render_template, request

from flask_debugtoolbar import DebugToolbarExtension

from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm

app = Flask(__name__)

app.config['SECRET_KEY'] = "secret"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///adopt"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

connect_db(app)
db.create_all()


# Having the Debug Toolbar show redirects explicitly is often useful;
# however, if you want to turn it off, you can uncomment this line:
#
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

toolbar = DebugToolbarExtension(app)
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

@app.route("/")
def home_page():
    """displays the pets and pictures"""
    pets = Pet.query.all()

    return render_template('homepage.html', pets=pets)


@app.route("/add", methods=["GET", "POST"])
def add_pet():
    """Pet add form; handle adding."""

    form = AddPetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data
        
        pet = Pet(name = name, species = species, photo_url = photo_url, age = age, notes = notes)
        db.session.add(pet)
        db.session.commit()
        
        return redirect("/")
   
    return render_template(
        "pet_add_form.html", form=form)


@app.route("/pet/<int:pet_id>", methods=["GET", "POST"])
def show_pet_info_or_edit(pet_id):
    """Show pet details."""

    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        db.session.commit()
        return redirect(f"/pet/{pet_id}")

    return render_template("pet_detail.html", form=form, pet=pet)


