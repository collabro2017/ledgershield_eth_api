from rest_framework import views
from rest_framework.response import Response
from utils.web3 import Web3Util

class TransferView(views.APIView):

    def post(self, request, format=None):
        outs = []
        for obj in request.data:
            print("Transferring [{}]ETH to wallet [{}]".format(obj['amount'], obj['address']))
            txid = Web3Util().send_transaction(obj['address'], obj['amount'])
            out = obj.copy()
            out.update({'tx_hash': txid})
            outs.append(out)
        return Response({'data': outs})