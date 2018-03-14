from django.conf.urls import url
from django.urls import include
from .views.wallet import CreateWalletView
from .views.transfer import TransferView

urlpatterns = [
    url(r'^new', CreateWalletView.as_view()),
    url(r'^transfer', TransferView.as_view())
]