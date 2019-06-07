from bottle import Bottle,run,template,request,redirect,HTTPResponse
from app import db
from app.models import User,Post
import datetime

app=Bottle()

@app.route('/create',method='POST')
def create_user():
    data=request.json
    name=str(data["name"])
    username=str(data["username"])
    email=str(data["email"])
    password=str(data["password"])
    userv = User.query.filter_by(username=username).first()
    if userv is None:
        user = User.query.filter_by(username=username).first()
        user = User(name=name,username=username,email=email)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        return {"state":"Ok"}
    else:
        return {"state":"Not Ok"}

run(app,host='0.0.0.0',port=5000,debug=True)