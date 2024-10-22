from django.db import models
from django.contrib.auth.models import User

# User model is handled by Django's built-in auth system

# Organization model
class Organization(models.Model):
    name = models.CharField(max_length=255)  # Organization name
    contact_email = models.EmailField()  # Contact email
    phone_number = models.CharField(max_length=15)  # Phone number
    address = models.TextField()  # Organization address

    def __str__(self):
        return self.name


# Expense model
class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # The user who made the expense
    category = models.CharField(max_length=100)  # Category of the expense (e.g., Utilities, Maintenance)
    amount = models.DecimalField(max_digits=10, decimal_places=2)  # Amount of the expense
    date = models.DateField()  # Date of the expense
    description = models.TextField(blank=True, null=True)  # Optional description

    def __str__(self):
        return f"{self.category} - {self.amount} by {self.user.username}"

    class Meta:
        ordering = ['-date']  # Order expenses by date (most recent first)


# FoodOrder model
class FoodOrder(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)  # The organization placing the order
    people_served = models.IntegerField()  # Number of people served
    food_items = models.TextField()  # Comma-separated string of food items
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)  # Total cost of the order
    date = models.DateField()  # Date of the order
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # The user managing the order

    def __str__(self):
        return f"Order for {self.organization.name} - {self.total_cost}"


# Invoice model
class Invoice(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)  # The organization being invoiced
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)  # Total amount of the invoice
    status = models.CharField(max_length=50, choices=[('paid', 'Paid'), ('pending', 'Pending'), ('unpaid', 'Unpaid')])  # Status of the invoice
    date = models.DateField(auto_now_add=True)  # Automatically sets the date when the invoice is created
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)


    def __str__(self):
        return f"Invoice for {self.organization.name} - {self.total_amount} ({self.status})"


# Optional: if you want to track user sessions, Django's built-in session handling can be used
