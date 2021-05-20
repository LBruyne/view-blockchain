from backend.bc.simchain import Network


class Blockchain:

    def __init__(self):
        self.net = None
        self.NUM_OF_PEERS = 12  # 设置12个初始节点
        self.DEFAULT_BALANCE = 10000  # 以分为单位

    def run(self):
        self.net = Network(self.NUM_OF_PEERS, self.DEFAULT_BALANCE)

    def get_peers(self):
        if self.net is None:
            raise Exception("区块链未初始化")
        return self.net.peers


blockchain = Blockchain()
blockchain.run()
