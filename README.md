# Univail Sales Inventory System

## Overview
Univail Sales Inventory System is a comprehensive Django-based application designed to streamline inventory management and sales operations for businesses. This system provides real-time tracking of inventory levels, sales analytics, and automated reporting.

## Features
- **Inventory Management**: Track stock levels, product details, and automate reordering
- **Sales Processing**: Handle transactions, generate invoices, and manage customer data
- **User Management**: Role-based access control for administrators, managers, and staff
- **Analytics Dashboard**: Visual representation of sales trends and inventory status
- **Reporting**: Generate detailed reports on sales, inventory, and profitability

## Technology Stack
- Django 4.2+
- Python 3.9+
- PostgreSQL
- Bootstrap 5
- Django REST Framework (for API endpoints)

## Installation

1. Clone the repository
```bash
git clone https://github.com/yourusername/univail-sales-inventory.git
cd univail-sales-inventory
```

2. Create a virtual environment and activate it
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Configure database settings in `settings.py`

5. Run migrations
```bash
python manage.py migrate
```

6. Create a superuser
```bash
python manage.py createsuperuser
```

7. Run the development server
```bash
python manage.py runserver
```

## Usage
Access the admin interface at `http://localhost:8000/admin/` to configure initial settings and manage data.

Access the main application at `http://localhost:8000/` to start using the inventory system.

## License
MIT License

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
