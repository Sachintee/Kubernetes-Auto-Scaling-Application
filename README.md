# Kubernetes Auto-Scaling Application 🚀

## 📌 Project Overview
This project demonstrates a cloud-native application deployed on Kubernetes with **Horizontal Pod Autoscaler (HPA)** enabled to automatically scale pods based on CPU utilization.

## 🧱 Architecture
User Traffic → Kubernetes Service → Pods (Auto-scaled by HPA)

↑

Metrics Server


## 🛠 Tech Stack
- Python (Flask)
- Docker
- Kubernetes (Minikube)
- Metrics Server
- Horizontal Pod Autoscaler (HPA)


📈 Auto-Scaling Demo
- Pods scale up when CPU > 50%

- Pods scale down automatically when load stops

🧠 Key Learnings
- Docker image management in Minikube

- Kubernetes Services and networking

- Metrics Server configuration

- CPU-based auto-scaling using HPA
