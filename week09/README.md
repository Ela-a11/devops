# Week 09 - Kubernetes Deployment and Service

## 1. Objectives
- Deploy Guestbook using YAML
- Understand Deployment, ReplicaSet, and Pod
- Configure Kubernetes Service
- Test scaling and self-healing
- Perform rolling update and rollback

## 2. Deployment
Created deployment.yaml using:
- Image: ghcr.io/ela-a11/guestbook:v1
- Replicas: 2
- Container port: 5000

Commands:
- kubectl apply -f week09/deployment.yaml
- kubectl get deployments
- kubectl get pods -l app=guestbook

Result: 2/2 Pods Running.

## 3. Service
Created service.yaml:
- Type: NodePort
- Port: 80
- TargetPort: 5000
- NodePort: 30080

Result: Service created and connected to two Pod endpoints.

## 4. Scaling and Self-Healing
Scaled Deployment from 2 to 3 replicas.
Deleted one Pod manually.
Kubernetes automatically created a replacement Pod.

Result: 3 Pods Running.

## 5. Rolling Update
Updated container image from v1 to v2.

Result: New Pods started and old Pods terminated.

## 6. Rollback
Rolled back Deployment from v2 to v1.

Result:
- Rollback completed successfully
- 3 new Pods Running
- Image: ghcr.io/ela-a11/guestbook:v1

## 7. Conclusion
Practiced declarative Kubernetes deployment, Service configuration,
scaling, self-healing, rolling updates, and rollback.
