clean:
	find . -name "*.pyc" -exec rm -f {} \;
	find . -name "*.pyo" -exec rm -f {} \;
	find . -name "*.py[co]" -o -name __pycache__ -exec rm -rf {} +

down:
	docker-compose down

up: 
	docker-compose down
	docker-compose up -d

build:
	docker-compose build --force-rm --progress string
