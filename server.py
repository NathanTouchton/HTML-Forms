from os import environ
from flask import Flask, render_template, request
from emailtemplate import SendEmail

app = Flask(__name__)
send = SendEmail(smtp_server="smtp.mail.yahoo.com")

@app.route("/", methods=["GET", "POST"])
def hello():
    return render_template("index.html")

@app.route("/send", methods=["POST"])
def send_email():
    send.send_message(
        to_email=environ["TO_EMAIL"],
        message=f"Subject:Inquiry from {request.form['name']}\n\n{request.form['message']}"
    )
    return render_template("send.html")
