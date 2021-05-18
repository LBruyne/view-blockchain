from flask import Flask
from bc.simchain import Network

app = Flask(__name__)
app.config['DEBUG'] = True
net = Network(nop=1, von=10000)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/network/peer/num')
def get_peer_num():
    response = dict()
    response['num'] = len(net.peers)
    response['success'] = True
    response['code'] = 200
    return response


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
