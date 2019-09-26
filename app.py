from flask import Flask, render_template
import socket

# creates a Flask application, named app
app = Flask(__name__)

# a route where we will display a welcome message via an HTML template
@app.route("/")
def hello():
    message = "Hello World!"
    hostname = socket.gethostname()
    app.logger.info('Container ID: %s', hostname)
    return render_template('index.html', message=message, hostname=hostname)

# run the application
if __name__ == "__main__":
    app.run(debug=True, threaded=True)