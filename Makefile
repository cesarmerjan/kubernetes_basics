.PHONY: backend-network
backend-network:
	docker network create -d bridge backend

.PHONY: frontend-network
frontend-network:
	docker network create -d bridge frontend

.PHONY: web-server
web-server:
	minikube service --url --namespace=frontend web-server-service