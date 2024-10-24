from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

# Organization model
class Organization(models.Model):
    name = models.CharField(max_length=255)  # Organization name
    contact_person = models.CharField(max_length=255, null=True)  # Make this field nullable
    email = models.EmailField(null=True)  # Make this field nullable
    address = models.TextField()  # Organization address
    contact_email = models.EmailField()  # Contact email

    def __str__(self):
        return self.name


# Expense model
class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Ensure this line exists
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
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=[('Paid', 'Paid'), ('Unpaid', 'Unpaid')])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Invoice for {self.organization.name} - {self.total_amount}"

class FoodOrder(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    people_served = models.IntegerField()
    food_items = models.TextField()  # Store food items as a string
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)
    order_date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # Create the food order
        super().save(*args, **kwargs)
        # Create an invoice for the food order
        Invoice.objects.create(
            organization=self.organization,
            total_amount=self.total_cost,
            status='Unpaid'  # Default status
        )
