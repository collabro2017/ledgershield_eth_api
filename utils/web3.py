from web3 import Web3, HTTPProvider, IPCProvider

class Web3Util():


    def __init__(self):
        self.we3obj = Web3(HTTPProvider('http://18.219.213.90/rpc'))
        self.from_address = '0x2d071a04aba0724602351c0e8708b7a0ba1be71b'
        self.from_password = 'masterwallet#@1'

    def getBlock(self, block):
        return self.we3obj.eth.getBlock(block)

    def create_account(self, passphrase):
        return  self.we3obj.personal.newAccount(password=passphrase)

    def send_transaction(self, to, value):
        value = Web3.toWei(value, 'ether')
        print('{}, {}'.format(to, value))
        return self.we3obj.personal.sendTransaction({'to': to, 'value': value, 'from': self.from_address}, passphrase=self.from_password)