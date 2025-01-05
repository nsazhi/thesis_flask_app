from flask import render_template, flash, redirect, url_for
from .forms import LoginForm
from mff_app.admin import bp


@bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}'.format(form.username.data))
        return redirect(url_for(''))
    return render_template('login.html', form=form)


@bp.route('/panel', )