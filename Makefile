.PHONY: backend
backend:
	kubectl create -f authentication/kubernetes/namespace.yaml

	kubectl create -f authentication/kubernetes/database/configmap.yaml
	kubectl create -f authentication/kubernetes/database/service.yaml
	kubectl create -f authentication/kubernetes/database/deploy.yaml

	kubectl create -f authentication/kubernetes/app/service.yaml
	kubectl create -f authentication/kubernetes/app/job.yaml
	kubectl create -f authentication/kubernetes/app/deploy.yaml

.PHONY: frontend
frontend:
	kubectl create -f web/kubernetes/namespace.yaml

	kubectl create -f web/kubernetes/server/service.yaml
	kubectl create -f web/kubernetes/server/router.yaml
	kubectl create -f web/kubernetes/server/deploy.yaml

.PHONY: deploy
deploy: backend frontend

.PHONY: clean
clean:
	kubectl delete namespace frontend
	kubectl delete namespace backend