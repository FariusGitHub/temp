# Prometheus Terminal

This is an example of Prometheus terminal needed to run Grafana.</br>
Leave it open and open another new terminal for Grafana for visualization.

```txt
$ sudo snap install helm --classic
  helm 3.14.2 from Snapcrafters✪ installed

$ helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
  "prometheus-community" has been added to your repositories

$ helm repo update
  Hang tight while we grab the latest from your chart repositories...
  ...Successfully got an update from the "prometheus-community" chart repository
  Update Complete. ⎈Happy Helming!⎈

$ kubectl create namespace monitoring
  namespace/monitoring created

$ kubectl get nodes
  NAME             STATUS   ROLES           AGE   VERSION
  docker-desktop   Ready    control-plane   9d    v1.29.1

$ kubectl get ns
  NAME              STATUS   AGE
  default           Active   9d
  kube-node-lease   Active   9d
  kube-public       Active   9d
  kube-system       Active   9d
  monitoring        Active   43m

$ helm install monitoring prometheus-community/kube-prometheus-stack -n monitoring
  Error: INSTALLATION FAILED: cannot re-use a name that is still in use

$ helm uninstall monitoring -n monitoring
  release "monitoring" uninstalled

$ helm install monitoring prometheus-community/kube-prometheus-stack -n monitoring
  NAME: monitoring
  LAST DEPLOYED: Tue Mar 26 18:00:46 2024
  NAMESPACE: monitoring
  STATUS: deployed
  REVISION: 1
  NOTES:
  kube-prometheus-stack has been installed. Check its status by running:
    kubectl --namespace monitoring get pods -l "release=monitoring"

  Visit https://github.com/prometheus-operator/kube-prometheus for instructions on how to create & configure Alertmanager and Prometheus instances using the Operator.

$ kubectl apply -f ev3.yaml
  deployment.apps/ev3-deployment created

$ kubectl port-forward service/monitoring-kube-prometheus-prometheus 9090:9090 -n monitoring
  Forwarding from 127.0.0.1:9090 -> 9090
  Forwarding from [::1]:9090 -> 9090
```
