#!make
include .env

dcollect:
	docker-compose exec web python manage.py collectstatic
dtest:
	docker-compose exec web python manage.py test


dmigr:
	docker-compose exec web python manage.py makemigrations && docker-compose exec web python manage.py migrate
duser:
	docker-compose exec web python manage.py createsuperuser
dshell:
	docker-compose exec web python manage.py shell

dloaddump:
	docker-compose exec web python manage.py loaddata db.json
dcreatedump:
	docker-compose exec web python manage.py dumpdata > core/db.json