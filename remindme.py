import os
from flask import Flask, request, redirect, render_template
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)


@app.route('/')
def show_homepage():
    """Homepage for our Remind Me app."""

    return render_template('homepage.html')














if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')