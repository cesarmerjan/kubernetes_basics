SERVICE=web-server
TAG=0.0.3
IMAGE=${SERVICE}:${TAG}
CONTAINER=${SERVICE}-container
PORT=80
DOCKERHUB_USERNAME=cesarmerjan

.PHONY: frontend-network
frontend-network:
	docker network create -d bridge frontend


.PHONY: build
build:
	docker build -t ${DOCKERHUB_USERNAME}/${IMAGE} -t ${DOCKERHUB_USERNAME}/${SERVICE}:latest .

.PHONY: container
container:
	docker create --name ${CONTAINER} -p ${PORT}:${PORT} ${IMAGE}

.PHONY: clean
clean:
	docker rm ${CONTAINER}

.PHONY: start
start:
	docker network connect frontend ${CONTAINER}
	docker network connect backend ${CONTAINER}
	docker start ${CONTAINER}

.PHONY: stop
stop:
	docker stop ${CONTAINER}

.PHONY: logs
logs:
	docker logs ${CONTAINER}


.PHONY: debug
debug:
	kubectl run -it --image debian --namespace=frontend debug


.PHONY: push-image
push-image:
	docker push ${DOCKERHUB_USERNAME}/${IMAGE}
	docker push ${DOCKERHUB_USERNAME}/${SERVICE}:latest


.PHONY: web-server-url
web-server-url:
	minikube service --url --namespace=frontend web-server-service
	