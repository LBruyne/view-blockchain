View-BlockChain - API DOC EASY VERSION:

0、获取当前网络的基本信息 GET: /network/detail

```javascript
{
  "code": 200,
  "data": {
    "GDP": 120000,
    "block_height": 1,
    "current_winner": null,
    "local_time": "2021-05-20 14:00:41",
    "num_of_txs": 1,
    "peer_num": 12
  },
  "success": true
}

```

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
  "data": {
    "fee": 10,
    "id": "031c4789c83e20ec6d1b7f5099040487d58055d0fe753e012b6a7f4d22e7a2e7",
    "is_coinbase": false,
    "lock_time": 0,
    "receiver": {
      "addr": "1EHAHcZWVYLSCX3sH6XAaDVNPAZ1fzTRT1",
      "ip": "219.80.215.65"
    },
    "sender": {
      "addr": "146dgr2CMBCoEQw6fvZrpLd4mXyY5TX6ah",
      "ip": "113.155.42.230"
    },
    "v_in": [
      {
        "to_spend": {
          "pointer_n": 8,
          "pointer_tx_id": "6ad87cf2b8986fc3bf4e2fe0a40c4f70eb5065abce89314b4c69045dc9302cc5"
        }
      }
    ],
    "v_out": [
      {
        "to_addr": "1EHAHcZWVYLSCX3sH6XAaDVNPAZ1fzTRT1",
        "value": 46
      },
      {
        "to_addr": "146dgr2CMBCoEQw6fvZrpLd4mXyY5TX6ah",
        "value": 9944
      }
    ]
  },
  "success": true
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

9、获取目前区块链的数据 GET: /network/blockchain/list

