import time
import requests

# This library does not work well due to limitations with Discord's API.


def uploadImage(name, imageString):
    URL = "https://discord.com/api/v9/oauth2/applications/APPLICATION/assets"
    data = {
        "name": str(name),
        "image": "data:image/png;base64," + str(imageString),
        "type": "1"
    }
    print(data["image"])
    headers = {
        "Authorization": "AUTHORIZATION"
    }

    r = requests.post(URL, json=data, headers=headers)


def getAllImages():
    URL = "https://discord.com/api/v9/oauth2/applications/APPLICATION/assets"

    headers = {
        "Authorization": "AUTHORIZATION",
    }

    images = requests.get(URL, headers=headers).json()

    for image in images:
        print(image)
    print("\n")


def deleteAllImages():
    URL = "https://discord.com/api/v9/oauth2/applications/APPLICATION/assets"

    headers = {
        "Authorization": "AUTHORIZATION",
    }

    images = requests.get(URL, headers=headers).json()

    for image in images:
        requests.delete(URL + "/" + image["id"], headers=headers)
        time.sleep(10)
