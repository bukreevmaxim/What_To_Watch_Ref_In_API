# what_to_watch/opinions_app/__init__.py

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from settings import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Новый импорт — api_views
from opinions_app import api_views, cli_commands, error_handlers, views 

@app.route('/')
def index_view():
    return views.index_view()

@app.route('/add', methods=['GET', 'POST'])
def add_opinion_view():
    return views.add_opinion_view()

@app.route('/opinion/<int:id>')
def opinion_view(id):
    return views.opinion_view(id)