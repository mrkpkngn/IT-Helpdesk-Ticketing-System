"""
URL configuration for helpdesk_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from tickets import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('new-employee/', views.new_employee, name="new_employee"),
    path('new-equipment.', views.new_equipment, name="new_equipment"),
    path('new-category/', views.new_category, name="new_category"),
    path('new-ticket/', views.new_ticket, name="new_ticket"),
    path('register-equipment/', views.register_equipment, name="register_equipment"),
    path('tickets/<int:id>/', views.ticket_details, name="ticket_details"),
    path('tickets/<int:id>/ticket-status/', views.ticket_status, name="ticket_status"),
    path('tickets/<int:id>/add-comment/', views.add_comment, name="add_comment"),
    path('accounts/', include('django.contrib.auth.urls')), 
    path('inventory/', views.inventory, name="inventory"),
    path('employees/', views.employee_list, name="employee_list"),
    path('employees/<int:id>', views.employee_details, name="employee_details"),
]
