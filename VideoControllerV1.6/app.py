import flask
import main

app = flask.Flask(__name__)
number = "2018555055"
logined = False

@app.route("/")
def login():
    global logined
    logined = False
    return flask.render_template("login.html")

@app.route("/selectvideo", methods=['POST'])
def selectVideo():
    global logined
    global number
    if logined == False:
        number = flask.request.form["number"]
        logined = True
        return flask.render_template("runVideo.html", number=number)
    else:
        return flask.render_template("runVideo.html", number=number)

@app.route("/videorun", methods=['POST'])
def videoRun():
    global number
    main.start(number)
    return flask.render_template("return.html")
