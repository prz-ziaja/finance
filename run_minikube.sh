minikube start
eval $(minikube docker-env)
docker build -t spfinance .
kubectl apply -f deployment.yml