from flask import Flask, render_template
#from healthcheck import HealthCheck, EnvironmentDump
import socket

# creates a Flask application, named app
app = Flask(__name__)

# wrap the flask app and give a heathcheck url
# health = HealthCheck(app, "/healthcheck")
# envdump = EnvironmentDump(app, "/environment")

# add check functions
# def check_me():
#     # Code here..
#     return True, "redis ok"

# health.add_check(check_me)

# add your own data to the environment dump
# def application_data():
# 	return {
#         "maintainer": "Nhi TRAN",
#         "git": "https://github.com/nntran/hello-world"
#     }

# envdump.add_section("application", application_data)

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