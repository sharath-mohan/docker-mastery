# 💾 Docker Data Management: Volumes & Bind Mounts

In Docker, containers are ephemeral—meaning any data created inside them is lost when the container is deleted. To persist data, Docker provides two primary mechanisms: **Volumes** and **Bind Mounts**.

---

## 🏗️ Storage Strategies

| Feature           | Volumes                                             | Bind Mounts                                |
| :---------------- | :-------------------------------------------------- | :----------------------------------------- |
| **Managed by**    | Docker                                              | User (Host System)                         |
| **Host Location** | Docker-managed storage (`/var/lib/docker/volumes/`) | Any arbitrary path on host                 |
| **Isolation**     | High (isolated from host OS)                        | Low (direct access to host files)          |
| **Performance**   | High (native host speed)                            | Dependent on host storage speed            |
| **Typical Use**   | Database storage, shared data between containers    | Source code syncing, config file overrides |

---

## 📦 1. Volumes

Volumes are the preferred mechanism for persisting data generated and used by Docker containers.

### Anonymous Volumes

When you run a container without specifying a source for the volume, Docker creates an anonymous one.

**Example: Postgres**

```sh
# Run Postgres (will create an anonymous volume automatically)
docker run --name some-postgres \
  -e POSTGRES_PASSWORD=mysecretpassword \
  -d postgres:alpine3.22
```

**Inspecting Volumes:**

```sh
# List all volumes
docker volume ls

# Inspect the container to find the mount point
docker inspect some-postgres
```

### Named Volumes

Named volumes are easier to manage and reference.

```sh
docker run --name some-postgres \
  -e POSTGRES_PASSWORD=mysecretpassword \
  -v postgres-db:/var/lib/postgresql/data \
  -d postgres:alpine3.22
```

---

## 🔗 2. Bind Mounts

Bind mounts link a specific path on your host machine to a path in the container. This is extremely useful for development.

### Example: Nginx with Local Source

Map your current working directory to the Nginx HTML folder to see live changes.

```sh
docker container run --name some-nginx \
  -p 8000:80 \
  -v $(pwd):/usr/share/nginx/html \
  -d nginx:alpine
```

---

## 💡 Pro Tips

- **Persistence**: Both volumes and bind mounts outlive the container. You must delete them explicitly if they are no longer needed.
- **Portability**: Volumes are more portable because they are managed entirely by Docker and don't depend on the host's directory structure.
- **Security**: Be careful with bind mounts; giving a container write access to sensitive host directories can be a security risk.

---

_Back to [Root README](../README.md)_
