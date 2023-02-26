.PHONY: backend
backend:
	kubectl apply -f authentication/kubernetes/namespace.yaml

	kubectl apply -f authentication/kubernetes/database/configmap.yaml
	kubectl apply -f authentication/kubernetes/database/service.yaml
	kubectl apply -f authentication/kubernetes/database/deploy.yaml

	kubectl apply -f authentication/kubernetes/app/service.yaml
	kubectl apply -f authentication/kubernetes/app/job.yaml
	kubectl apply -f authentication/kubernetes/app/deploy.yaml

.PHONY: frontend
frontend:
	kubectl apply -f web/kubernetes/namespace.yaml

	kubectl apply -f web/kubernetes/server/service.yaml
	kubectl apply -f web/kubernetes/server/router.yaml
	kubectl apply -f web/kubernetes/server/deploy.yaml

.PHONY: deploy
deploy: backend frontend

.PHONY: clean
clean:
	kubectl delete namespace frontend
	kubectl delete namespace backend