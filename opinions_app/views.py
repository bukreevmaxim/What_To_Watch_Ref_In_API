from random import randrange
from flask import render_template, abort, flash, request, redirect, url_for
from opinions_app import db
from opinions_app.models import Opinion
from opinions_app.forms import OpinionForm


def random_opinion():
    quantity = Opinion.query.count()
    if quantity:
        offset_value = randrange(quantity)
        opinion = Opinion.query.offset(offset_value).first()
        return opinion

def index_view():
    opinion = random_opinion()
    # Если random_opinion() вернула None, значит, в БД нет записей.
    if opinion is None:
        abort(500)
    return render_template('opinion.html', opinion=opinion)

def add_opinion_view():
    form = OpinionForm()
    if form.validate_on_submit():
        text = form.text.data
        if Opinion.query.filter_by(text=text).first() is not None:
            flash('Такое мнение уже было оставлено ранее!')
            return render_template('add_opinion.html', form=form)
        opinion = Opinion(
            title=form.title.data,
            text=text,
        )
    return render_template('add_opinion.html', form=form)

def opinion_view(id):
    opinion = Opinion.query.get_or_404(id)
    return render_template('opinion.html', opinion=opinion)