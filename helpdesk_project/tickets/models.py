from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=100)
    office = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    class Meta:
        verbose_name = "Department"
        verbose_name_plural = "Departments"
    def __str__(self):
        return self.name

class Employee(AbstractUser):
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True)
    class Meta:
        verbose_name = "Employee"
        verbose_name_plural = "Employees"
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Equipment(models.Model):
    asset_tag = models.CharField(max_length=20, unique=True)
    equipment_type = models.CharField(max_length=50)
    owner = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True)
    class Meta:
        verbose_name = "Equipment"
        verbose_name_plural = "Equipment"
    def __str__(self):
        return f"{self.equipment_type} ({self.asset_tag})"

class Category(models.Model):
    name = models.CharField(max_length=50)
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
    def __str__(self):
         return self.name
        
    
class Ticket(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    is_resolved = models.BooleanField(default=False)
    author = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    class Meta:
        verbose_name = "Ticket"
        verbose_name_plural = "Tickets"
    def __str__(self):
        return self.title

class TicketComment(models.Model):
    body = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE) 
    author = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True)
    class Meta:
        verbose_name = "Ticket Comment"
        verbose_name_plural = "Ticket Comments"
    def __str__(self):
        return f"{self.author} on {self.ticket}: '{self.body[:30]}...'"
        