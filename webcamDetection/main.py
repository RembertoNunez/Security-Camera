#main.py
#This is the flask handler that we
#use to route the app properly.
#It will be used in collaboration with 
#the camera py file made earlier

from flask import Flask, render_template, Response #Imports some functions from flask
from camera import VideoCamera #From our camera.py file we import the VideoCamera class

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html') #Opens the main page

def gen(camera): #Define a function gen that takes an argument, camera
    while True: #Creates an infinite will loop
        frame = camera.get_frame() #Grabs values from camera and stores them in variable fram
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__': #Allows us to run the app on a localhost
    app.run(host='0.0.0.0', debug=True)
