minikube start
eval $(minikube docker-env)
kubectl create configmap sql-commands --from-file=src/sql/init.sql
docker build -t spfinance .
kubectl apply -f deployment.yml