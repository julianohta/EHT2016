from flask import Flask, render_template, request
import reportreq

app = Flask(__name__)
app.config.update(
    DEBUG=True,
)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/report', methods=["POST","GET"])
def report():
    # db = get_db()
    # cur = db.execute('select title, text from entries order by id desc')
    # entries = cur.fetchall()
    #geoinfo = reportreq.getgeoinfo()
    print("hello")
    if request.method == 'POST':
        addr = request.form["address"]
        print(addr)
    	return render_template('report.html', lat=reportreq.getLat(addr), lng=reportreq.getLng(addr))
    else:
    	return render_template('report.html')
    #return render_template('report.html', lat=geoinfo["latitude"], lng=geoinfo["longitude"])
    #addrInfo = reportreq.getAddrInfo(addr)


if __name__ == "__main__":
    app.run()
