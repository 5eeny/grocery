from flask import Flask
from flask import render_template
from flask import request

app=Flask (__name__)

@app.route('/', methods= ["GET","POST"])   #path

def firstone():
    if request.method == "GET":
        return render_template("getdetails.html")
    elif request.method=="POST":
        username = request.form["user_name"]
        return render_template("displaydetails.html", display_name=username)
    else:
        print("cant go that way")





if __name__=='__main__':
    app.debug=True
    app.run()


