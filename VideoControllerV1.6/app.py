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
        return flask.render_template("videoSelect.html", number=number)
    else:
        return flask.render_template("videoSelect.html", number=number)

@app.route('/selectvideo/videoRunner', methods=['POST'])
def videoRunner():
    """Video streaming home page."""
    return flask.render_template('videoPlayer.html')

@app.route('/selectvideo/videoRunner/video_feed')
def video_feed():
    global number
    #Video streaming route. Put this in the src attribute of an img tag
    return flask.Response(main.start(number), mimetype='multipart/x-mixed-replace; boundary=frame')