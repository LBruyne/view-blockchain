from typing import List
from backend.bc.simchain import Network
from backend.bc.simchain import Peer
from backend.bc.simchain import Block


class Blockchain:

    def __init__(self):
        self.net: Network = None
        self.peers: List[Peer] = []
        self.blockchain: List[Block] = []
        self.NUM_OF_PEERS: int = 12  # 设置12个初始节点
        self.DEFAULT_BALANCE: float = 10000  # 以分为单位

    def run(self):
        self.net = Network(self.NUM_OF_PEERS, self.DEFAULT_BALANCE)
        self.peers = self.net.peers
        self.blockchain = self.peers[0].blockchain

    def get_peers(self):
        if self.net is None:
            raise Exception("区块链未初始化")
        self.peers = self.net.peers
        return self.peers

    def get_blockchain(self):
        if self.net is None:
            raise Exception("区块链未初始化")
        self.blockchain = self.peers[0].blockchain
        return self.blockchain

    def get_network(self):
        if self.net is None:
            raise Exception("区块链未初始化")
        return self.net


blockchain = Blockchain()
blockchain.run()
