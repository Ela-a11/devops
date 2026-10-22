# Week 05 — Docker Basics

## 1. Lab Objectives

- Verify the Docker environment.
- Run the `hello-world` container.
- Start an Nginx web server in a Docker container.
- Verify the web server response at `localhost:8080`.
- Inspect running containers with `docker ps`.
- Compare Python 3.9 and Python 3.12 execution environments.

## 2. Commands and Verification

```bash
docker --version
docker run --rm hello-world
curl -I http://localhost:8080
docker ps
```

- `docker --version` displays the installed Docker version.
- `docker run --rm hello-world` runs a test container and removes it after it exits.
- `curl -I` checks the HTTP response headers from the local web server.
- `docker ps` lists running containers.

## 3. Results

| Task | Result |
|---|---|
| Docker environment | Docker version verified |
| Hello World | Container executed successfully |
| Nginx | Available at `http://localhost:8080` |
| Python 3.9 | `Python 3.9.25` |
| Python 3.12 | `Python 3.12.14` |
| `test.py` | Produced a `SyntaxError` in Python 3.9 and printed `Python 3.12` in Python 3.12 |

The `test.py` result demonstrates that Python code compatibility can depend on the interpreter version.

## 4. Checklist

- [x] Verified the Docker version
- [x] Ran the `hello-world` container
- [x] Started the Nginx web container
- [x] Verified the response at `localhost:8080`
- [x] Checked container status with `docker ps`
- [x] Documented the results in `week05/README.md`
- [x] Cleaned up containers

## 5. Key Takeaways

- **Docker image:** A packaged template used to create containers.
- **Container:** An isolated environment for running an application.
- **Nginx:** A web server that can run inside a container.
- **Port mapping:** Makes a container service accessible through a host port.
- **Python versions:** Different interpreters may support different syntax and language features.

This lab introduced the basic Docker workflow: running containers, checking service availability, inspecting container status, and comparing application behavior across Python versions.
