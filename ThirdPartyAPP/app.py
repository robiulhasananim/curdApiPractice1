import requests
import json

URL = "http://127.0.0.1:8000/studentapi/"

def get_data(id=None):
    data = {}
    if id is not None:
        data = {'id': id}
    json_data = json.dumps(data)

    r = requests.get(url=URL, data=json_data)

    data = r.json()

    print(data)

# get_data(1)   # call for id 1    


def post_data():
    data = {
        'name':'dabul',
        'roll':104,
        'city':'Manikganj',
    }

    json_data = json.dumps(data)

    r = requests.post(url=URL, data=json_data)
    # print(r.text)
    # print(r.status_code)

    data = r.json()

    print(data)


# post_data()


def update_data():
    data = {
        'id': 4,
        'name':'ebul',
        'roll':104,
        'city':'sylhet',
    }

    json_data = json.dumps(data)

    r = requests.put(url=URL, data=json_data)
    # print(r.text)
    # print(r.status_code)

    data = r.json()

    print(data)


update_data()


