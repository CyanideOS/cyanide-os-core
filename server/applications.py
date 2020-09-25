from flask import jsonify

def _getInstalledApplications():
    return jsonify({
        "ms.outlook.microsoft.application": {
            "name": "Microsoft Outlook | Mail Client",
            "packageName": "ms-outlook.microsoft.com",
            "installedOn": 1600882638399,
        },
        "settings.cyanide.application": {
            "name": "Settings",
            "packageName": "settings.cyanide.application",
            "installedOn": 1601022220863,
        },
    })


def _serveApplicationByPid(pid):
    return jsonify({
        "packageName": "settings.cyanide.application",
        "name": "Settings",
        "title": "Settings",
        "pid": pid,
        "width": 120,
        "height": 66,
        "zIndex": 0,
        "icon": "icons/icon.png",
        "positionY": 1.5,
        "positionX": 0,
        "isClosable": True,
        "isMaximizable": True,
        "isMinimizable": True,
        "isModal": False,
        "isOpenAtCenter": True,
        "port": 4201,
    })
