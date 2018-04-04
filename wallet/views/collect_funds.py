from rest_framework import views, status
from rest_framework.response import Response

from wallet.tasks import collect_deposit_funds


class CollectFundsView(views.APIView):

    def get(self, request):
        collect_deposit_funds()
        return Response({'task': 'submitted'}, status=status.HTTP_200_OK)