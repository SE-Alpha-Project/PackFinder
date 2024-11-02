Installation
===========

Prerequisites
------------
* Python 3.11+
* Django 4.1.1
* Other dependencies listed in requirements.txt

Setup
-----
1. Clone the repository::

    git clone https://github.com/yourusername/PackFinder.git
    cd PackFinder

2. Create a virtual environment::

    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install dependencies::

    pip install -r requirements.txt

4. Run migrations::

    python manage.py migrate

5. Create a superuser::

    python manage.py createsuperuser

6. Run the development server::

    python manage.py runserver 