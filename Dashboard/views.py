# Dashboard/views.py
from django.shortcuts import render, redirect
from .models import Organization, Expense, Invoice  # Correct import
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
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
                return redirect('index')  # Redirecting to the main index page
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
                    return redirect('index')  # Redirecting to the main index page
                except Exception as e:
                    return render(request, 'auth.html', {'error': 'Username or email already exists', 'mode': 'signup'})
            else:
                return render(request, 'auth.html', {'error': 'Passwords do not match', 'mode': 'signup'})

    mode = request.GET.get('mode', 'login')
    return render(request, 'auth.html', {'mode': mode})

@login_required
def index(request):
    return render(request, 'index.html')  # Render your index.html

# View for organizations page
def organization(request):
    return render(request, 'organization.html')

# Rename this function to food_order
# View for the food orders page
def food_order_view(request):
    organizations = Organization.objects.all()  # Fetch all organizations
    if request.method == 'POST':
        # Process the submitted form data here
        pass

    return render(request, 'food_order.html', {'organizations': organizations})
# View for invoicing page
def invoicing_view(request):
    invoices = Invoice.objects.all()  # Fetch all invoices
    return render(request, 'invoicing.html', {
        'invoices': invoices,
        'user': request.user  # Pass the user object for personalization
    })

# View for expense page
# @login_required  # This decorator will redirect unauthenticated users to the login page
@login_required  # Ensure only authenticated users can access this view
def expense_view(request):
    expenses = Expense.objects.filter(user=request.user)
    return render(request, 'expense.html', {'expenses': expenses})

# View for reports page
def reports(request):
    return render(request, 'reports.html')

# View for profile settings page
def profile(request):
    return render(request, 'profile.html')
