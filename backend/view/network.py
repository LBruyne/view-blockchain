import time
from typing import List

from flask import Blueprint
from backend.model.http_result import HttpResult
from backend.model.blockchain import blockchain
from simchain import Block, Peer, Network

app_network = Blueprint("network", __name__)


@app_network.route('/network/detail')
def get_network_info():
    net: Network = blockchain.get_network()
    bc: List[Block] = blockchain.get_blockchain()
    peers: List[Peer] = blockchain.get_peers()

    data = {
        "peer_num": len(net.peers),
        "block_height": len(bc),
        "local_time": get_timestamp(),
        "current_winner": net.current_winner.addr,
        "GDP": get_all_balance(peers),
        "num_of_txs": get_all_txs_num(bc)
    }

    return HttpResult.success_result(data)


def get_timestamp():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))


def get_all_balance(peers: List[Peer]):
    return sum(peer.get_balance() for peer in peers)


def get_all_txs_num(bc: List[Block]):
    return sum(len(block.txs) for block in bc)
