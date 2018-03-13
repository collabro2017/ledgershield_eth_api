from web3 import Web3, HTTPProvider, IPCProvider

class Web3Util():


    def __init__(self):
        self.we3obj = Web3(HTTPProvider('http://18.219.191.49/rpc'))
        self.from_address = '0xfdb1e41acc2657337d59018ffca2dc6fd7708d4c'
        self.from_password = 'master_wallet_password'

    def create_master_account(self):
        return self.create_account(self.from_password)

    def getBlock(self, block):
        return self.we3obj.eth.getBlock(block)

    def syncing(self):
        return self.we3obj.eth.syncing

    def create_account(self, passphrase):
        return  self.we3obj.personal.newAccount(password=passphrase)

    def send_transaction(self, to, value):
        value = Web3.toWei(value, 'ether')
        print('{}, {}'.format(to, value))
        try:
            return self.we3obj.personal.sendTransaction({'to': to, 'value': value, 'from': self.from_address}, passphrase=self.from_password)
        except Exception as e:
            print(e)
            return None