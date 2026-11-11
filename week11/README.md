# 11주차 - 쿠버네티스 설정과 상태 점검

## 1. 실습 목표

- ConfigMap과 Secret을 이용한 설정 분리
- Redis Deployment 및 Service 구성
- 환경 변수를 이용한 Guestbook과 Redis 연결
- ConfigMap 변경 및 Rolling Update 확인
- Readiness Probe와 Liveness Probe 동작 확인
- kubectl 명령어를 이용한 상태 점검 및 문제 해결

## 2. ConfigMap과 Secret

ConfigMap을 생성하여 APP_TITLE, THEME_COLOR, REDIS_HOST, REDIS_PORT를 설정하였다.

Secret을 생성하고 Base64 디코딩을 통해 값이 암호화가 아닌 인코딩 방식으로 저장되는 것을 확인하였다.

## 3. Redis 배포

Redis Deployment와 ClusterIP Service를 생성하였다.

실행 결과:
- Redis Pod: 1/1 Running
- Redis Service: 6379 포트
- Guestbook과 Redis 연결 성공

로그:
[INFO] Redis 연결 성공: redis:6379

## 4. 환경 변수 확인

kubectl exec 명령어를 사용하여 환경 변수를 확인하였다.

- APP_TITLE: 방명록 (k8s)
- THEME_COLOR: #16a34a
- REDIS_HOST: redis

## 5. ConfigMap 변경

APP_TITLE을 New 방명록 (k8s)로 변경하고 THEME_COLOR를 #e11d48로 변경하였다.

kubectl rollout restart 명령어로 Deployment를 재시작한 후 변경된 환경 변수가 적용된 것을 확인하였다.

## 6. Health Check

/readyz 응답:
{"status":"ready"}

/healthz 응답:
{"status":"ok"}

## 7. Readiness Probe 장애 실험

Readiness Probe 경로를 /wrong-readyz로 변경하였다.

결과:
- HTTP 404 오류 발생
- Pod Ready 상태가 False로 변경됨
- 컨테이너는 계속 실행됨
- 재시작 횟수는 증가하지 않음

이후 /readyz로 복구하였다.

## 8. Liveness Probe 장애 실험

Liveness Probe 경로를 /wrong-healthz로 변경하였다.

결과:
- HTTP 404 오류 발생
- Liveness probe failed 이벤트 발생
- Kubernetes가 컨테이너를 자동 재시작함
- 재시작 횟수 3~4회 확인

이후 /healthz로 복구하였다.

## 9. 실습 결과

- ConfigMap 및 Secret 설정 완료
- Redis 연결 성공
- Guestbook Pod 3개 정상 실행
- Readiness 및 Liveness Probe 테스트 완료
- 장애 발생 및 복구 과정 확인

## 10. 관련 파일

- guestbook/k8s/configmap.yaml
- guestbook/k8s/deployment.yaml
- guestbook/k8s/redis.yaml
- guestbook/k8s/secret.example.yaml

실제 Secret 파일은 보안을 위해 Git에 업로드하지 않았다.
