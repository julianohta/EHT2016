# all the imports
import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash

# create our little application :)
app = Flask(__name__)
app.config.from_object(__name__)
app.config.update(
    DEBUG=True,
)

# Load default config and override config from an environment variable
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'flaskr.db'),
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default'
))
app.config.from_envvar('FLASKR_SETTINGS', silent=True)


def connect_db():
    """Connects to the specific database."""
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv


if __name__ == '__main__':
    app.run()


def get_db():
    """Opens a new database connection if there is none yet for the
    current application context.
    """
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db


@app.teardown_appcontext
def close_db(error):
    """Closes the database again at the end of the request."""
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()


def init_db():
    db = get_db()
    with app.open_resource('schema.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()


# registers new command to flask command line tool called 'initdb' which runs init_db()
@app.cli.command('initdb')
def initdb_command():
    """Initializes the database."""
    init_db()
    print 'Initialized the database.'


# display table
@app.route('/view')
def show_entries():
    db = get_db()
    cur = db.execute('select title, text from entries order by id desc')
    entries = cur.fetchall()
    return render_template('view.html', entries=entries)


# shows
@app.route('/add', methods=['POST'])
def add_entry():
    if not session.get('logged_in'):
        abort(401)
    db = get_db()

    db.execute('insert into entries (title, text) values (?, ?)',
                 [request.form['title'], request.form['text']])
    db.commit()
    flash('New entry was successfully posted')
    return redirect(url_for('show_entries'))


@app.route('/register', methods=['GET', 'POST'])
def add_user():
    error = None
    if request.method == 'POST':

        db = get_db()

        username = request.form['username']

        user = db.execute('SELECT username, password FROM users WHERE username LIKE \'%s\'' % username)

        row = user.fetchall()
        #print(row)

        if (row is None) | (len(row) == 0):
            if len(request.form['ssid']) == 0:
                error = 'invalid account ssid'

            elif len(request.form['token']) == 0:
                error = 'invalid authentication token'

            else:

                db.execute('insert into users (username, password, account_ssid, auth_token) values (?, ?, ?, ?)',
                           [request.form['username'], request.form['password'], request.form['ssid'], request.form['token']])

                db.commit()
                flash('Successfully added user')

                return redirect(url_for('login'))

        else:
            flash('Username taken')
            error = 'invalid username'
    else:
        error = 'invalid data'

    return redirect(url_for('signup', error=error))


@app.route('/signup')
def signup():
    return render_template('register.html')


@app.route('/')
def index():
    return redirect(url_for('login'))


@app.route('/login' , methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        db = get_db()
        username = request.form['username']
        password = request.form['password']
        user = db.execute('SELECT username, password FROM users WHERE username LIKE \'%s\'' % username)

        row = user.fetchall()
        if (row is not None) & (len(row) != 0):
            row = row[0]

            uname = row[0]
            pword = row[1]

            print(uname)
            print(pword)
            #uname = ""
            #pw = ""

            #for usr in users:
            #    uname = usr.username
            #    pw = usr.password

            if request.form['username'] != uname: #user[1:2]:
                error = 'Invalid username'
                #error = user
            elif request.form['password'] != pword:
                error = 'Invalid password'
            else:
                session['logged_in'] = True
                flash('You were logged in')
                # return redirect(url_for('show_entries'))

        else:
            error = 'Invalid username'
    return render_template('login.html', error=error)


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('login'))
