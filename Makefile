
# Define the virtual environment commands using pipenv
venv:
	python3.10 -m venv venv

activate:
	source venv/bin/activate

rm:
	rm -rf venv

install:
	pip install -r requirements.txt

start:
	python manage.py runserver 11001

migrate:
	python manage.py makemigrations
	python manage.py migrate

# Create a superuser for the Django admin panel
createsuperuser:
	python manage.py createsuperuser

# Run Django tests
test:
	python manage.py test

# Check for missing migrations
check:
	python manage.py check

# Collect static files
collectstatic:
	python manage.py collectstatic --noinput

# Create a new Django app (usage: make app name=app_name)
app:
	@[ -n "$(name)" ] || (echo "Error: Missing app name. Usage: make app name=your_app_name" && exit 1)
	python manage.py startapp $(name)

# Format the code using black
format:
	black .

# Lint the code using flake8
lint:
	flake8 .


.PHONY: venv rm activate install start migrate createsuperuser test check collectstatic app format lint clean
