from django.shortcuts import redirect, render
from django.contrib import messages
from .models import Ticket
from .forms import EmployeeForm, RegisterEquipmentForm, EquipmentForm, CategoryForm, TicketForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

# Create your views here.
@login_required
def dashboard(request):
    if request.user.department and request.user.department.name == 'IT Support':
        tickets = Ticket.objects.all().order_by('date_created')
    else:
        tickets = Ticket.objects.filter(author=request.user).order_by('date_created')
    
    return render(request, "dashboard.html", {"tickets": tickets})

def new_employee(request):
    if request.method == "POST":
        employee_form = EmployeeForm(request.POST)
        if employee_form.is_valid():
            employee_form.save()
            messages.success(request, 'Employee has been successfully added.')
            return redirect('dashboard')
    else:
        employee_form = EmployeeForm()
    
    return render(request, "tickets/new-employee.html", {"employee_form" : employee_form})

def new_equipment(request):
    if request.method == "POST":
        equipment_form = EquipmentForm(request.POST)
        if equipment_form.is_valid():
            equipment_form.save()
            messages.success(request, 'Equipment has been successfully added.')
            return redirect('dashboard')
    else:
        equipment_form = EquipmentForm()
    
    return render(request, "tickets/new-equipment.html", {"equipment_form" : equipment_form})

def new_category(request):
    if request.method == "POST":
        category_form = CategoryForm(request.POST)
        if category_form.is_valid():
            category_form.save()
            messages.success(request, 'Category has been successfully added.')
            return redirect('dashboard')
    else:
        category_form = CategoryForm()
    
    return render(request, "tickets/new-category.html", {"category_form" : category_form})

@login_required
def new_ticket(request):
    if request.method == "POST":
        ticket_form = TicketForm(request.POST)
        if ticket_form.is_valid():
            ticket = ticket_form.save(commit=False)
            ticket.author = request.user 
            ticket.save()
            
            return redirect('dashboard')
    else:
        ticket_form = TicketForm()
        
    return render(request, 'tickets/new-ticket.html', {'ticket_form': ticket_form})
    
def register_equipment(request):
    if request.method == "POST":
        register_equipment_form = RegisterEquipmentForm(request.POST)
        if register_equipment_form.is_valid():
            equipment = register_equipment_form.cleaned_data["equipments"]
            employee = register_equipment_form.cleaned_data["employees"]
            equipment.owner = employee
            equipment.save()
            messages.success(request, 'Equipment was successfully assigned to employee.')
            return redirect('dashboard')
    
    else:
        register_equipment_form = RegisterEquipmentForm()
        return render(request, "tickets/register-equipment.html", {"register_equipment_form" : register_equipment_form})
        