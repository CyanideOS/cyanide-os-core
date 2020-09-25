from flask import Flask, request
from flask_cors import CORS
from server.applications import _getInstalledApplications, _serveApplicationByPid

app = Flask(__name__)
CORS(app)


@app.route("/getInstalledApplications", methods=["POST"])
def getInstalledApplications():
    return _getInstalledApplications()

@app.route("/serveApplicationByPid", methods=["POST"])
def serveApplicationByPid():
    req = request.get_json()
    return _serveApplicationByPid(req["pid"])


app.run(debug=True)
