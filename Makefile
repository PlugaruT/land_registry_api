help:
	@echo "install"
	@echo "   Install project dependencies."
	@echo "test"
	@echo "   Run tests."
	@echo "run"
	@echo "   Run local development server."
	@echo "lint"
	@echo "   Run project linters and autoformatters."


install:
	pip install -r requirements.txt

test:
	python manage.py test
	
run:
	python manage.py runserver

lint:
	black .