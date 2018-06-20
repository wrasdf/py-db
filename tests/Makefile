.PHONY: build run

build:
	docker build -t py-db:latest .

run: build
	docker run --rm py-db:latest python -m unittest ut/connect.py
