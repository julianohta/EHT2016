import os
from flask import Flask, jsonify, request
from faker import Factory
from twilio.access_token import AccessToken, IpMessagingGrant

from flask import Blueprint
import sqlite3

sms_app = Blueprint('sms_app', __name__,
                    template_folder='templates', static_folder='static')

fake = Factory.create()


@sms_app.route('/')
def index():
    return sms_app.send_static_file('index.html')


@sms_app.route('/token')
def token():
    # get credentials for environment variables
    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    api_key = os.environ['TWILIO_API_KEY']
    api_secret = os.environ['TWILIO_API_SECRET']
    service_sid = os.environ['TWILIO_IPM_SERVICE_SID']

    # create a randomly generated username for the client
    identity = fake.user_name()

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

