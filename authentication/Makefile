SERVICE=authentication
TAG=0.0.1
IMAGE=${SERVICE}:${TAG}
CONTAINER=${SERVICE}-container
PORT=5000
DOCKERHUB_USERNAME=cesarmerjan

.PHONY: backend-network
backend-network:
	docker network create -d bridge backend

.PHONY: build
build:
	docker build -t ${DOCKERHUB_USERNAME}/${IMAGE} -t ${DOCKERHUB_USERNAME}/${SERVICE}:latest .

.PHONY: container
container:
	docker create --hostname authentication-service --name ${CONTAINER} --network backend -p ${PORT}:${PORT} ${IMAGE}

.PHONY: clean
clean:
	docker rm ${CONTAINER}

.PHONY: start
start:
	docker start ${CONTAINER}

.PHONY: stop
stop:
	docker stop ${CONTAINER}

.PHONY: logs
logs:
	docker logs ${CONTAINER}

.PHONY: admin
admin:
	docker exec ${CONTAINER} flask user create Admin admin@gmail.com admin


.PHONY: database-start
database-start:
	docker run --rm --hostname authentication-database-service --name authentication-database-container --network backend -p 5432:5432 -e POSTGRES_DB=authentication -e POSTGRES_USER=user -e POSTGRES_PASSWORD=password -d postgres


.PHONY: database-stop
database-stop:
	docker stop authentication-database-container


.PHONY: debug
debug:
	kubectl run -it --image debian --namespace=backend debug


.PHONY: push-image
push-image:
	docker push ${DOCKERHUB_USERNAME}/${IMAGE}
	docker push ${DOCKERHUB_USERNAME}/${SERVICE}:latest
	