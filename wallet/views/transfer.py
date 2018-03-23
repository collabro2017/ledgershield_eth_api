import json

from rest_framework import views, status
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from utils.web3 import Web3Util


class TransferView(views.APIView):

    parser_classes = (JSONParser,)

    def post(self, request, format=None):
        outs = []
        try:
            if type(request.data) == list:
                data = request.data
            else:
                data = json.loads(request.data)

            for obj in data:
                print("Transferring [{}] ETH to wallet [{}]".format(obj['amount'], obj['address']))
                txid, error = Web3Util().send_transaction(obj['address'], obj['amount'])
                print('{} {}'.format(txid, error))
                out = obj.copy()
                out.update({'tx_hash': txid, 'comment': error})
                outs.append(out)
            return Response({'data': outs})
        except Exception as ex:
            return Response({'error': 'something went wrong while transferring funds'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
