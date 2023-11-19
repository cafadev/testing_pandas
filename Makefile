install:
	./setup-dev.sh
up:
	docker-compose up -d

stop:
	docker-compose stop

restart:
	docker-compose restart

shell: up
	docker-compose exec app bash

prod:
	gunicorn src.wsgi:application --reload --bind 0.0.0.0:9000

dev:
	python manage.py runserver 0.0.0.0:9000

makemigrations:
	python manage.py makemigrations

migrate:
	python manage.py migrate

db-update:
	python manage.py makemigrations && python manage.py migrate

.PHONY: up down restart shell runserver makemigrations migrate db-update
