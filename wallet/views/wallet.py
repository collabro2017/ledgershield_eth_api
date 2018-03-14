from django.shortcuts import render
from rest_framework import views, authentication, permissions, generics, status
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from utils.misc import random_string_generator
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