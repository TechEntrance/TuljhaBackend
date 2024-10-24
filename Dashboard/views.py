# Dashboard/views.py
from django.shortcuts import render, redirect
from .models import Organization, FoodOrder, Invoice, Expense
from django.contrib import messages
from django.db.models import Sum

def index(request):
    # Fetch data for charts
    organizations_count = Organization.objects.count()
    food_orders_count = FoodOrder.objects.count()
    expenses_total = Expense.objects.aggregate(Sum('amount'))['amount__sum'] or 0
    invoices_total = Invoice.objects.aggregate(Sum('total_amount'))['total_amount__sum'] or 0

    return render(request, 'index.html', {
        'organizations_count': organizations_count,
        'food_orders_count': food_orders_count,
        'expenses_total': expenses_total,
        'invoices_total': invoices_total,
    })

# View for organizations page
def organization(request):
    if request.method == 'POST':
        name = request.POST['name']
        contact_person = request.POST['contact_person']
        email = request.POST['email']
        Organization.objects.create(name=name, contact_person=contact_person, email=email)
        messages.success(request, "Organization added successfully!")
        return redirect('organization')

    organizations = Organization.objects.all()
    return render(request, 'organization.html', {'organizations': organizations})

# View for the food orders page
def food_order_view(request):
    if request.method == 'POST':
        organization_id = request.POST['organization']
        people_served = request.POST['people_served']
        food_items = request.POST['food_items']
        total_cost = request.POST['total_cost']
        FoodOrder.objects.create(
            organization_id=organization_id,
            people_served=people_served,
            food_items=food_items,
            total_cost=total_cost
        )
        messages.success(request, "Food order added successfully!")
        return redirect('food-order')

    organizations = Organization.objects.all()
    return render(request, 'food_order.html', {'organizations': organizations})

# View for invoicing page
def invoicing_view(request):
    invoices = Invoice.objects.all()
    return render(request, 'invoicing.html', {'invoices': invoices})

# View for expense page
def expense_view(request):
    if request.method == 'POST':
        category = request.POST.get('category')
        amount = request.POST.get('amount')
        date = request.POST.get('date')
        # Ensure to set the user when creating the expense
        Expense.objects.create(
            user=request.user,  # Add this line
            category=category,
            amount=amount,
            date=date
        )
        return redirect('expense')  # Redirect after successful creation
    # Handle GET request and render the template
    return render(request, 'expense.html', {'expenses': Expense.objects.all()})

# View for reports page
def reports(request):
    return render(request, 'reports.html')

# View for profile settings page
def profile(request):
    return render(request, 'profile.html')
