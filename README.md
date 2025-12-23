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

## ⚙️ Setup Instructions

### 1️⃣ Start Minikube
```bash
minikube start

2️⃣ Build Docker Image inside Minikube
minikube docker-env | Invoke-Expression
docker build -t autoscale-app .

3️⃣ Deploy Application
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml

4️⃣ Enable Metrics Server
minikube addons enable metrics-server

5️⃣ Deploy HPA
kubectl apply -f hpa.yaml

6️⃣ Access Application
kubectl port-forward service/autoscale-service 8081:80
Open browser:
http://127.0.0.1:8081

7️⃣ Trigger Auto-Scaling
while ($true) {
  Invoke-WebRequest http://127.0.0.1:8081/load | Out-Null
}

📈 Auto-Scaling Demo
Pods scale up when CPU > 50%

Pods scale down automatically when load stops

🧠 Key Learnings
Docker image management in Minikube

Kubernetes Services and networking

Metrics Server configuration

CPU-based auto-scaling using HPA