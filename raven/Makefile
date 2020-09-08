.PHONY: env shell lint test run wipedb migrations migrate requirements
.DEFAULT: env

env:
	@python -m venv .venv
	@poetry install

shell:
	@poetry run ./manage.py shell

lint:
	@poetry run black . --exclude migrations

test:
	@poetry run coverage run --branch ./manage.py test
	@poetry run coverage html

run:
	@poetry run ./manage.py runserver 0.0.0.0:8000

wipedb:
	@poetry run ./manage.py flush

migrations:
	@poetry run ./manage.py makemigrations

migrate:
	@poetry run ./manage.py migrate

requirements:
	@poetry show --no-dev | tr -s " " | sed 's/ /==/' | sed 's/ .*//' > requirements.txt