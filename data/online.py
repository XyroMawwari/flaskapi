import requests

def online():
    online = requests.get('https://www.growtopiagame.com/detail').json()
    player = online['online_user']
    return player