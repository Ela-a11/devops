# Week 08 — Kubernetes 실습

## 1. 실습 목표
Minikube를 이용하여 로컬 Kubernetes 클러스터를 구성하고, Pod와 Deployment의 동작을 확인한다.

## 2. 실습 환경
- macOS
- Docker Desktop
- Minikube
- kubectl

## 3. 실습 내용

### Kubernetes 클러스터 실행
- `minikube start --driver=docker`
- `kubectl get nodes`
- 노드 상태: Ready

### Nginx Pod 실행
- `kubectl run mynginx --image=nginx`
- `kubectl get pods`
- `kubectl describe pod mynginx`
- `kubectl logs mynginx`
- `kubectl port-forward mynginx 8080:80`
- 브라우저에서 Nginx 페이지 확인

### Deployment 및 Self-healing
- `kubectl create deployment mynginx --image=nginx --replicas=3`
- 3개의 Pod 실행 확인
- Pod 1개 삭제 후 새로운 Pod 자동 생성 확인

### Guestbook 실행
- `kubectl create deployment guestbook --image=ghcr.io/ela-a11/guestbook:v1`
- `kubectl get deployments`
- `kubectl logs -l app=guestbook`
- `kubectl port-forward deployment/guestbook 8081:5000`
- 브라우저에서 Guestbook 실행 확인

## 4. 오류 및 해결
처음에 이미지 이름에 대문자를 사용하여 InvalidImageName 오류가 발생했다.

- 오류 이미지: `ghcr.io/Ela-a11/guestbook:v1`
- 수정 이미지: `ghcr.io/ela-a11/guestbook:v1`

`kubectl set image` 명령어로 수정한 후 정상 실행되었다.

## 5. 실습 결과
Kubernetes의 Pod, Deployment, ReplicaSet 및 Self-healing 기능을 확인했다.
Guestbook 애플리케이션을 Kubernetes에서 실행하고 브라우저 접속에 성공했다.

## 6. 실습 종료
- `kubectl delete deployment guestbook`
- `minikube stop`
