from django.conf.urls import url
from django.urls import include
from .views.wallet import CreateWalletView, WalletBalance
from .views.transfer import TransferView
from .views.collect_funds import CollectFundsView

urlpatterns = [
    url(r'^new', CreateWalletView.as_view()),
    url(r'^transfer', TransferView.as_view()),
    url(r'^balance/(?P<address>[^\/]+)$', WalletBalance.as_view()),
    url(r'^collect/deposit', CollectFundsView.as_view())
]