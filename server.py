from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/getInstalledApplications", methods=["POST"])
def index():
    return jsonify({
        "ms-outlook.microsoft.com": "ms-outlook-microsoft-com",
    })


app.run(debug=True)
