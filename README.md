# 🐳 Docker Mastery

Welcome to my **Docker Mastery** journey! This repository serves as a comprehensive collection of notes, examples, and configuration files created while mastering Docker and container orchestration.

## 🎯 Repository Purpose

This repo is a living document of my progress, containing:

- **Core Concepts**: [Understanding images, containers, and layers](./docker_basics/README.md).
- **Workflow**: [Dockerfiles, image building, and registry management](./docker_basics/README.md).
- **Networking**: Bridging, host, and overlay networks.
- **Persistence**: [Volumes and bind mounts](./docker_volumes/README.md).
- **Orchestration**: Docker Compose and basic Swarm/K8s concepts.
- **Best Practices**: Security, optimization, and multi-stage builds.

## 📂 Modules

Explore detailed notes and examples for each topic:

- 🛠️ [**Docker Basics**](./docker_basics/) - Core concepts, CLI essentials, and sample apps.
- 💾 [**Docker Volumes & Data**](./docker_volumes/) - Data persistence, bind mounts, and volumes.
- 🚀 [**Docker Entrypoint**](./docker_entrypoint/) - Understanding ENTRYPOINT vs CMD and executable images.

## 🗺️ Learning Roadmap

### 1. The Basics

- [x] [What is a Container?](./docker_basics/README.md)
- [x] Installing Docker & Setup
- [x] [The Docker CLI Essentials](./docker_basics/README.md)
- [x] [Working with Images](./docker_basics/README.md) (`pull`, `push`, `build`)

### 2. Deep Dive: Dockerfiles

- [x] [Instruction Sets](./docker_basics/sample_fast_api_app/README.md) (`FROM`, `RUN`)
- [x] [ENTRYPOINT vs CMD](./docker_entrypoint/README.md)

- [ ] Layer Caching & Optimization
- [ ] Multi-stage Builds (Partial - see FastAPI app)
- [x] [Environment Variables & Args](./docker_basics/sample_fast_api_app/README.md)

### 3. Data Management

- [x] [Bind Mounts vs Volumes](./docker_volumes/README.md)
- [x] [Persistence Strategies](./docker_volumes/README.md)
- [ ] Backing up and Restoring Data

### 4. Networking

- [ ] Default Bridge Network
- [ ] User-Defined Bridge Networks
- [ ] Container-to-Container Communication
- [ ] Port Mapping

### 5. Docker Compose

- [ ] Writing `docker-compose.yml`
- [ ] Managing Multi-Container Apps
- [ ] Environment Files
- [ ] Overrides and Profiles

---

## 🛠️ Tools Used

- **Docker Desktop / Engine**
- **Docker Hub**
- **VS Code Docker Extension**

## 📚 Resources

- [Docker Documentation](https://docs.docker.com/)
- [Docker Curriculum](https://docker-curriculum.com/)
- [Play with Docker](https://labs.play-with-docker.com/)

---

_Happy Dockering!_ 🚀
