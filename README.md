Before you begin, ensure you have met the following requirements:

- [Python](https://www.python.org/downloads/) (at least Python 3.x)
- [Pip](https://pip.pypa.io/en/stable/installation/)



1-Create a virtual environment:
	python -m venv venv

2-Activate the virtual environment:
	On Windows:
		venv\Scripts\activate

	On macOS and Linux:
		source venv/bin/activate
	
3-Install the project dependencies:
	pip install -r requirements.txt

4-Apply database migrations:
	python manage.py makemigrations
	python manage.py migrate

5-Creating a Superuser
	To create a superuser with the username "admin" and password "admin," follow these steps:
	In your project directory, run the following command:
		python manage.py createsuperuser
	Enter the following details when prompted:
	Username: admin
	Email address: [your-email@example.com]
	Password: admin (or any other password of your choice)
	The superuser will be created and can be used to log in to the Django admin site.


Start the development server:
		python manage.py runserver


The API docs will be available at:
 		http://127.0.0.1:8000/docs/	


