run:
	python3 manage.py runserver
migrations:
	python3 manage.py makemigrations
migrate:
	python3 manage.py migrate
admin:
	python3 manage.py createsuperuser
virtual:
	source venv/bin/activate
celery:
	celery -A config worker -l info