# Running PLCSoftRel in Docker

This document provides instructions to run PLCSoftRel as a multi-container Docker Application using Docker Compose.

<hr/>

### Prerequisites

- Docker Desktop: https://docs.docker.com/engine/install/

### Run run.sh script
This bash script copies files to the docker folder and execute docker-compose to run the applicaiton. It will build Dockerfiles to create images for MySQL, FastAPI, and Next.js server and then run a multi-container application.
```bash
bash ./run.sh
```

<hr/>

### How to run bash script in Windows
One of ways to run bash scripts in windows is to utilize the windows feature: Windows Subsystem for Linux (WSL). The following steps will guide you to install Ubuntu in Windows.

1. Enable WSL

Search for "Turn Windows features on or off" in the Start Menu and enable "Windows Subsystem for Linux"

2. Check your default Linux distribution you are running
```bash
wsl -l
```
3. Install Ubuntu
```bash
wsl --install
```
4. Set Ubuntu as your default Linux distribution
```bash
wsl -s Ubuntu # or wsl --set-default Ubuntu
```
