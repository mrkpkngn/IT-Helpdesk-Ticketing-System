# IT Helpdesk Ticketing System
A comprehensive Django-based system for managing IT support tickets. Employees can report computer or software issues, and IT staff can track, update, and resolve them efficiently.

## Features
- **Employee Management**: Add and manage company employees across departments
- **Equipment Tracking**: Register and track company equipment (laptops, monitors, etc.)
- **Ticket Management**: Create, view, and manage IT support tickets
- **Ticket Comments**: Add comments and updates to tickets for collaboration
- **Category Organization**: Organize tickets by category (Hardware, Software, Network, etc.)
- **Role-Based Access**: Separate views and permissions for IT staff and regular employees
- **User Authentication**: Secure login system with Django's built-in auth

## Project Structure

```
helpdesk_project/          # Main Django project
├── helpdesk_project/      # Project settings and configuration
├── tickets/               # Main application (models, views, forms)
├── templates/             # HTML templates
├── static/                # CSS, JavaScript, and static assets
├── manage.py              # Django management script
├── db.sqlite3             # SQLite database
└── package.json           # Node.js dependencies (Tailwind CSS)
```

## Data Models

- **Department**: Company departments with office and location information
- **Employee**: Employee records linked to departments
- **Equipment**: Registered company equipment (laptops, monitors, etc.)
- **Category**: Ticket categories (Hardware, Software, Network, etc.)
- **Ticket**: Support tickets with title, description, status, and assignment
- **TicketComment**: Comments and updates on tickets for collaboration

## Prerequisites

- Python 3.8 or higher
- pip or uv (Python package manager)
- Node.js 14+ (for Tailwind CSS)

## Installation

### Option 1: Using `uv` (Recommended)

1. **Clone the repository**
   ```bash
   cd IT-Helpdesk-Ticketing-System
   ```

2. **Create and activate virtual environment**
   ```bash
   uv venv
   # On Windows:
   .\.venv\Scripts\activate
   # On macOS/Linux:
   source .venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   uv pip install -r requirements.txt
   ```

4. **Install Node.js dependencies**
   ```bash
   npm install
   ```

### Option 2: Using pip and venv

1. **Clone the repository**
   ```bash
   cd IT-Helpdesk-Ticketing-System
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv venv
   # On Windows:
   .\venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Install Node.js dependencies**
   ```bash
   npm install
   ```

## Getting Started

1. **Navigate to the project directory**
   ```bash
   cd helpdesk_project
   ```

2. **Apply database migrations**
   ```bash
   python manage.py migrate
   ```

3. **Create a superuser (admin account)**
   ```bash
   python manage.py createsuperuser
   ```

4. **Load initial data** (optional)
   ```bash
   python manage.py loaddata initial_data
   ```

5. **Compile Tailwind CSS** (in a separate terminal)
   ```bash
   npm run dev
   ```

6. **Start the development server**
   ```bash
   python manage.py runserver
   ```

7. **Access the application**
   - Application: http://localhost:8000
   - Admin panel: http://localhost:8000/admin

## Usage

### For Employees
- Log in with your employee credentials
- Create new support tickets for issues
- Add comments and updates to your tickets
- View ticket status and resolution updates

### For IT Staff
- Log in with IT department credentials
- View all open and closed tickets
- Update ticket status and add resolution comments
- Manage employee and equipment information

## Development


### Creating Migrations
```bash
python manage.py makemigrations
```

### Running Management Commands
```bash
python manage.py shell
```

## Troubleshooting
### Virtual environment not activating
- Ensure you're in the project root directory
- Try using absolute paths to the activation script

### Database errors
- Delete `db.sqlite3` and run migrations again: `python manage.py migrate`
- Check that all migrations are applied: `python manage.py showmigrations`

## License
This project is provided as-is for educational and internal use.
