View-BlockChain - API DOC EASY VERSION:

1、获取当前网络所有节点信息  GET:  /network/peer/info/list  

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

​    "success": **true**

}
```



2、获取某一个节点的详细信息：GET : /network/peer/info/detail?pid=1

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
    "code": 200,
    "data": [
        "5 peers are mining",
        "peer(ip:200.205.64.122)(pid=0) is winner,2.1593589782714844 secs used"
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
    "success": true
}
```

