up:
	docker-compose up --build

down:
	docker-compose down -v

test:
	docker-compose run --rm web sh -c "cd src && pytest -vv -s"