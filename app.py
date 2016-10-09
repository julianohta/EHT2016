# all the imports
from flask import Flask, session, g, redirect, url_for, abort, \
     render_template, flash
import os
from parse_report import process
from flask import jsonify, request
from twilio.access_token import AccessToken, IpMessagingGrant
from flask_mail import Message, Mail
from twilio.rest import TwilioRestClient
import sqlite3


app = Flask(__name__)


# create our little application :)
app.config.from_object(__name__)
app.config.update(
    DEBUG=True,
)


# Load default config and override config from an environment variable
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'app.db'),
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default',
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=587,
    MAIL_USE_TLS=True,
    MAIL_USE_SSL=False,
    MAIL_USERNAME='demomododo@gmail.com',
    MAIL_PASSWORD='hackathons',
))
app.config.from_envvar('APP_SETTINGS', silent=True)

mail = Mail(app)


#db functions
def connect_db():
    """Connects to the specific database."""
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv


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


# twilio stuff
@app.route('/')
def index():
    return app.send_static_file('index.html')


@app.route('/send_text', methods=['POST'])
def send_text():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    else:
        sid = session.get('sid')
        tkn = session.get('token')
        client = TwilioRestClient(account=sid, token=tkn)
        client.messages.create(to="+16073398907", from_="+16073912565", body=request.form['body'])
        return redirect(url_for('login'))
    #16073398907
    #18012449440


@app.route('/text')
def text():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    else:
        return render_template('text.html')


@app.route('/email')
def email():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    else:
        return render_template('email.html')


@app.route('/token')
def token():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    else:

        # get credentials for environment variables
        account_sid = session.get('sid')
        print(session.get('sid'))
        api_key = os.environ['TWILIO_API_KEY']
        api_secret = os.environ['TWILIO_API_SECRET']
        service_sid = os.environ['TWILIO_IPM_SERVICE_SID']

        # create a randomly generated username for the client
        db = get_db()
        username = session.get('user')

        identity = username

        # Create a unique endpoint ID for the
        device_id = request.args.get('device')
        endpoint = "TwilioChatDemo:{0}:{1}".format(identity, device_id)

        # Create access token with credentials
        token = AccessToken(account_sid, api_key, api_secret, identity)

        # Create an IP Messaging grant and add to token
        ipm_grant = IpMessagingGrant(endpoint_id=endpoint, service_sid=service_sid)
        token.add_grant(ipm_grant)

        # Return token info as JSON
        return jsonify(identity=identity, token=token.to_jwt())


# messaging
@app.route('/mail', methods=['POST'])
def send_mail():
    msg = Message(subject=request.form['title'], body=request.form['body'], sender="demomododo@gmail.com")
    msg.add_recipient("demomododo@gmail.com")
    mail.send(msg)

    return redirect(url_for('login'))


# display table
@app.route('/view')
def show_entries():
    if not session.get('logged_in'):
        return render_template('login.html', error='Please login and try again')
    db = get_db()

    cur = db.execute('select location,description,time,date,venue_name,venue_type from reports order by id desc')
    entries = cur.fetchall()

    victim_lst = []
    suspect_lst = []
    cur = db.execute('select victims,suspects from reports order by id desc')
    persons = cur.fetchall()
    for case in persons:
        case_victims = []
        for victim in str.split(str(case[0][:-1])):
            victim_query = db.execute('select * from persons where id='+victim)
            case_victims.append(victim_query.fetchall())

        victim_lst.append(case_victims)

        case_suspects = []
        for suspect in str.split(str(case[1][:-1])):
            suspect_query = db.execute('select * from persons where id='+suspect)
            case_suspects.append(suspect_query.fetchall())

        suspect_lst.append(case_suspects)

    return render_template('view.html', entries=entries, victims=victim_lst, suspects=suspect_lst)

@app.route('/report', methods=["POST","GET"])
def report():
    db = get_db()
    if request.method == 'POST':
        process(request, db)
    # db = get_db()
    # cur = db.execute('select title, text from entries order by id desc')
    # entries = cur.fetchall()
    #geoinfo = reportreq.getgeoinfo()
    # if request.method == 'POST':
    #     addr = request.form["address"]
    #     print(addr)
    #     return render_template('report.html', lat=reportreq.getLat(addr), lng=reportreq.getLng(addr))
    # else:
    return render_template('report.html')

#please don't hack :]
@app.route('/register', methods=['GET', 'POST'])
def add_user():
    error = None
    if request.method == 'POST':

        db = get_db()

        tax_id = request.form['tax_id']

        _tax_id = db.execute('SELECT tax_id FROM users WHERE tax_id = %s' % tax_id)

        row = _tax_id.fetchall()
        #print(row)

        if (row is None) | (len(row) == 0):
            if len(request.form['account_sid']) < 34:
                error = 'invalid account SID'

            elif len(request.form['auth_token']) < 32:
                error = 'invalid authentication token'

            else:

                db.execute('insert into users (tax_id, precinct, sector, password, first_name, last_name,' +
                           ' account_sid, auth_token) values (?, ?, ?, ?, ?, ?, ?, ?)',
                           [request.form['tax_id'], request.form['precinct'], request.form['sector'],
                            request.form['password'], request.form['first_name'], request.form['last_name'],
                            request.form['account_sid'], request.form['auth_token']])

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


@app.route('/login' , methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        db = get_db()
        tax_id = request.form['tax_id']
        user = db.execute('SELECT tax_id, password, account_sid, auth_token, last_name FROM users WHERE tax_id = %s' % tax_id)

        row = user.fetchall()
        if (row is not None) & (len(row) != 0):
            row = row[0]


            tax_id = row[0]
            pword = row[1]
            sid = row[2]
            token = row[3]
            last = row[4]


            print(request.form['tax_id'])
            print(tax_id)

            if int(request.form['tax_id']) != int(tax_id):
                error = 'Invalid tax_id'

            elif request.form['password'] != pword:
                error = 'Invalid password'

            else:
                session['logged_in'] = True
                session['user'] = last
                session['sid'] = sid
                session['token'] = token
                flash('You were logged in')
                # return redirect(url_for('show_entries'))

        else:
            error = 'Invalid username'
    return render_template('login.html', error=error)


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    session.pop('user', None)
    session.pop('sid', None)
    session.pop('token', None)
    flash('You were logged out')
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)
