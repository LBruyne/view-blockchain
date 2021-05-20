View-BlockChain - API DOC EASY VERSION:

1、获取当前网络所有节点信息  GET:  /network/peer/list  

```javascript
{

​    "code": 200,

​    "data": [

​        {

​            "addr": "1Kv8TKJprS9UnHh9fKRKHsGrNkqopUj1qo",

​            "balance": 10000,

​            "id": 0,

​            "ipv4": "200.205.64.122"

​        },

​        {

​            "addr": "13xaHk8ah2tiit8VceCfCXqDBQMN2pbfKZ",

​            "balance": 9890,

​            "id": 1,

​            "ipv4": "171.169.154.110"

​        },

​    ],

​    "success": true

}
```



2、获取某一个节点的详细信息：GET : /network/peer/detail?pid=1

```javascript
{
    "code": 200,
    "data": {
        "addr": "1KM3hqsgpABfRsyW5bqWb8mQ9Txv9njxeJ",
        "balance": 10000,
        "id": 2,
        "ipv4": "178.185.124.169"
    },
    "success": true
}
```



3、让网络发起一次共识： GET:  /network/consensus

```javascript
{
    "blockTxs": [
        {
            "txId": "5c72f6230741c38717e2c93fa7151084f380764dafa53c22a49657301a443718",
            "txIsCoinBase": true,
            "vinList": [],
            "voutList": [
                {
                    "to_addr_peer_address": "1EVXfjPJz4uoj29zFwNSkBoFosSbF8c4XD",
                    "value": 510
                }
            ]
        },
        {
            "txId": "4ae0b080eb969383c7e579ab5b62f15a4d15909bd7bc8b9d76e6767feb5e4aae",
            "txIsCoinBase": false,
            "vinList": [
                {
                    "pointer_n": 1,
                    "pointer_tx_id": "ebe1d90abd33a35a12bcb0a1e0b2a9e6330cb743272f50a0d8122a9fa2bb2da1"
                }
            ],
            "voutList": [
                {
                    "to_addr_peer_address": "1EVXfjPJz4uoj29zFwNSkBoFosSbF8c4XD",
                    "value": 9890
                }
            ]
        }
    ],
    "code": 200,
    "log_info": [
        "7 peers are mining",
        "peer(ip:117.110.204.198)(pid=1) is winner,2.887375831604004 secs used"
    ],
    "success": true
}
```



4、创建一笔交易 POST: /network/transaction/create

```javascript
请求示例如下：
{
   "transaction_originator_id":1,
   "transaction_receipt_id":2,   
   "transaction_price":100   //以分为单位
}
```



```javascript
{
    "code": 200,
    "success": true,
    "tx": {
        "txId": "4ae0b080eb969383c7e579ab5b62f15a4d15909bd7bc8b9d76e6767feb5e4aae",
        "txIsCoinBase": false,
        "vinList": [
            {
                "pointer_n": 1,
                "pointer_tx_id": "ebe1d90abd33a35a12bcb0a1e0b2a9e6330cb743272f50a0d8122a9fa2bb2da1"
            }
        ],
        "voutList": [
            {
                "to_addr_peer_address": "1EVXfjPJz4uoj29zFwNSkBoFosSbF8c4XD",
                "value": 9890
            }
        ]
    }
}
```

5、获取一个节点的所有utxo GET: /network/peer/utxo

```javascript
请求示例如下：
{
   "peer_id":1,
}
```



```javascript
{
    "code": 200,
    "data": [
        {
            "tx_id": "728d02ec7ce216c4adf663e501564f3805913310b66656fea3172c782b4a3647",
            "tx_vout_n": 1,
            "vout_addr": "1M8Tz4pzga7HGQn9uJVRp6aKQ9pSrVo3kw",
            "vout_value": 10000
        }
    ],
    "success": true
}
```

6、获取一个节点的所有待确认的utxo GET: /network/peer/utxo/unconfirm

```javascript
请求示例如下：
{
   "peer_id":1,
}
```



```javascript
{
    "code": 200,
    "data": [
        {
            "tx_id": "728d02ec7ce216c4adf663e501564f3805913310b66656fea3172c782b4a3647",
            "tx_vout_n": 1,
            "vout_addr": "1M8Tz4pzga7HGQn9uJVRp6aKQ9pSrVo3kw",
            "vout_value": 10000
        }
    ],
    "success": true
}
```

7、获取一个节点的所有已确认的utxo GET: /network/peer/utxo/confirm

```javascript
请求示例如下：
{
   "peer_id":1,
}
```



```javascript
{
    "code": 200,
    "data": [
        {
            "tx_id": "728d02ec7ce216c4adf663e501564f3805913310b66656fea3172c782b4a3647",
            "tx_vout_n": 1,
            "vout_addr": "1M8Tz4pzga7HGQn9uJVRp6aKQ9pSrVo3kw",
            "vout_value": 10000
        }
    ],
    "success": true
}
```

8、往网络中增加一个节点 GET: /network/peer/add

```javascript
{
    "code": 200,
    "data": {
        "addr": "1DSpQV7kVYQG3kCz21A68W8Nd1UEHbSk4B",
        "balance": 0,
        "id": 12,
        "ipv4": "31.165.196.139"
    },
    "success": true
}
```