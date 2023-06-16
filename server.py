from os import environ
from flask import Flask, render_template, request
from emailtemplate import SendEmail

app = Flask(__name__)

send = SendEmail(smtp_server="smtp.mail.yahoo.com")

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/login", methods=["POST"])
def send_email():
    send.send_message(
        to_email=environ["TO_EMAIL"],
        message=f"Inquiry from {request.form['name']}:\n\n{request.form['message']}"
    )
