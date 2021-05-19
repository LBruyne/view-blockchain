from flask import Flask,request
from backend.model.blockchain import Blockchain
app = Flask(__name__)
app.config['DEBUG'] = True
NUM_OF_PEERS = 12
DEFAULT_BALANCE = 10000  # fen 为单位
blockChain = Blockchain(NUM_OF_PEERS,DEFAULT_BALANCE)

@app.route('/')
def hello_world():
    return 'Hello World!'

##获取当前网络所有节点信息，示例如下：
# "peers_info": [
#         {
#             "addr": "1DiMBemreX72W8G9oG3NdqXBEKBbEq5nmy",
#             "balance": 10000,
#             "ipv4": "169.47.96.236"
#         },
#         {
#             "addr": "1Av85BWsyy33ET32YuhVjKD63SmhhxmNi2",
#             "balance": 10000,
#             "ipv4": "214.76.5.213"
#         },
#     ]
@app.route('/network/peer/info/list')
def get_peer_info_list():
    peers = blockChain.get_peers()
    peers_info = []
    count = 0
    for peer in peers:
        # 后续根据具体所需信息进行完善
        info = {
            "id": count,
            "ipv4":peer.ipv4,
            "balance":peer.get_balance(),
            "addr":peer.addr
        }
        peers_info.append(info)
        count = count + 1

    response = dict()
    response['data'] = peers_info
    response['success'] = True
    response['code'] = 200
    return response

@app.route('/network/peer/info/detail')
# 请求示例如下：请在url中携带参数
# pid = 1
def get_peer_info_detail():
    peer_id = int(request.args.get("pid"))
    peer = blockChain.get_peers()[peer_id]
    info = {
        "id": peer_id,
        "ipv4": peer.ipv4,
        "balance": peer.get_balance(),
        "addr": peer.addr
    }

    response = dict()
    response['data'] = info
    response['success'] = True
    response['code'] = 200
    return response

## 让当前网络发起一次共识,目前在共识结束后会返回一个数组，示例如下：
# "peers_info": [
#         "7 peers are mining",
#         "peer(ip:218.228.67.204)(pid=9) is winner,4.51121187210083 secs used"
#  ]
@app.route('/network/consensus')
def consensus():
    resultInfo,block = blockChain.net.consensus()
    print(block.hash)
    txs = []
    for eachTx in block.txs:
        txId = eachTx.id
        vinlist = []
        voutlist = []
        for eachVin in eachTx.tx_in:
            print(eachVin)
            if eachVin.to_spend != None:
                vinlist.append({
                    "pointer_tx_id": eachVin.to_spend.tx_id,
                    "pointer_n": eachVin.to_spend.n,
                })
        for eachVout in eachTx.tx_out:
            if type(eachVout.to_addr) == str:
                voutlist.append({
                    "to_addr_peer_address":eachVout.to_addr,
                    "value":eachVout.value
                })
        txIsCoinBase = eachTx.is_coinbase
        data = {
            "vinList":vinlist,
            "voutList":voutlist,
            "txId":txId,
            "txIsCoinBase":txIsCoinBase
        }
        txs.append(data)
    response = dict()
    response['log_info'] = resultInfo
    response['blockTxs'] = txs
    response['success'] = True
    response['code'] = 200
    return response

@app.route('/network/transaction/create',methods=['POST'])
## 请求示例如下：
# {
#     "transaction_originator_id":1,
#     "transaction_receipt_id":2,   //
#     "transaction_price":100   #以分为单位
# }
def create_transaction():
    reqBody = request.get_json()
    transaction_originator_id = reqBody["transaction_originator_id"]
    transaction_receipt_id = reqBody["transaction_receipt_id"]
    transaction_price = reqBody["transaction_price"]

    peers = blockChain.get_peers()
    transaction_originator = peers[transaction_originator_id]
    transaction_receipt = peers[transaction_receipt_id]
    transaction_originator.create_transaction(transaction_receipt,transaction_price)
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

@app.route('/network/peer/utxo')
## 请求示例如下：
# {
#  peer_id = 1
# }
def get_peer_utxo():
    peer_id = int(request.args.get("peer_id"))

    peers = blockChain.get_peers()
    utxos = peers[peer_id].get_utxo()
    data = []
    for each in utxos:
        vout = each.vout
        pointer = each.pointer
        each_data = {
            "vout_addr":vout.to_addr,
            "vout_value":vout.value,
            "tx_id":pointer.tx_id,
            "tx_vout_n":pointer.n
        }
        data.append(each_data)

    response = dict()
    response['data'] = data
    response['success'] = True
    response['code'] = 200
    return response

@app.route('/network/peer/utxo/unconfirm')
## 请求示例如下：
# {
#  peer_id = 1
# }
def get_peer_utxo_unconfirmed():
    peer_id = int(request.args.get("peer_id"))

    peers = blockChain.get_peers()
    utxos = peers[peer_id].get_unconfirmed_utxo()
    data = []
    for each in utxos:
        vout = each.vout
        pointer = each.pointer
        each_data = {
            "vout_addr":vout.to_addr,
            "vout_value":vout.value,
            "tx_id":pointer.tx_id,
            "tx_vout_n":pointer.n
        }
        data.append(each_data)

    response = dict()
    response['data'] = data
    response['success'] = True
    response['code'] = 200
    return response

@app.route('/network/peer/utxo/confirm')
## 请求示例如下：
# {
#  peer_id = 1
# }
def get_peer_utxo_confirmed():
    peer_id = int(request.args.get("peer_id"))

    peers = blockChain.get_peers()
    utxos = peers[peer_id].get_confirmed_utxo()
    data = []
    for each in utxos:
        vout = each.vout
        pointer = each.pointer
        each_data = {
            "vout_addr":vout.to_addr,
            "vout_value":vout.value,
            "tx_id":pointer.tx_id,
            "tx_vout_n":pointer.n
        }
        data.append(each_data)

    response = dict()
    response['data'] = data
    response['success'] = True
    response['code'] = 200
    return response

@app.route('/network/peer/add')
def network_peer_add():
    peer = blockChain.net.add_peer()
    info = {
        "id": peer.pid,
        "ipv4": peer.ipv4,
        "balance": peer.get_balance(),
        "addr": peer.addr
    }
    response = dict()
    response['data'] = info
    response['success'] = True
    response['code'] = 201
    return response


if __name__ == '__main__':

    app.run(host='127.0.0.1', port=5000)
