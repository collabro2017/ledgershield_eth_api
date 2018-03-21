from django.shortcuts import render
from rest_framework import views, authentication, permissions, generics, status
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from utils.misc import random_string_generator
from utils.txWatcher import TxWatcher
from utils.web3 import Web3Util
from wallet.models import UserWallet


class CreateWalletView(views.APIView):

    parser_classes = (JSONParser,)

    def post(self, request, format=None):
        try:
            reference = random_string_generator()
            response = Web3Util().create_account(reference)
            if response is not None:
                uw = UserWallet(wallet_address=response, reference=reference)
                uw.save()
                return Response({'address': response})
            return Response({'data':'something went wrong while generting deposit address!'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except Exception as e:
            return  Response({'data': 'Error while processing request'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



class WalletBalance(views.APIView):

    def get(self, request, address):
        balance = Web3Util().watch_balance(address)
        return Response({'address': address, 'balance': balance})

class TestView(views.APIView):

    def get(self, request):
        address = '0xfdb1e41acc2657337d59018ffca2dc6fd7708d4c'
        Web3Util().watch_account(lambda res: TxWatcher().depositAmount(address))
        return Response({'data':'abc'})