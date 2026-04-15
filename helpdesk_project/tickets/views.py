from django.shortcuts import redirect, render
from django.contrib import messages
from django import forms
from .forms import EmployeeForm

# Create your views here.
def index(request):
    return render(request, "index.html")

def success(request, success_message):
    return render(request, "success.html", {"success_message" : success_message})

def new_employee(request):
    if request.method == "POST":
        employee_form = EmployeeForm(request.POST)
        if employee_form.is_valid():
            employee_form.save()
            messages.success(request, 'Employee has been successfully added.')
            return redirect('index')
    else:
        employee_form = EmployeeForm()
    
    return render(request, "tickets/new-employee.html", {"employee_form" : employee_form})
    