from flask import Flask
from flask_cors import CORS
from view.default import app_default
from view.consensus import app_consensus
from view.transaction import app_transaction
from view.peer import app_peer
from view.chain import app_chain
from view.network import app_network

app = Flask(__name__)
CORS(app)
app.register_blueprint(app_default)
app.register_blueprint(app_consensus)
app.register_blueprint(app_transaction)
app.register_blueprint(app_peer)
app.register_blueprint(app_chain)
app.register_blueprint(app_network)

if __name__ == '__main__':
    app.config['DEBUG'] = True
    app.run(host='127.0.0.1', port=5000)
