# Cloud System Info

A Flask-based web application deployed on AWS to demonstrate a secure, segmented Linux environment with a Bastion Host, a private EC2 instance, and Nginx as the service layer.

This project was built to simulate a real infrastructure scenario: a publicly reachable entry point for administration, a private server with no public IP, and controlled access between both layers.

## Overview

The application runs inside a private Ubuntu EC2 instance and is accessed only through the designed network path. The Bastion Host is used for SSH administration, while Nginx serves as the public-facing service layer. During testing and demonstration, ngrok was used as a temporary public tunnel.

## Architecture

```text
Internet
   ↓
ngrok
   ↓
Bastion Host (Ubuntu, public IP)
   ↓ SSH
Private EC2 (Ubuntu, no public IP)
   ↓
Nginx service
   ↓
Flask application
```

## What This Project Demonstrates

* Linux administration with Ubuntu
* SSH access through a Bastion Host
* AWS EC2 networking and segmentation
* Security Group-based access control
* Nginx as a service and reverse proxy
* Flask application deployment
* Controlled public exposure for testing and validation
* Technical documentation and infrastructure thinking

## Features

* Home page with navigation
* Status page with server information
* Flask application running in a cloud environment
* Private server access only through the Bastion Host
* Restricted inbound traffic on the private instance

## Security Design

* The private EC2 instance has **no public IP**
* SSH access is allowed only from the Bastion Host
* HTTP/HTTPS are blocked on the private instance
* Administrative access is centralized through the Bastion Host
* Network exposure is intentionally minimized

## Stack

* Python
* Flask
* Ubuntu Linux
* AWS EC2
* Bastion Host
* Nginx
* SSH
* Security Groups
* ngrok

## How It Was Built

### 1. Flask application

A lightweight Flask app was created with a simple home page and a status page.

### 2. Linux environment

The application was deployed on Ubuntu to mirror common cloud server environments.

### 3. AWS architecture

Two EC2 instances were used:

* one Bastion Host with a public IP
* one private instance without public access

### 4. Access control

Security Groups were configured so the private instance could only be reached from the Bastion Host.

### 5. Nginx service

Nginx was configured as a service to sit in front of the application and act as the entry layer.

### 6. Public exposure for testing

ngrok was used only as a temporary tunnel for validation and demonstration.

## Deployment

The application was deployed in the following flow:

1. Create the AWS EC2 instances.
2. Configure the Bastion Host with public access.
3. Deploy the Flask app inside the private Ubuntu instance.
4. Configure Nginx as the service layer.
5. Restrict access to the private instance using Security Groups.
6. Use the Bastion Host for SSH administration.
7. Expose the service temporarily with ngrok for external validation.

## Project Structure

```text
cloud-system-info/
├── app.py
├── templates/
│   ├── home.html
│   └── status.html
├── README.md
└── .gitignore
```

## Learning Outcomes

This project helped me practice:

* cloud infrastructure basics
* Linux server management
* SSH and Bastion-based access
* network isolation and security boundaries
* service exposure and reverse proxy concepts
* practical deployment workflow

## Final Note

This repository is more than a Flask app. It represents a complete infrastructure exercise focused on access control, Linux servers, and cloud deployment patterns.
