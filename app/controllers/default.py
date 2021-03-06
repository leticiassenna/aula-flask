from flask import render_template, flash, redirect, url_for
from flask_login import login_user, logout_user
from app import app, db, lm

from app.models.tables import User
from app.models.forms import LoginForm, CadastroForm

@lm.user_loader
def load_user(id):
    return User.query.filter_by(id=id).first()

@app.route("/index")
@app.route("/")
def index():
	return render_template('index.html')

@app.route("/login", methods=["GET", "POST"])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(username=form.username.data).first()
		if user and user.password == form.password.data:
			login_user(user)
			flash("Loged in.")
			return redirect(url_for("index"))
		else:
			flash("Invalid login.")
	return render_template('login.html',
		form=form)

@app.route("/logout")
def logout():
	logout_user()
	flash("Logged out!")
	return redirect(url_for("index"))


@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    form = CadastroForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.username == form.username.data:
                flash("User already used!")
                return redirect(url_for("cadastro"))
        else:
            user = User.query.filter_by(email=form.email.data).first()
            if user and user.email == form.email.data:
                flash("Email already used!")
                return redirect(url_for("cadastro"))
            else:
                new_user = User(form.username.data, form.password.data, form.name.data, form.email.data)
                flash("Registered with success!")
    	db.session.add(new_user)
    	db.session.commit()

    return render_template('cadastro.html', form=form)
