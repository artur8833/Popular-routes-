import os

basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, '..', 'db.sqlite3')

UPLOAD_FOLDER = 'webapp/static/media'

ALLOWED_EXTENSIONS = {'json'}

