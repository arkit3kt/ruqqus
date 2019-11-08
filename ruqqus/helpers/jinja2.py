import time
import re

from sqlalchemy import text

from ruqqus.classes.user import User
from ruqqus.classes.ips import IP
from ruqqus.__main__ import app, db, cache

youtube_regex=re.compile("^.*(youtu.be\/|v\/|u\/\w\/|embed\/|watch\?v=|\&v=)([^#\&\?]*).*")



@app.template_filter("users_here")
def users_here(x):

    now=time.time()

    cutoff=now-300

    return db.query(User).join(IP).filter(IP.created_utc>=cutoff).count()

@app.template_filter("total_users")
def total_users(x):

    return db.query(User).filter(text("ban_state>-1")).count()

@app.template_filter("youtube_embed")
def youtube_embed(url):

    try:
        yt_id=re.match(youtube_regex, url).group(2)
    except AttributeError:
        return "error"

    if yt_id and len(yt_id)==11:
        return yt_id
    else:
        return "error"
