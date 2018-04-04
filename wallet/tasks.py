from celery.task import task

from wallet.models import UserWallet
from utils.web3 import Web3Util
from config.models import NodeConfig

@task()
def collect_deposit_funds():
    web3 = Web3Util()
    wallets = UserWallet.objects.filter(status=False)
    config = NodeConfig.objects.get()
    _to = config.master_wallet_address
    gas_price, err = web3.get_gas_price()

    if err is not None:
        print(err)
    if gas_price is not None:
        for wallet in wallets:
            balance = web3.watch_balance(wallet.wallet_address)
            if balance > 0:
                _from = wallet.wallet_address
                gas, fee_error = web3.estimate_fee(_to, _from, balance)
                if fee_error is not None:
                    print(_to, _from, balance, fee_error)
                    break
                fee = gas_price * gas
                final_balance = (balance - fee);
                message = ""
                if final_balance > 0:
                    tx_hash, error = web3.send_from(_to,
                                                    _from,
                                                    final_balance,
                                                    wallet.reference)

                    if tx_hash is not None:
                        message = tx_hash
                        wallet.tx_hash = tx_hash
                        wallet.status = True
                        wallet.save()
                    else:
                        message = error

                    print("To {} From {} fee {} balance {} message {}".format(_to, _from, fee, final_balance, message))
                else:
                    print("Insufficient balance to transfer original balance{} fee {} final balance {}".format(balance, fee, final_balance))
