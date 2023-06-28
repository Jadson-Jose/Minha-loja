from contextlib import _RedirectStream
from flask import render_template, session, request, redirect, url_for, flash
from loja import app, db, bcrypt
from loja.admin.formulario import RegistrationForm
from .models import User
import os

from loja.admin.models import User


@app.route('/')
def home():
    return "Seja bem vindo ao sistema em flask."


@app.route('/registrar', methods=['GET', 'POST'])
def registrar():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        hash_password = bcrypt.generate_password_hash(form.password.data)
        user = User(name=form.name.data,
                    username=form.username.data,
                    email=form.email.data,
                    password=hash_password)
        db.session.add(user)
        flash('Obrigado por se registrar.')
        return _RedirectStream(url_for('login'))
    return render_template('admin/registrar.html', form=form, title="Pagina de registros")