```javascript
{
  "code": 200,
  "data": [
    {
      "current_hash": "d1821dece51ef0ef0e7c5c8a04a52105d46495417cd8c0d05e4e2e86dd2e9515",
      "merkel_root_hash": "6ad87cf2b8986fc3bf4e2fe0a40c4f70eb5065abce89314b4c69045dc9302cc5",
      "nonce": 0,
      "previous_hash": null,
      "timestamp": 841124,
      "txs": [
        {
          "fee": 0,
          "id": "6ad87cf2b8986fc3bf4e2fe0a40c4f70eb5065abce89314b4c69045dc9302cc5",
          "is_coinbase": true,
          "lock_time": 0,
          "v_in": [
            {
              "to_spend": ""
            }
          ],
          "v_out": [
            {
              "to_addr": "13m6A6rjG9bSfFmRJSYdfiEGL97gLEhAcf",
              "value": 10000
            },
            {
              "to_addr": "18h9AsyXFCDJ9Ktr3W5ZuGC9u56K7Q52t2",
              "value": 10000
            },
            {
              "to_addr": "1J7TnX7AFKSg1ePoHGDYkbcRZWPeruJe9r",
              "value": 10000
            },
            {
              "to_addr": "12YoV9J6fLw1YyxsYhepiD92Fzwz4CtxDM",
              "value": 10000
            },
            {
              "to_addr": "1EPv83tnmGS1DKNhNnmsbkvxuU7hPT3cUt",
              "value": 10000
            },
            {
              "to_addr": "17eki86zhPB4chmdtgyHLNKpsnkoc3jkbn",
              "value": 10000
            },
            {
              "to_addr": "12PxCyq14XJkdrF62CjDX8o9cbHtQsyx99",
              "value": 10000
            },
            {
              "to_addr": "1EHAHcZWVYLSCX3sH6XAaDVNPAZ1fzTRT1",
              "value": 10000
            },
            {
              "to_addr": "146dgr2CMBCoEQw6fvZrpLd4mXyY5TX6ah",
              "value": 10000
            },
            {
              "to_addr": "14KLZwadCkZE4fWD1jQ8uHMQ77WJ8YNPm9",
              "value": 10000
            },
            {
              "to_addr": "1KviTvLnVsBwAgPGYxByrtR3KMtc4ZvFwK",
              "value": 10000
            },
            {
              "to_addr": "1KkKQtnXVfCGfJ1cJamPEzqtsGyuh7Fy34",
              "value": 10000
            }
          ]
        }
      ]
    },
    {
      "current_hash": "0000106569ff4fcbedaec796e95c28912d96f9fc2af1fe84b826a05f1a534972",
      "merkel_root_hash": "962f07c05a421473b6b86a6a76b330061bf51fc53cb48953225e46e35208ad76",
      "nonce": 117840,
      "previous_hash": "d1821dece51ef0ef0e7c5c8a04a52105d46495417cd8c0d05e4e2e86dd2e9515",
      "timestamp": 0,
      "txs": [
        {
          "fee": 0,
          "id": "9974884f66be2ac66ab036e15d7d5ce26553efc99c32488c1c3b9853730cf7d9",
          "is_coinbase": true,
          "lock_time": 0,
          "v_in": [
            {
              "to_spend": ""
            }
          ],
          "v_out": [
            {
              "to_addr": "1KkKQtnXVfCGfJ1cJamPEzqtsGyuh7Fy34",
              "value": 540
            }
          ]
        },
        {
          "fee": 10,
          "id": "4a1631e7c84e04047bfc26f023c1990af532b44b2c10ab60a91b11dabab4f51c",
          "is_coinbase": false,
          "lock_time": 0,
          "v_in": [
            {
              "to_spend": {
                "pointer_n": 5,
                "pointer_tx_id": "6ad87cf2b8986fc3bf4e2fe0a40c4f70eb5065abce89314b4c69045dc9302cc5"
              }
            }
          ],
          "v_out": [
            {
              "to_addr": "18h9AsyXFCDJ9Ktr3W5ZuGC9u56K7Q52t2",
              "value": 10
            },
            {
              "to_addr": "17eki86zhPB4chmdtgyHLNKpsnkoc3jkbn",
              "value": 9980
            }
          ]
        },
        {
          "fee": 10,
          "id": "7b4b0b5729dcd76124e0bf453ea68cbc205d102a5361e6f74165ce488d76ffbf",
          "is_coinbase": false,
          "lock_time": 0,
          "v_in": [
            {
              "to_spend": {
                "pointer_n": 1,
                "pointer_tx_id": "6ad87cf2b8986fc3bf4e2fe0a40c4f70eb5065abce89314b4c69045dc9302cc5"
              }
            }
          ],
          "v_out": [
            {
              "to_addr": "1J7TnX7AFKSg1ePoHGDYkbcRZWPeruJe9r",
              "value": 88
            },
            {
              "to_addr": "18h9AsyXFCDJ9Ktr3W5ZuGC9u56K7Q52t2",
              "value": 9902
            }
          ]
        },
        {
          "fee": 10,
          "id": "802f90332870767ac4a237457db6c79de5623c11a2f9d178926545d858529ace",
          "is_coinbase": false,
          "lock_time": 0,
          "v_in": [
            {
              "to_spend": {
                "pointer_n": 6,
                "pointer_tx_id": "6ad87cf2b8986fc3bf4e2fe0a40c4f70eb5065abce89314b4c69045dc9302cc5"
              }
            }
          ],
          "v_out": [
            {
              "to_addr": "18h9AsyXFCDJ9Ktr3W5ZuGC9u56K7Q52t2",
              "value": 24
            },
            {
              "to_addr": "12PxCyq14XJkdrF62CjDX8o9cbHtQsyx99",
              "value": 9966
            }
          ]
        },
        {
          "fee": 10,
          "id": "031c4789c83e20ec6d1b7f5099040487d58055d0fe753e012b6a7f4d22e7a2e7",
          "is_coinbase": false,
          "lock_time": 0,
          "v_in": [
            {
              "to_spend": {
                "pointer_n": 8,
                "pointer_tx_id": "6ad87cf2b8986fc3bf4e2fe0a40c4f70eb5065abce89314b4c69045dc9302cc5"
              }
            }
          ],
          "v_out": [
            {
              "to_addr": "1EHAHcZWVYLSCX3sH6XAaDVNPAZ1fzTRT1",
              "value": 46
            },
            {
              "to_addr": "146dgr2CMBCoEQw6fvZrpLd4mXyY5TX6ah",
              "value": 9944
            }
          ]
        }
      ]
    }
  ],
  "success": true
}
```

