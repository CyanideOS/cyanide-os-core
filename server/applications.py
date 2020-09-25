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
    return jsonify({
        "packageName": "microsoft",
        "name": "Outlook",
        "title": "Outlook",
        "pid": pid,
        "width": 70,
        "height": 50,
        "zIndex": 0,
        "icon": '',
        "positionY": 8,
        "positionX": 18,
        "isClosable": True,
        "isMaximizable": True,
        "isMinimizable": True,
        "isModal": False,
        "isOpenAtCenter": True,
        "port": 4200,
    })
