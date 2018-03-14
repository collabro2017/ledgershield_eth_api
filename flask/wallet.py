from flask import Blueprint, jsonify

from utils.web3 import Web3Util

wallet = Blueprint('wallet', __name__)

@wallet.route('/create/<password>')
def create_wallet(password):
    account = Web3Util().create_account(password)
    return jsonify(account)

@wallet.route('/find/<address>')
def find_wallet(address):

    return 'this is test wallet {}'.format(address)
@wallet.route('/block/<block>')
def get_block(block):
    dict = Web3Util().getBlock(block=block)
    return jsonify(dict)

@wallet.route('/master')
def create_master_account():
    d = Web3Util().create_master_account()
    return jsonify(d)

@wallet.route('/transfer/<to>/<amount>')
def send_funds(to, amount):
    data = Web3Util().send_transaction(to, amount)
    print(data)
    return jsonify({'txid':data})

@wallet.route('/syncing')
def get_syncing():
    d = Web3Util().syncing()
    print(d)
    return jsonify(d)