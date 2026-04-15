# IT-Helpdesk-Ticketing-System
A system for employees in a company to report computer or software issues, and for IT staff to resolve them.

The 6 Models:

Department
	Name STRING
	Office STRING
	Location STRING

Employee: 
	Name STRING
	Job Title STRING
	Email STRING
	Department (FK)

Equipment: 
	Asset Tag 
	Type (e.g., Laptop, Monitor) 
	Owner (Employee FK)

Category: 
	Name (e.g., Hardware, Software, Network) STRING

Ticket: 
	Title STRING
	Description STRING
	Date Created DATE
	Is_Resolved BOOL
	Author (EMPLOYEE FK)
	Category (Category FK)

TicketComment: 
	Text STRING
	Date DATE
	Ticket (Ticket FK)
	Author (Employee FK).

The 6 Forms:
Add Employee, 
Register Equipment, 
Create Ticket, 
Add Comment to Ticket, 
Update Ticket Status,
Add Category.

The 12+ Views/Templates:
Home/Dashboard, 
Open Tickets List, 
Closed Tickets List, 
Ticket Detail (shows ticket info + comments), 
Create Ticket page, 
Employee List, 
Employee Detail (shows their equipment and tickets),
Equipment List, 
Add Employee page,
Add Equipment page,
Add Comment view,
Resolve Ticket view.
