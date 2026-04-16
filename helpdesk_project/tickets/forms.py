from django import forms
from .models import Employee, Equipment


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        exclude=[]
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['department'].empty_label = "Please select a department"
        
class RegisterEquipmentForm(forms.Form):
    equipments = forms.ModelChoiceField(
        queryset= Equipment.objects.filter(owner__isnull=True),
        empty_label="Please select an unassigned equipment."
    )
    
    employees = forms.ModelChoiceField(
        queryset= Employee.objects.all(),
        empty_label="Please select an employee."
    )
