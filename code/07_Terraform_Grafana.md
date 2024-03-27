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
provider "aws" {
  region = "us-west-2"
}

resource "aws_instance" "ec2_instance" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t2.micro"
  key_name      = "my-key"

  tags = {
    Name = "EC2Instance"
  }

  provisioner "remote-exec" {
    inline = [
      "sudo snap install helm --classic",
      "helm repo add prometheus-community https://prometheus-community.github.io/helm-charts",
      "helm repo update",
      "kubectl create namespace monitoring",
      "helm install monitoring prometheus-community/kube-prometheus-stack -n monitoring",
      "kubectl apply -f ev3.yaml",
      "kubectl port-forward service/monitoring-kube-prometheus-prometheus 9090:9090 -n monitoring",
      "kubectl port-forward service/monitoring-grafana 8080:80 -n monitoring"
    ]
  }
}
```
