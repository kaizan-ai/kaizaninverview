.PHONY: start_local_web_worker
## start_local_web_worker: Start the local web worker in a shell
start_local_web_worker:
	celery --app=kaizaninterview worker --concurrency=1 -l info -Q celery


.PHONY: start_local_web_server
## start_local_web_server: Start the local web server in a shell
start_local_web_server:
	python manage.py runserver


.PHONY: format_all
## format_all: Format the codebase
format_all: sort_imports format


.PHONY: format
## format: Format the codebase
format: 
	black .


.PHONY: sort_imports
## sort_imports: Sort the module imports
sort_imports:
	isort .