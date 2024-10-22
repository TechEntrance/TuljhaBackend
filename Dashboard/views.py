from django.shortcuts import render, redirect
from .models import Organization, Expense, Invoice, FoodOrder
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

def auth_view(request):
    if request.method == 'POST':
        if 'login' in request.POST:
            email = request.POST.get('email')
            password = request.POST.get('password')
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')  # Redirect to main index page
            else:
                return render(request, 'auth.html', {'error': 'Invalid credentials', 'mode': 'login'})

        elif 'signup' in request.POST:
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            confirm_password = request.POST.get('confirm_password')

            if password == confirm_password:
                try:
                    user = User.objects.create_user(username=username, email=email, password=password)
                    user.save()
                    login(request, user)
                    return redirect('index')  # Redirect to main index page
                except Exception as e:
                    return render(request, 'auth.html', {'error': 'Username or email already exists', 'mode': 'signup'})
            else:
                return render(request, 'auth.html', {'error': 'Passwords do not match', 'mode': 'signup'})

    mode = request.GET.get('mode', 'login')
    return render(request, 'auth.html', {'mode': mode})

@login_required
def index(request):
    return render(request, 'index.html')  # Render index.html
@login_required
def organization(request):
    if request.method == 'POST':
        org_name = request.POST.get('org_name')
        contact_person = request.POST.get('contact_person')
        contact_email = request.POST.get('contact_email')

        # Create and save the organization instance
        organization = Organization(
            name=org_name,
            contact_email=contact_email,
            # Assuming 'phone_number' and 'address' are also required; you may want to add these fields to the form.
            phone_number=request.POST.get('phone_number', ''),  # Add this field to your form
            address=request.POST.get('address', '')  # Add this field to your form
        )
        organization.save()  # Save the organization instance to the database
        return redirect('organization')  # Redirect to the organization page or any other page

    # Fetch all organizations to display in the table
    organizations = Organization.objects.all()
    return render(request, 'organization.html', {'organizations': organizations})

@login_required
def food_order_view(request):
    organizations = Organization.objects.all()  # Fetch all organizations
    if request.method == 'POST':
        # Process the submitted food order data
        organization_id = request.POST.get('organization')
        food_items = request.POST.get('food_items')
        people_served = request.POST.get('people_served')
        total_cost = request.POST.get('total_cost')
        organization = Organization.objects.get(id=organization_id)
        
        FoodOrder.objects.create(
            organization=organization,
            people_served=people_served,
            food_items=food_items,
            total_cost=total_cost,
            user=request.user
        )
        return redirect('food-order')

    return render(request, 'food_order.html', {'organizations': organizations})

@login_required
def invoicing_view(request):
    invoices = Invoice.objects.all()  # Fetch all invoices
    return render(request, 'invoicing.html', {
        'invoices': invoices,
        'user': request.user
    })

@login_required
def expense_view(request):
    expenses = Expense.objects.filter(user=request.user)  # Fetch user's expenses
    return render(request, 'expense.html', {'expenses': expenses})

@login_required
def reports(request):
    return render(request, 'reports.html')

@login_required
def profile(request):
    return render(request, 'profile.html')
