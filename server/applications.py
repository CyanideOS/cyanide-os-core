from flask import jsonify

def _getInstalledApplications():
    return jsonify({
        "ms-outlook.microsoft.com": {
            "name": "Microsoft Outlook | Mail Client",
            "component": "ms-outlook-microsoft-com",
            "packageName": "ms-outlook.microsoft.com",
            "installedOn": 1600882638399,
        },
    })


def _serveApplicationByPid(pid):
    print(f"Serve {pid}")
    return jsonify({
        "isStarted": True,
        "isAlreadyServing": 42107,
    })
