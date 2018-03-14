from django.contrib import admin
from .models import UserWallet


class UserWalletAdmin(admin.ModelAdmin):
    list_display = ('pk', 'wallet_address', 'status')


admin.site.register(UserWallet, UserWalletAdmin)