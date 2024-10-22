from django.urls import path
from .views import (
    index,
    auth_view,
    organization,
    food_order_view,
    invoicing_view,
    expense_view,
    reports,
    profile,
)

urlpatterns = [
    path('', index, name='index'),  # Home page
    path('auth/', auth_view, name='auth'),  # Authentication URL
    path('organization/', organization, name='organization'),  # Organization page
    path('food-order/', food_order_view, name='food-order'),  # Food order page
    path('invoicing/', invoicing_view, name='invoicing'),  # Invoicing page
    path('expense/', expense_view, name='expense'),  # Expense page
    path('reports/', reports, name='reports'),  # Reports page
    path('profile/', profile, name='profile'),  # Profile settings page
]
