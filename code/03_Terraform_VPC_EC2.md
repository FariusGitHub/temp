# Infrastructure-as-Code to setup VPC, Subnet, Peering Connection, Internet Gateway, Route Table, Security Group, Network Interface, Elastic IP, EC2 

Setting up Cloud infrastructure with CLI (bash commands) or terraform would be something every DevOps engineer is passionate about.
I wrote few article about this using multiple tools such as 
- [Terraform](https://medium.com/p/23f568a31353/edit)
- [Ansible](https://medium.com/p/a8e6bf45eeb2/edit)
- [Chef](https://github.com/FariusGitHub/chef-ec2)

Herewith couple example of setting up cloud infrastructure.
Ideally this project using AWS EC2 as master node and Raspberry Pi as worker nodes.
We could also try to use local computer as master node and keep Raspberry Pi as worker nodes to experiment.

## example of EC2 with Ansible
```tf
#DEVELOP AWS RESOURCE WITH ANSIBLE
- name: Develop AWS Resources
  hosts: localhost
  vars:
    aws_access_key: "..."
    aws_secret_key: "..."

  tasks:
    - name: Create VPC
      amazon.aws.ec2_vpc_net:
        aws_access_key: "{{ aws_access_key }}"
        aws_secret_key: "{{ aws_secret_key }}"
        region: us-east-1
        cidr_block: 10.2.0.0/16
        name: vpc-project2
        tags:
          Name: vpc-project2
      register: vpc_project2

    - name: Create Public Subnet
      ec2_vpc_subnet:
        vpc_id: "{{ vpc_project2.vpc.id }}"
        cidr: 10.2.254.0/24
        region: us-east-1
        aws_access_key: "{{ aws_access_key }}"
        aws_secret_key: "{{ aws_secret_key }}"
        tags:
          Name: pub-subnet
      register: pub_subnet

    - name: Create Private Subnet
      ec2_vpc_subnet:
        vpc_id: "{{ vpc_project2.vpc.id }}"
        cidr: 10.2.2.0/24
        region: us-east-1
        aws_access_key: "{{ aws_access_key }}"
        aws_secret_key: "{{ aws_secret_key }}"
        tags:
          Name: prv-subnet
      register: prv_subnet

    - name: Create AWS Internet Gateway
      ec2_vpc_igw:
        aws_access_key: "{{ aws_access_key }}"
        aws_secret_key: "{{ aws_secret_key }}"
        region: us-east-1
        vpc_id: "{{ vpc_project2.vpc.id }}"
        tags:
          Name: "igw-vpc-project2"
      register: igw_vpc_project2      

    - name: Set route table
      amazon.aws.ec2_vpc_route_table:
        aws_access_key: "{{ aws_access_key }}"
        aws_secret_key: "{{ aws_secret_key }}"
        vpc_id: "{{ vpc_project2.vpc.id }}"
        region: us-east-1
        tags:
          Name: rt-pub-project2
        subnets:
          - "{{ pub_subnet.subnet.id }}"
        routes:
          - dest: 0.0.0.0/0
            gateway_id: "{{ igw_vpc_project2.gateway_id }}"
          - dest: ::/0
            gateway_id: "{{ igw_vpc_project2.gateway_id }}"
      register: rt_pub_project2

    - name: security group
      amazon.aws.ec2_security_group:
        name: sg_api_project2
        description: sg_api_project2
        aws_access_key: "{{ aws_access_key }}"
        aws_secret_key: "{{ aws_secret_key }}"
        region: us-east-1
        vpc_id: "{{ vpc_project2.vpc.id }}"
        rules:
          - proto: "tcp"
            from_port: 80
            to_port: 80
            cidr_ip: 0.0.0.0/0
          - proto: "tcp"
            from_port: 443
            to_port: 443
            cidr_ip: 0.0.0.0/0            
          - proto: "tcp"
            from_port: 22
            to_port: 22
            cidr_ip: 0.0.0.0/0
          - proto: "tcp"
            from_port: 3306
            to_port: 3306
            cidr_ip: 0.0.0.0/0
          - proto: "tcp"
            from_port: 5432
            to_port: 5432
            cidr_ip: 0.0.0.0/0
        rules_egress:
          - proto: "-1"
            from_port: 0
            to_port: 0
            cidr_ip: 0.0.0.0/0
        tags:
          Name: sg_api_project2
      register: sg_api_project2

    - name: security group
      amazon.aws.ec2_security_group:
        name: sg_pdb_project2
        description: sg_pdb_project2
        aws_access_key: "{{ aws_access_key }}"
        aws_secret_key: "{{ aws_secret_key }}"
        region: us-east-1
        vpc_id: "{{ vpc_project2.vpc.id }}"
        rules:
          - proto: "-1"
            from_port: 0
            to_port: 0
            cidr_ip: 0.0.0.0/0
        rules_egress:
          - proto: "-1"
            from_port: 0
            to_port: 0
            cidr_ip: 0.0.0.0/0
        tags:
          Name: sg_pdb_project2
      register: sg_pdb_project2

    - name: start database instance with no public IP address
      amazon.aws.ec2_instance:
        aws_access_key: "{{ aws_access_key }}"
        aws_secret_key: "{{ aws_secret_key }}"
        region: us-east-1
        key_name: "wcd-projects"
        vpc_subnet_id: "{{ prv_subnet.subnet.id }}"
        instance_type: t2.micro
        security_group: "{{ sg_pdb_project2.group_id }}"
        network:
          assign_public_ip: false
        user_data: "{{ lookup('file', 'dbinstall.txt') }}"
        image_id: ami-0fc5d935ebf8bc3bc
        name: PRIVATEDB
        tags:
          Environment: PRIVATEDB
      register: PRIVATEDB

    - name: create launch template
      community.aws.ec2_launch_template:
        name: EC2_template_project2
        image_id: ami-0fc5d935ebf8bc3bc
        key_name: wcd-projects
        instance_type: t2.micro
        aws_access_key: "{{ aws_access_key }}"
        aws_secret_key: "{{ aws_secret_key }}"
        region: us-east-1
        network_interfaces:
          - associate_public_ip_address: true
            subnet_id: "{{ pub_subnet.subnet.id }}"
        user_data: "{{ lookup('file', 'apiinstall.sh') | b64encode }}"
      register: EC2_template_project2

    - amazon.aws.autoscaling_group:
        name: AutoScaled_API_project2
        health_check_type: ELB
        aws_access_key: "{{ aws_access_key }}"
        aws_secret_key: "{{ aws_secret_key }}"
        region: us-east-1        
        launch_template:
            version: '1'
            launch_template_name: 'EC2_template_project2'
        min_size: 2
        max_size: 2
        desired_capacity: 2
        vpc_zone_identifier: [ "{{ pub_subnet.subnet.id }}"]
        tags:
         -  key: Name
            value: PUB_API
            propagate_at_launch: true

```

## Example of Azure VM setup with Terraform

```txt
terraform {
  required_providers {
    azurerm = {
      source = "hashicorp/azurerm"
      version = "2.93.0"
    }
  }
}
provider "azurerm" {
  features {}
}
locals {
  resource_group="app-grp"
  location="eastus"
}
resource "tls_private_key" "linux_key" {
  algorithm = "RSA"
  rsa_bits = 4096
}
# We want to save the private key to our machine
# We can then use this key to connect to our Linux VM
resource "local_file" "linuxkey" {
  filename="linuxkey.pem"
  content=tls_private_key.linux_key.private_key_pem
}
resource "azurerm_resource_group" "app_grp"{
  name=local.resource_group
  location=local.location
}
resource "azurerm_virtual_network" "app_network" {
  name                = "app-network"
  location            = local.location
  resource_group_name = azurerm_resource_group.app_grp.name
  address_space       = ["10.0.0.0/16"]
}
resource "azurerm_subnet" "SubnetA" {
  name                 = "SubnetA"
  resource_group_name  = local.resource_group
  virtual_network_name = azurerm_virtual_network.app_network.name
  address_prefixes     = ["10.0.1.0/24"]
  depends_on = [
    azurerm_virtual_network.app_network
  ]
}
resource "azurerm_network_interface" "app_interface" {
  name                = "app-interface"
  location            = local.location
  resource_group_name = local.resource_group
  ip_configuration {
    name                          = "internal"
    subnet_id                     = azurerm_subnet.SubnetA.id
    private_ip_address_allocation = "Dynamic"
    public_ip_address_id = azurerm_public_ip.app_public_ip.id
  }
  depends_on = [
    azurerm_virtual_network.app_network,
    azurerm_public_ip.app_public_ip
  ]
}
resource "azurerm_linux_virtual_machine" "linux_vm" {
  name                = "wikibot"
  resource_group_name = local.resource_group
  location            = local.location
  size                = "Standard_D2s_v3"  #Standard_B1s
  admin_username      = "elastic"
  network_interface_ids = [
    azurerm_network_interface.app_interface.id,
  ]
  admin_ssh_key {
    username   = "elastic"
    public_key = tls_private_key.linux_key.public_key_openssh
  }
  os_disk {
    caching              = "ReadWrite"
    storage_account_type = "Standard_LRS"
  }
  custom_data = filebase64("docker_and_elastic.txt")
  source_image_reference {
    publisher = "Canonical"
    offer     = "UbuntuServer"
    sku       = "18.04-LTS"
    version   = "latest"
  }
  depends_on = [
    azurerm_network_interface.app_interface,
    tls_private_key.linux_key,
    # azurerm_network_security_rule.priority1001,
    azurerm_network_security_rule.priority1002,
    azurerm_network_security_rule.priority1003,
    azurerm_network_security_rule.priority1004,
  ]
}
resource "azurerm_public_ip" "app_public_ip" {
  name                = "app-public-ip"
  resource_group_name = local.resource_group
  location            = local.location
  allocation_method   = "Static"
  depends_on = [
    azurerm_resource_group.app_grp
  ]
}
resource "azurerm_network_security_group" "example" {
  name = "example-nsg"
    location = azurerm_resource_group.app_grp.location
  resource_group_name = azurerm_resource_group.app_grp.name
  }
# resource "azurerm_network_security_rule" "priority1001" {
#   name                        = "example-allow-SSH"
#     priority                    = 1001
#   direction                   = "Inbound"
#   access                      = "Allow"
#   protocol                    = "Tcp"
#   source_port_range           = "*"
#   destination_port_range      = "22"
#   source_address_prefix       = "*"
#   destination_address_prefix  = "*"
#   resource_group_name = azurerm_resource_group.app_grp.name
#   network_security_group_name = azurerm_network_security_group.example.name
#   }
resource "azurerm_network_security_rule" "priority1002" {
  name                        = "example-allow-Jupyter"
    priority                    = 1002
  direction                   = "Inbound"
  access                      = "Allow"
  protocol                    = "Tcp"
  source_port_range           = "*"
  destination_port_range      = "8888"
  source_address_prefix       = "*"
  destination_address_prefix  = "*"
  resource_group_name = azurerm_resource_group.app_grp.name
  network_security_group_name = azurerm_network_security_group.example.name
  }
resource "azurerm_network_security_rule" "priority1003" {
    name                        = "example-allow-Elastic"
    priority                    = 1003
    direction                   = "Inbound"
    access                      = "Allow"
    protocol                    = "Tcp"
    source_port_range           = "*"
    destination_port_range      = "9200"
    source_address_prefix       = "*"
    destination_address_prefix  = "*"
    resource_group_name         = azurerm_resource_group.app_grp.name
    network_security_group_name = azurerm_network_security_group.example.name
}
resource "azurerm_network_security_rule" "priority1004" {
  name                        = "example-allow-Outbound"
  priority                    = 1004
  direction                   = "Outbound"
  access                      = "Allow"
  protocol                    = "Tcp"
  source_port_range           = "*"
  destination_port_range      = "*"
  source_address_prefix       = "*"
  destination_address_prefix  = "*"
  resource_group_name         = azurerm_resource_group.app_grp.name
  network_security_group_name = azurerm_network_security_group.example.name
}
```
