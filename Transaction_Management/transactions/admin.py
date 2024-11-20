from django.contrib import admin
from .models import Transaction

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('id', 'amount', 'transaction_type', 'user', 'timestamp', 'status')
# Register your models here.
