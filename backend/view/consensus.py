from flask import Blueprint
from backend.model.blockchain import blockchain

app_consensus = Blueprint("consensus", __name__)


@app_consensus.route('/network/consensus')
def consensus():
    resultInfo, block = blockchain.net.consensus()
    print(block.hash)
    txs = []
    for eachTx in block.txs:
        txId = eachTx.id
        vinlist = []
        voutlist = []
        for eachVin in eachTx.tx_in:
            print(eachVin)
            if eachVin.to_spend is not None:
                vinlist.append({
                    "pointer_tx_id": eachVin.to_spend.tx_id,
                    "pointer_n": eachVin.to_spend.n,
                })
        for eachVout in eachTx.tx_out:
            if type(eachVout.to_addr) == str:
                voutlist.append({
                    "to_addr_peer_address": eachVout.to_addr,
                    "value": eachVout.value
                })
        txIsCoinBase = eachTx.is_coinbase
        data = {
            "vinList": vinlist,
            "voutList": voutlist,
            "txId": txId,
            "txIsCoinBase": txIsCoinBase
        }
        txs.append(data)
    response = dict()
    response['log_info'] = resultInfo
    response['blockTxs'] = txs
    response['success'] = True
    response['code'] = 200
    return response
