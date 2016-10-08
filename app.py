from flask import Flask, render_template

app = Flask(__name__)
app.config.update(
    DEBUG=True,
)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/report')
def report():
    # db = get_db()
    # cur = db.execute('select title, text from entries order by id desc')
    # entries = cur.fetchall()
    return render_template('report.html')

if __name__ == "__main__":
    app.run()
