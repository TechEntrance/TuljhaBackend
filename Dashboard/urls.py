from django.urls import path
from .views import (
    index,
    organization,
    food_order_view,
    invoicing_view,
    expense_view,
    reports,
    profile,
    edit_invoice,
    delete_invoice,
)
urlpatterns = [
    path('', index, name='index'),  # Home page
    path('organization/', organization, name='organization'),  # Organization page
    path('food-order/', food_order_view, name='food-order'),  # Food order page
    path('invoicing/', invoicing_view, name='invoicing'),  # Invoicing page
    path('expense/', expense_view, name='expense'),  # Expense page
    path('reports/', reports, name='reports'),  # Reports page
    path('profile/', profile, name='profile'),  # Profile settings page
    path('edit-invoice/<int:invoice_id>/', edit_invoice, name='edit_invoice'),
    path('delete-invoice/<int:invoice_id>/', delete_invoice, name='delete_invoice'),
]
