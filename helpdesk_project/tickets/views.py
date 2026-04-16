from django.shortcuts import redirect, render
from django.contrib import messages
from django import forms
from .forms import EmployeeForm, RegisterEquipmentForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def dashboard(request):
    return render(request, "dashboard.html")

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
    
def register_equipment(request):
    if request.method == "POST":
        register_equipment_form = RegisterEquipmentForm(request.POST)
        if register_equipment_form.is_valid():
            equipment = register_equipment_form.cleaned_data["equipments"]
            employee = register_equipment_form.cleaned_data["employees"]
            equipment.owner = employee
            equipment.save()
            messages.success(request, 'Equipment was successfully assigned to employee.')
            return redirect('index')
    
    else:
        register_equipment_form = RegisterEquipmentForm()
        return render(request, "tickets/register-equipment.html", {"register_equipment_form" : register_equipment_form})
        