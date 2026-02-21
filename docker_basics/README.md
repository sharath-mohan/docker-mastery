# 🛠️ Docker Basics

This module focuses on the fundamental concepts of Docker: images, containers, and the registry.

## 🧠 Core Concepts

- **Image**: A read-only template with instructions for creating a Docker container.
- **Container**: A runnable instance of an image.
- **Dockerfile**: A text document that contains all the commands a user could call on the command line to assemble an image.

---

## 🏗️ Hands-on Example

Checkout our [**Sample FastAPI App**](./sample_fast_api_app/README.md) to see a real-world implementation of:

- Writing a modern `Dockerfile`.
- Using `uv` for lightning-fast Python builds.
- Building and running images.

---

## ⌨️ Essential CLI Commands

### Image Management

- `docker image build -t name .` - Build an image from a Dockerfile.
- `docker image ls` - List all local images.
- `docker image rm name` - Remove an image.

### Container Management

- `docker container run -p 80:80 -d name` - Run a container in detached mode with port mapping.
- `docker container ls` - List running containers (`-a` for all).
- `docker container stop id` - Stop a running container.
- `docker container rm id` - Remove a container.

### Inspection & Logs

- `docker container logs -f id` - Follow container logs.
- `docker container inspect id` - View detailed container info.
- `docker container exec -it id sh` - Start an interactive shell inside a container.

---

_Back to [Root README](../README.md)_
