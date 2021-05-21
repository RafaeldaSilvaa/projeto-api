import ssl
import os
from pymongo import MongoClient
import pymongo
import flask
from flask import Flask
from bson.json_util import dumps

myclient = MongoClient("mongodb+srv://admin:admin@clusteriq.bg4n2.mongodb.net/teste?retryWrites=true&w=majority", ssl_cert_reqs=ssl.CERT_NONE)

mydb = myclient["teste"]
mycol = mydb["teste"]
app = Flask(__name__)

@app.route('/')
def hello_world():
    #x = str(mycol.find_one(sort=[( '_id', pymongo.DESCENDING)]))

    return dumps(mycol.find_one(sort=[( '_id', pymongo.DESCENDING)]))
    #return dumps(mycol.find_one({"posicaoX": 973}))
    #Response(json.dumps(mycol.find_one(sort=[( '_id', pymongo.DESCENDING)])), mimetype='application/json')


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
