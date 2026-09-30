# 5주차 - Docker

## 실습 내용
- Docker 실행 환경 확인
- hello-world 실행
- nginx 컨테이너 실행
- localhost:8080 응답 확인
- docker ps 상태 확인
- Python 3.9 / 3.12 실행 확인

## 검증
- `docker --version`
- `docker run --rm hello-world`
- `curl -I http://localhost:8080`
- `docker ps`

## 결과
- nginx: `http://localhost:8080`
- Python 3.9: `Python 3.9.25`
- Python 3.12: `Python 3.12.14`
- `test.py`: Python 3.9에서 `SyntaxError`, Python 3.12에서 `Python 3.12`

## 체크리스트
- [x] docker --version
- [x] docker run hello-world
- [x] web nginx container
- [x] localhost:8080 response
- [x] docker ps status
- [x] week05/README.md record
- [x] clean up containers
