# 🚀 Docker ENTRYPOINT vs CMD

Understanding the difference between `ENTRYPOINT` and `CMD` is crucial for creating predictable and flexible Docker images.

## 📝 Core Concepts

### ENTRYPOINT

- Defines the **main executable** of the container.
- Cannot be easily overridden by just passing arguments at the end of `docker run`.
- Used for making images that act like **executables**.

### CMD

- Provides **default arguments** for the entrypoint.
- Can be **completely overridden** by the user when starting the container.
- If no `ENTRYPOINT` is defined, `CMD` acts as the command itself.

---

## 🛠️ Overriding Commands

### Overriding CMD

Simply provide a new command at the end of the `docker run` statement:

```bash
docker run <image_name> echo "Hello World"
```

### Overriding ENTRYPOINT

You must explicitly use the `--entrypoint` flag:

```bash
# Start a bash shell instead of the default entrypoint
docker run --entrypoint /bin/bash <image_name>

# Start a shell and run a specific command
docker run --entrypoint /bin/bash <image_name> -c "echo hello"
```

---

## 🤝 Using ENTRYPOINT + CMD Together

The most powerful pattern is to use `ENTRYPOINT` to define the binary and `CMD` to provide default flags.

### Example: A `curl` Tool

```Dockerfile
FROM ubuntu:22.04

RUN apt-get update && apt-get install -y curl

# The fixed command
ENTRYPOINT ["curl"]

# The default argument (can be overridden)
CMD ["--help"]
```

#### Usage Scenarios:

1.  **Default Run**: `docker run my-curl`
    - Executes: `curl --help`
2.  **Custom Run**: `docker run my-curl google.com`
    - Executes: `curl google.com` (completely replaces `--help`)

---

## 💡 Best Practices

- Use **Exec Form** (JSON array: `["executable", "param1"]`) instead of Shell Form. This ensures signals (like SIGTERM) are passed correctly to the process.
- Use `ENTRYPOINT` for the "unchanging" part of your command.
- Use `CMD` for arguments that users are likely to change.
