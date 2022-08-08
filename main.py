import redis
from flask import Flask, request

app = Flask(__name__)

redis_client = redis.Redis(host='redis', port=6379, db=0, charset="utf-8", decode_responses=True)

@app.route("/", methods=['GET'])
def home():
    return f'Success.'

@app.route("/set", methods=['POST'])
def setdata():
    data = request.form
    redis_client.set(data['key'], data['value'])
    return f'Successfully added.'

@app.route("/get/<key>", methods=['GET'])
def getdata(key):
    data = redis_client.get(key)
    return f'{key}: {data}'



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')