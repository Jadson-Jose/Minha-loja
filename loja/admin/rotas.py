from contextlib import _RedirectStream


from flask import render_template, session, request, url_for,flash
from loja import app, db
from loja.admin.formulario import RegistrationForm


@app.route('/')
def home():
    return "Seja bem vindo ao sistema em flask."


@app.route('/registrar', methods=['GET', 'POST'])
def registrar():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        # user = User(form.username.data, form.email.data,
        # form.password.data)
        # db_session.add(user)
        flash('Obrigado por se registrar.')
        return _RedirectStream(url_for('login'))
    return render_template('admin/registrar.html', form=form, title="Pagina de registros")
