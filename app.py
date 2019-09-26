from flask import Flask, render_template
import socket

# creates a Flask application, named app
app = Flask(__name__)
hostname = socket.gethostname()

# a route where we will display a welcome message via an HTML template
@app.route("/")
def hello():
    message = "Hello World!"
    return render_template('index.html', message=message, hostname=hostname)

# run the application
if __name__ == "__main__":
    app.logger.debug('Container ID: %s', hostname)
    app.run(debug=True, threaded=True)