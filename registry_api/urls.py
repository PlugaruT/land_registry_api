from django.urls import path

from .views import index, house_prices, transactions

urlpatterns = [
    path('', index),
    path('house-prices', house_prices, name='average-house-prices'),
    path('transactions', transactions, name='number-of-transactions')
]
