from typing import List

from flask import Blueprint
from backend.model.http_result import HttpResult
from backend.model.blockchain import blockchain
from backend.bc.simchain import Tx, Vin, Vout

app_chain = Blueprint("chain", __name__)


@app_chain.route('/network/blockchain/list')
def get_chain():
    net = blockchain.get_network()
    bc = blockchain.get_blockchain()

    result = []
    for block in bc:
        data = {
            "previous_hash": block.prev_block_hash,
            "current_hash": block.hash,
            "txs": get_txs_in_block(block.txs),
            "nonce": block.nonce,
            "timestamp": block.timestamp,
            "merkel_root_hash": block.merkle_root_hash
        }
        result.append(data)
    return HttpResult.success_result(result)

def get_txs_in_block(txs: List[Tx]):
    result = []
    for tx in txs:
        data = {
            "id": tx.id,
            "is_coinbase": tx.is_coinbase,
            "v_in": get_v_in(tx.tx_in),
            "v_out": get_v_out(tx.tx_out),
            "fee": tx.fee,
            "lock_time": tx.nlocktime
        }
        result.append(data)
    return result


def get_v_in(tx_in: List[Vin]):
    result = []
    for vin in tx_in:
        data = {
            "to_spend": "" if vin.to_spend is None else {
                "pointer_tx_id": vin.to_spend.tx_id,
                "pointer_n": vin.to_spend.n,
            },
        }
        result.append(data)
    return result


def get_v_out(tx_out: List[Vout]):
    result = []
    for vout in tx_out:
        data = {
            "to_addr": vout.to_addr,
            "value": vout.value
        }
        result.append(data)
    return result

def format_mem_pool(mem_pool: dict):
    result = []
    for key in mem_pool.keys():
        tx: Tx = mem_pool[key]
        result.append({
            "id": tx.id,
            "is_coinbase": tx.is_coinbase,
            "v_in": get_v_in(tx.tx_in),
            "v_out": get_v_out(tx.tx_out),
            "fee": tx.fee,
            "lock_time": tx.nlocktime
        })
    return result