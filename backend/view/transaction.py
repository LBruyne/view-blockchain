import random

from flask import Blueprint, request
from backend.model.blockchain import blockchain
from backend.model.http_result import HttpResult
from backend.bc.simchain import Peer

app_transaction = Blueprint("transaction", __name__)


@app_transaction.route('/network/transaction/random', methods=["GET"])
def random_transaction():
    peers = blockchain.get_peers()
    sender:Peer = random.choice(peers[1:])
    receiver = random.choice(peers[1:])
    sender.create_transaction(receiver.wallet.addrs[-1],
                              tx_random_value())
    tx = sender.current_tx
    sender.broadcast_transaction()

    vin_list = []
    vout_list = []
    for eachVin in tx.tx_in:
        print(eachVin)
        if eachVin.to_spend != None:
            vin_list.append({
                "to_spend": "" if eachVin.to_spend is None else {
                    "pointer_tx_id": eachVin.to_spend.tx_id,
                    "pointer_n": eachVin.to_spend.n,
                }
            })
    for eachVout in tx.tx_out:
        if type(eachVout.to_addr) == str:
            vout_list.append({
                "to_addr": eachVout.to_addr,
                "value": eachVout.value
            })
    data = {
        "sender": {
            "addr": sender.addr,
            "ip": sender.ipv4
        },
        "receiver": {
            "addr": receiver.addr,
            "ip": receiver.ipv4
        },
        "id": tx.id,
        "is_coinbase": tx.is_coinbase,
        "v_in": vin_list,
        "v_out": vout_list,
        "fee": tx.fee,
        "lock_time": tx.nlocktime
    }
    return HttpResult.success_result(data)


@app_transaction.route('/network/transaction/create', methods=['POST', "GET"])
def create_transaction():
    if request.method == 'OPTIONS':
        return HttpResult.success_result("")
    reqBody = request.get_json()
    transaction_originator_id = reqBody["transaction_originator_id"]
    transaction_receipt_id = reqBody["transaction_receipt_id"]
    transaction_price = reqBody["transaction_price"]

    peers = blockchain.get_peers()
    sender: Peer = peers[transaction_originator_id]
    receiver: Peer = peers[transaction_receipt_id]
    sender.create_transaction(receiver.wallet.addrs[-1], transaction_price)
    tx = sender.current_tx
    sender.broadcast_transaction()

    vin_list = []
    vout_list = []
    for eachVin in tx.tx_in:
        print(eachVin)
        if eachVin.to_spend != None:
            vin_list.append({
                "to_spend": "" if eachVin.to_spend is None else {
                    "pointer_tx_id": eachVin.to_spend.tx_id,
                    "pointer_n": eachVin.to_spend.n,
                }
            })
    for eachVout in tx.tx_out:
        if type(eachVout.to_addr) == str:
            vout_list.append({
                "to_addr": eachVout.to_addr,
                "value": eachVout.value
            })
    data = {
        "sender": {
            "addr": sender.addr,
            "ip": sender.ipv4
        },
        "receiver": {
            "addr": receiver.addr,
            "ip": receiver.ipv4
        },
        "id": tx.id,
        "is_coinbase": tx.is_coinbase,
        "v_in": vin_list,
        "v_out": vout_list,
        "fee": tx.fee,
        "lock_time": tx.nlocktime
    }
    return HttpResult.success_result(data)


def tx_random_value():
    return random.randint(0, 100)
