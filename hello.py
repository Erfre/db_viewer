from db_manager import db_manager
from flask import Flask
from flask import g
from json_loader import get_settings
from json_loader import get_settings

#Not working with multiple databases yet
db_path, db_name = get_settings()
db_m = db_manager(db_path)
db_m.table = db_name

# Static is where the html,css shit is
app = Flask(__name__, static_url_path='/static/')
app.config.from_object(__name__)
app.config.update(DATABASE=db_path)
app.config.from_envvar('FLASKR_SETTINGS', silent=True)

@app.cli.command('initdb')
def initdb_command():
    """Initializes the database."""
    db = get_db()
    print("Connected to database.\n")


@app.teardown_appcontext
def close_db(error):
    """Closes the database again at the end of the request."""
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()

@app.route('/')
def show_entries():
    print(test)

#I need to figure out how the site should behave and look
@app.route('/<db_name>')
def hello():
    return "nib"
#    # return app.send_static_file('index.html')



def get_db():
    """Opens a new database connection if there is
    none yet for the current application context."""
    # not working atm
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = db_m
        g.sqlite_db.createconnect()
    return g.sqlite_db