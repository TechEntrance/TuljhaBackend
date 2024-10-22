# Tuljha/urls.py (or my_project/urls.py)
from django.contrib import admin
from django.urls import path, include
from Dashboard import views  # Import the views from your app (replace 'my_app' with your app name)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),  # Map the root URL to the 'index' view in your app
    path('Dashboard/', include('Dashboard.urls')),  # Example of including other app URLs
]
