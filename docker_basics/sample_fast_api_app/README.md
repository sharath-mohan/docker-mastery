# 🚀 Sample FastAPI App (with UV & Docker)

This directory contains a modern **FastAPI** application that demonstrates best practices for Dockerizing Python applications using [**uv**](https://github.com/astral-sh/uv), the extremely fast Python package manager.

---

## ✨ Features

- **FastAPI**: High-performance web framework.
- **UV**: Blazing fast dependency resolution and management.
- **Dockerized**: Optimized `Dockerfile` using `python:3.12-slim-trixie`.
- **Environment Management**: Modern `pyproject.toml` and `uv.lock` workflow.

---

## 🛠️ Docker Instructions

### 1. Build the Image

```bash
docker image build -t fastapp .
```

### 2. Run the Container

```bash
docker container run --name some-fast-app -p 8000:8000 -d fastapp
```

### 3. Verify it's Working

Open [http://localhost:8000](http://localhost:8000) in your browser. You should see:

```json
{ "Hello": "World updated" }
```

---

## 💻 Local Development (with UV)

If you have `uv` installed, you can run the app locally without Docker:

```bash
# Install dependencies
uv sync

# Run the app
uv run uvicorn main:app --reload
```

---

## 🔍 Deep Dive: The Dockerfile

Our `Dockerfile` uses some advanced patterns:

1. **`COPY --from=ghcr.io/astral-sh/uv`**: Instead of installing `uv` via `pip`, we copy the binary directly from the official UV image. This is faster and more reliable.
2. **`uv sync --locked`**: Uses the `uv.lock` file to ensure deterministic installs.
3. **Environment Variables**:
   - `UV_NO_DEV=1`: Excludes development dependencies in the final image.
   - `PATH="/app/.venv/bin:$PATH"`: Ensures we use the virtual environment created by `uv`.

---

_Back to [Docker Basics](../README.md)_
