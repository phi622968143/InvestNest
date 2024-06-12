# myapp/admin.py
from django.contrib import admin
from .models import User, Account, Trade, Dividend, Receive, Distribute

admin.site.register(User)
admin.site.register(Account)
admin.site.register(Trade)
admin.site.register(Dividend)
admin.site.register(Receive)
admin.site.register(Distribute)
