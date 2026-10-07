# Week 06 — Dockerfile & GHCR

## 1. Docker Image

내가 배포한 Docker Image:

- `ghcr.io/ela-a11/guestbook:v1`
- `ghcr.io/ela-a11/guestbook:v2`

GHCR에 Docker Image를 push하고 pull하여 정상적으로 실행되는 것을 확인하였다.

---

## 2. Dockerfile 설명

사용한 Dockerfile:

```dockerfile
FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
RUN useradd -m appuser
USER appuser
ENV APP_TITLE="Eleonora의 방명록 V2" \
    THEME_COLOR="#C6A15B"
EXPOSE 5000
CMD ["python", "app.py"]
---

## 3. Docker Build Cache

When building `guestbook:v2`, Docker used the cache from previous layers:

```text
CACHED [2/6] WORKDIR /app
CACHED [3/6] COPY requirements.txt .
CACHED [4/6] RUN pip install --no-cache-dir -r requirements.txt


