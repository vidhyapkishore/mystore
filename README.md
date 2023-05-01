# MyStore - An E-commerce Web Application

MyStore is an e-commerce web application built with React, Redux, and Django.

## Features

- User authentication and registration
- Browse and search for products
- View product details, images, and reviews
- Add products to a cart and checkout
- View order history and order details
- Admin panel to manage products, orders, and customers
- Product search functionality
- Pagination for products

## Installation

1. Clone the repository:
git clone https://github.com/vidhyapkishore/mystore.git

2. Install the required packages:

pip install -r requirements.txt


3. Create the database:

python manage.py migrate


4. Create a superuser account:

python manage.py createsuperuser

5. Load the initial data:

python manage.py loaddata fixtures/*

6. Run the development server:

python manage.py runserver
7. Open `http://localhost:8000/` in a web browser to access the application.

## Technologies Used

- React
- Redux
- Django
- PostgreSQL
- Bootstrap
- Django REST Framework

## Credits

This project was created by Vidhya PK as part of a coding challenge.
