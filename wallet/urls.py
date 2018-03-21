from django.conf.urls import url
from django.urls import include
from .views.wallet import CreateWalletView, TestView, WalletBalance
from .views.transfer import TransferView

urlpatterns = [
    url(r'^new', CreateWalletView.as_view()),
    url(r'^transfer', TransferView.as_view()),
    url(r'^test', TestView.as_view()),
    url(r'^balance/(?P<address>[^\/]+)$', WalletBalance.as_view())
]