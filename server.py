from flask import Flask, request
from flask_cors import CORS
from server.applications import _getInstalledApplications, _serveApplicationByPid
from server.tasks import _registerTaskByPid

app = Flask(__name__)
CORS(app)

# Application Management
@app.route("/getInstalledApplications", methods=["POST"])
def getInstalledApplications():
    return _getInstalledApplications()

@app.route("/serveApplicationByPid", methods=["POST"])
def serveApplicationByPid():
    req = request.get_json()
    return _serveApplicationByPid(req["pid"])

# Task Management
@app.route("/registerTaskByPid", methods=["POST"])
def registerTaskByPid():
    req = request.get_json()
    return _registerTaskByPid(req["pid"], req["packageName"])


app.run(debug=True)