10、随机发起一次交易 POST: /network/transaction/random
```javascript
{
  "code": 200,
  "data": {
    "fee": 10,
    "id": "031c4789c83e20ec6d1b7f5099040487d58055d0fe753e012b6a7f4d22e7a2e7",
    "is_coinbase": false,
    "lock_time": 0,
    "receiver": {
      "addr": "1EHAHcZWVYLSCX3sH6XAaDVNPAZ1fzTRT1",
      "ip": "219.80.215.65"
    },
    "sender": {
      "addr": "146dgr2CMBCoEQw6fvZrpLd4mXyY5TX6ah",
      "ip": "113.155.42.230"
    },
    "v_in": [
      {
        "to_spend": {
          "pointer_n": 8,
          "pointer_tx_id": "6ad87cf2b8986fc3bf4e2fe0a40c4f70eb5065abce89314b4c69045dc9302cc5"
        }
      }
    ],
    "v_out": [
      {
        "to_addr": "1EHAHcZWVYLSCX3sH6XAaDVNPAZ1fzTRT1",
        "value": 46
      },
      {
        "to_addr": "146dgr2CMBCoEQw6fvZrpLd4mXyY5TX6ah",
        "value": 9944
      }
    ]
  },
  "success": true
}
```

11、获取节点的隐私信息 GET：/network/peer/more

```javascript
请求示例如下：
{
   "pid":1,
}
```

```javascript

  "code": 200,
  "data":
  {
      "id":1,
      "mem_pool":
      [
          {
              "fee": 10,
              "id": "88cc6234c7114c20be6fcf9d7a479f8beaea4b9b79f0db799a34c08093ec551d",
              "is_coinbase": false,
              "lock_time": 0,
              "v_in": [
                  {
                      "pub_key": "b'\\xcb\\xc8j\\x99\\xa1\\x16\\xf4<\\xfd\\x1a\\xeb\\xdbQ#\\xf0&\\xdd\\xfb#\\xaf\\xe1\\x93va\\x82^\\xe5\"\\nJ\\x1b\\xaf\\xe6M*\\xc5jR\\r\\xab\\xb5\\xebx\\xd1PJ\\x84\\x9f\\xe5\\xfc\\x98\\x87\\xd1\\x1d^\\x88f\\xbc\\x14\\xee\\x88\\x9d\\xbc\\xb8'",
                      "signature": "b'gSC\\x8c\\x90\\xe5\\x87\\xa9\\x01{\\xc4e\\xe5dEz\\x87\\x86\\x9fj\\xfc}\\\\\\xdd\\xd7\\xaaA\\xd2j0\\x053g\\xd6\\xa6\\xc9\\x08\\xcb\\x04\\xb7\\x1d\\x8e(\\x87XF6#\\t\\xe61\\xb8+\\xd1\\x85\\x1f\\xad}\\xdb\\xb5\\x03w\\xef\\xc0'",
                      "to_spend": {
                          "pointer_n": 1,
                          "pointer_tx_id": "a2fb2bab1bb8a3f9c0a853bb6b73a6c4950c9317f566c023b96c1f7ae1fc135f"
                      }
                  }
              ],
              "v_out": [
                  {
                      "to_addr": "144Advr5TKzMEv4gu5AELwGarEWi9TPUgC",
                      "value": 22
                  },
                  {
                      "to_addr": "1GoU2AkJpqTaHggfZxFgSsWF498nSvYHar",
                      "value": 9877
                  }
              ]
          },
      ],
  "success": true
```
