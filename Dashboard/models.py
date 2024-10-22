from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

# Organization model
class Organization(models.Model):
    name = models.CharField(max_length=255)  # Organization name
    address = models.TextField()  # Organization address
    contact_email = models.EmailField()  # Contact email

    def __str__(self):
        return self.name


# Expense model
class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # The user who made the expense
    organization = models.ForeignKey(Organization, null=True, blank=True, on_delete=models.SET_NULL)  # Optional, organization linked to the expense
    category = models.CharField(max_length=100)  # Category of the expense
    amount = models.DecimalField(max_digits=10, decimal_places=2)  # Amount of the expense
    date = models.DateField()  # Date of the expense
    description = models.TextField(blank=True, null=True)  # Optional description

    def __str__(self):
        return f"{self.category} - {self.amount} by {self.user.username}"

    class Meta:
        ordering = ['-date']  # Order expenses by date (most recent first)

User = get_user_model()

class Invoice(models.Model):
    organization = models.CharField(max_length=255)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50, choices=[('paid', 'Paid'), ('unpaid', 'Unpaid')])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Invoice {self.invoice_number} - {self.organization.name}"
