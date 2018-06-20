.PHONY: mysql postgres clean tests

mysql:
	cd mysql && docker-compose up

postgres:
	cd postgres && docker-compose up

tests:
	cd tests && make run

clean:
	docker stop $$(docker ps -aq)
	docker rm $$(docker ps -qa --no-trunc --filter "status=exited")
	docker volume rm $$(docker volume ls -qf dangling=true)
	docker network rm $$(docker network ls | grep "bridge" | awk '/ / { print $1 }')
