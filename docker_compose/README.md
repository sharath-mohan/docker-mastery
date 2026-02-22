# 🐙 Docker Compose: Multi-Container Orchestration

Docker Compose is a tool for defining and running multi-container Docker applications. With Compose, you use a YAML file to configure your application's services and then use a single command to create and start all the services.

## 🧱 The Two Pillars of Compose

1.  **The YAML Configuration (`docker-compose.yml`)**: A declarative file where you define services, networks, and volumes.
2.  **The CLI Tool (`docker compose`)**: The command-line interface used to manage the lifecycle of your application.

---

## 🚀 Common CLI Commands

| Command                  | Description                                                           |
| :----------------------- | :-------------------------------------------------------------------- |
| `docker compose up`      | Create and start containers defined in the YAML file.                 |
| `docker compose up -d`   | Start containers in **detached mode** (background).                   |
| `docker compose down`    | Stop and remove containers, networks, and images defined in the file. |
| `docker compose ps`      | List the status of containers managed by Compose.                     |
| `docker compose logs -f` | View and follow logs for all services.                                |
| `docker compose build`   | Rebuild images defined with the `build` instruction.                  |

> **Note**: Modern Docker uses `docker compose` (no hyphen), while older versions used `docker-compose`.

---

## 📄 Understanding the YAML Structure

A typical `docker-compose.yml` file consists of several key sections:

```yaml
version: "3.8" # Version of the Compose file format

services: # Define the containers that make up your app
  web:
    build: . # Build from a local Dockerfile
    ports:
      - "8000:8000"
    environment:
      - DEBUG=1

  database:
    image: postgres:15-alpine # Use a pre-built image
    volumes:
      - db_data:/var/lib/postgresql/data

volumes: # Define persistent data storage
  db_data:
```

---

## 🛠️ Practical Example: FastAPI + PostgreSQL

In this module, we have a concrete example of a FastAPI application communicating with a PostgreSQL database.

### 📁 Structure

- [**fast-api-postgres.yml**](./fast-api-postgres.yml): The orchestration file.
- [**fast-api-app/**](./fast-api-app/): The FastAPI source code and Dockerfile.

### 🏃 How to Run

To start the entire stack:

```bash
docker compose -f fast-api-postgres.yml up
```

### 💡 Key Concepts in This Example

- **`depends_on`**: Ensures the database starts before the API.
- **Service Discovery**: The API connects to the DB using the hostname `postgres` (the service name).
- **Volumes**: Mounting `./fast-api-app` for hot-reloading during development.
- **Environment Variables**: Passing credentials securely to both services.

---

## 🌟 Best Practices

- **Use Environment Files**: Keep secrets out of your YAML by using a `.env` file.
- **Define Healthchecks**: Ensure services are truly ready before others depend on them.
- **Resource Limits**: Set CPU and memory limits to prevent a single container from crashing the host.
- **Named Volumes**: Use named volumes instead of bind mounts for database persistence in production.
