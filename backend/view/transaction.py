from flask import Blueprint, request
from backend.model.blockchain import blockchain

app_transaction = Blueprint("transaction", __name__)


@app_transaction.route('/network/transaction/create', methods=['POST'])
def create_transaction():
    reqBody = request.get_json()
    transaction_originator_id = reqBody["transaction_originator_id"]
    transaction_receipt_id = reqBody["transaction_receipt_id"]
    transaction_price = reqBody["transaction_price"]

    peers = blockchain.get_peers()
    transaction_originator = peers[transaction_originator_id]
    transaction_receipt = peers[transaction_receipt_id]
    transaction_originator.create_transaction(transaction_receipt, transaction_price)
    tx = transaction_originator.current_tx
    transaction_originator.broadcast_transaction()

    txId = tx.id
    vinlist = []
    voutlist = []
    for eachVin in tx.tx_in:
        print(eachVin)
        if eachVin.to_spend != None:
            vinlist.append({
                "pointer_tx_id": eachVin.to_spend.tx_id,
                "pointer_n": eachVin.to_spend.n,
            })
    for eachVout in tx.tx_out:
        if type(eachVout.to_addr) == str:
            voutlist.append({
                "to_addr_peer_address": eachVout.to_addr,
                "value": eachVout.value
            })
    txIsCoinBase = tx.is_coinbase
    data = {
        "vinList": vinlist,
        "voutList": voutlist,
        "txId": txId,
        "txIsCoinBase": txIsCoinBase
    }
    response = dict()
    response["tx"] = data
    response['success'] = True
    response['code'] = 200
    return response
