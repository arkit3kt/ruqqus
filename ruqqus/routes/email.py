from flask import *
import time

from ruqqus.mail import *
from ruqqus.classes import *
from ruqqus.helpers.security import *

from ruqqus.__main__ import db, app

@app.route("/forgot_password", methods=["GET"])
def forgot_password_get():

    return render_template("forgot_password.html")

@app.route("/forgot_password", methods=["POST"])
def forgot_password_post():

    email=request.form.get("email")
    username=request.form.get("username")

    user = db.query(User).filter_by(email=email,
                                    username=username,
                                    is_activated=True
                                    ).first()

    if user:
        send_reset_email(user)

    return render_template("forgot_password_request.html")        

@app.route("/reset", methods=["GET"])
def reset_password_get():

    email=request.args.get("email")
    username=request.args.get("username")
    time=request.args.get("time")

    if not validate_hash(f"reset+{user.email}+{user.id}+{now}", request.args.get("token")):
        abort(403)

    render_template("reset_password.html")

@app.route("/reset", methods=["POST"])
@auth_required
@validate_formkey
def reset_password_post(v):

    pw=request.form.get("password")
    pv=request.form.get("confirm_password")

    if not pw==pv:
        render_template("reset_password.html", error="Passwords don't match")

    v.passhash = v.hash_password(pw)

    db.add(v)
    db.commit()

    return redirect(v.permalink)

    

    
