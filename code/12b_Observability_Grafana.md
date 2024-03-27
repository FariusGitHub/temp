# Observability with Grafana

After Prometheus server was running, we can start Grafana server like below. </br>
Take a look at https://github.com/FariusGitHub/prometheus_grafana as this is exactly the same. </br>
Instead of using nginx.yaml for web app minitoring we use ev3.yaml for robotic application.

```txt
$ kubectl port-forward service/monitoring-grafana 8080:80 -n monitoring
  Forwarding from 127.0.0.1:8080 -> 3000
  Forwarding from [::1]:8080 -> 3000
  Handling connection for 8080
  Handling connection for 8080
```
