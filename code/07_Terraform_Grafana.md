# Infrastructure-as-Code Prometheus and Grafana
```txt
$ sudo snap install helm --classic
$ helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
$ helm repo update
$ kubectl create namespace monitoring
$ helm install monitoring prometheus-community/kube-prometheus-stack -n monitoring
$ kubectl apply -f ev3.yaml
$ kubectl port-forward service/monitoring-kube-prometheus-prometheus 9090:9090 -n monitoring
$ kubectl port-forward service/monitoring-grafana 8080:80 -n monitoring
```
## TERRAFORM CODE

```txt
$ sudo snap install helm --classic
$ helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
$ helm repo update
$ kubectl create namespace monitoring
$ helm install monitoring prometheus-community/kube-prometheus-stack -n monitoring
$ kubectl apply -f ev3.yaml
$ kubectl port-forward service/monitoring-kube-prometheus-prometheus 9090:9090 -n monitoring

$ kubectl port-forward service/monitoring-grafana 8080:80 -n monitoring
```
