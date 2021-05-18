from backend.bc.simchain import Network


class Blockchain:

    def __init__(self,num_of_peers,default_balance):
        self.blockchain = []
        self.net = Network(num_of_peers,default_balance)

    def get_peers(self):
        return self.net.peers
