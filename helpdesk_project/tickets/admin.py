from django.contrib import admin
from .models import Department, Employee, Equipment, Category, Ticket, TicketComment

# Register your models here.
admin.site.register(Department)
admin.site.register(Employee)
admin.site.register(Equipment)
admin.site.register(Category)
admin.site.register(Ticket)
admin.site.register(TicketComment)