from flask import Flask, render_template, flash, redirect
from flask_debugtoolbar import DebugToolbarExtension
# from models import db, connect_db, User, Post, Tag, PostTag
from password import password
from models import db, connect_db, Pet
from forms import AddPetForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://postgres:{password}@localhost:5432/petshop"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "chickenzrcoolz"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)

toolbar = DebugToolbarExtension(app)


@app.route("/")
def home_display():
    """Build home page"""

    return render_template("home.html")


@app.route("/add")
def add_pet():
    """Add a pet to DB"""

    form = AddPetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data

        # Database work
        new_pet = Pet(name=name, species=species, photo_url=photo_url, age=age, notes=notes)
        db.session.add(new_pet)
        db.session.commit()

        flash(f"Added {name}!")
        return redirect("/")

    else:
        return render_template("pet_add_form.html", form=form)
