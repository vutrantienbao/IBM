import getopt
import signal
import time
import sys
import json
import wiotp.sdk.application
import dns
from pymongo import MongoClient
import os
from flask import Flask, request, render_template, jsonify
app = Flask(__name__, static_folder='public', template_folder='views')
# Khởi tạo một kết nối
app.secret = os.environ.get('SECRET')
myConfig = {
        "auth" :{
            "key": "a-1e4plt-muh1l3uuyj",
            "token": "GNZR+UcZgkiy*3W0z)"
            }
    }
clientMDB = MongoClient("mongodb+srv://vutrantienbao290699:vutrantienbao99@project.murnk.mongodb.net/ibm?retryWrites=true&w=majority")
# Khởi tạo một kết nối
client = wiotp.sdk.application.ApplicationClient(config=myConfig)

# Kết nối
client.connect()
db = clientMDB["ibm"]
mycol = db.record

# Sự kiện khi thiết bị gởi lên server
def myEventCallback(event):
    str = "%s event '%s' received from device [%s]: %s"
    print(json.dumps(event.data))
    mycol.insert_one({"data":json.dumps(event.data)})
# Gán sự kiện
client.deviceEventCallback = myEventCallback

# Liên tục theo dõi  các sự kiện từ thiết bị
while True:
    client.subscribeToDeviceEvents()
"""
@app.route("/")
def main():
    return "Hello World!"
"""
if __name__ == '__main__':
    app.run()

