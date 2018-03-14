from rest_framework import views
from rest_framework.response import Response


class TransferView(views.APIView):

    def post(self, request, format=None):
        for obj in request.data:
            print("Transferring [{}]ETH to wallet [{}]".format(obj['amount'], obj['address']))
        return Response({'data': 'transfer request submitted!'})