# Week 06 — Dockerfile & GHCR

## 1. Docker Images

Images published to GitHub Container Registry (GHCR):

- `ghcr.io/ela-a11/guestbook:v1`
- `ghcr.io/ela-a11/guestbook:v2`

I pushed and pulled the Docker images from GHCR and verified that they could run successfully.

## 2. Dockerfile

The Dockerfile uses `python:3.12-slim` as its base image, installs Python dependencies, copies the application files, creates a non-root user, and starts the application.

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
```

Running the application as a non-root user helps reduce security risks.

## 3. Docker Build Cache

When building `guestbook:v2`, Docker reused cached layers:

```text
CACHED [2/6] WORKDIR /app
CACHED [3/6] COPY requirements.txt .
CACHED [4/6] RUN pip install --no-cache-dir -r requirements.txt
```

Docker build cache speeds up rebuilds by reusing layers whose inputs have not changed.

## 4. Key Takeaways

- **Dockerfile:** Defines how a Docker image is built.
- **GHCR:** Stores and distributes container images.
- **Image tags:** Identify versions such as `v1` and `v2`.
- **Non-root user:** Reduces risks associated with running the application as root.
- **Build cache:** Avoids repeating unchanged build steps.
