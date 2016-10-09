from flask import Flask
from sms import sms_app

app = Flask(__name__)
app.register_blueprint(sms_app)

if __name__ == '__main__':
    app.run(debug=True)
