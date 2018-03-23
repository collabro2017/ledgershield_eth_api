import ast
import json

from web3 import Web3, HTTPProvider, IPCProvider
from config.models import NodeConfig

class Web3Util():

    def __init__(self):
        node = NodeConfig.objects.get()
        self.we3obj = Web3(HTTPProvider(node.node_url))
        self.from_address = node.master_wallet_address
        self.from_password = node.master_wallet_password

    def create_master_account(self):
        return self.create_account(self.from_password)

    def getBlock(self, block):
        return self.we3obj.eth.getBlock(block)

    def syncing(self):
        return self.we3obj.eth.syncing

    def create_account(self, passphrase):
        return  self.we3obj.personal.newAccount(password=passphrase)


    def watch_account(self, callback):
        filter = self.we3obj.eth.filter('latest')
        filter.watch(callback)

    def watch_balance(self, address):
        return self.we3obj.eth.getBalance(address)


    def get_transaction(self, tx_hash):
        return self.we3obj.eth.getTransactionReceipt(tx_hash)

    def send_transaction(self, to, value):
        value = Web3.toWei(value, 'ether')
        try:
            return self.we3obj.personal.sendTransaction({'to': to, 'value': value, 'from': self.from_address}, passphrase=self.from_password), None
        except Exception as e:
            return None, self.normalize_error_message(str(e))

    def normalize_error_message(self, error):
        try:
            error_obj = ast.literal_eval(error)
            if 'message' in error_obj:
                return error_obj['message']
            return 'Unknown error occurred during withdrawal!'
        except:
            return error