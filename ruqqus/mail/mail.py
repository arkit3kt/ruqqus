from os import environ
import requests
import time
from flask import *

from ruqqus.helpers.security import *
from ruqqus.helpers.wrappers import *
from ruqqus.classes import *
from ruqqus.__main__ import app, db

def send_mail(to_address, subject, html, from_address="Ruqqus <noreply@mail.ruqqus.com>"):

    url="https://api.mailgun.net/v3/mail.ruqqus.com/messages"

    data={"from": from_address,
          "to": [to_address],
          "subject": subject,
          "html": html
          }
        
    return requests.post(url,
                         auth=("api",environ.get("MAILGUN_KEY")),
                         data=data
                         )


def send_verification_email(user):

    url=f"https://{environ.get('domain')}/activate"
    now=int(time.time())

    token=generate_hash(f"verify+{user.email}+{user.id}+{now}")
    params=f"?email={escape(user.email)}&id={user.id}&time={now}&token={token}"

    link=url+params

    html=f"""
         <p>Welcome to Ruqqus, {user.username}!<p>
         <a href="{link}">Click here</a> to verify your email address.</p>
         """

    send_mail(to_address=user.email,
              html=html,
              subject="Validate your Ruqqus account"
              )

def send_reset_email(user):

    url=f"https://{environ.get('domain')}/reset"
    now=int(time.time())

    token=generate_hash(f"reset+{user.email}+{user.id}+{now}")
    params=f"?email={escape(user.email)}&id={user.id}&time={now}&token={token}"

    link=url+params

    html=f"""
         <p>Hi, {user.username}!<p>
         <p>A password reset was requested for your account.</p>
         <a href="{link}">Click here</a> to reset your Ruqqus password.</p>
         """

    send_mail(to_address=user.email,
              html=html,
              subject="Ruqqus Password Reset"
              )
    

@app.route("/activate", methods=["GET"])
@auth_desired
def activate():

    email=request.args.get("email","")
    id=request.args.get("id","")
    timestamp=int(request.args.get("time", "0"))
    token=request.args.get("token","")

    if int(time.time())-timestamp > 3600:
        return render_template("message.html", title="Verification link expired.", message="That link has expired."), 410


    if not validate_hash(f"verify+{email}+{id}+{timestamp}", token):
        abort(400)

    user = db.query(User).filter_by(id=id).first()
    if not user:
        abort(400)

    if user.is_activated:
        return render_template("message.html", title="Account already_verified.", message="That link has expired."), 404

    user.is_activated=True
    db.add(user)
    db.commit()
    return render_template("message.html", title="Email verified.", message=f"Your email {email} has been verified. Thank you.")
