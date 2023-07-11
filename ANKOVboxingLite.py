# import required library
import webbrowser
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, This is ANKOV boxing!</p>"

# call webbrowser.open() function.
webbrowser.open_new("http://127.0.0.1:5000")

# Start server
app.run()