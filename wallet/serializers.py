from rest_framework import serializers
from .models import UserWallet


class CreateWalletSerializer(serializers.Serializer):

    class Meta:
        model = UserWallet
        fields = ('wallet_address', 'reference')