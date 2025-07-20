# alx-backend-storage

## Project: Redis Basic

This project focuses on learning how to use Redis for basic operations and as a simple cache. It includes tasks to implement a `Cache` class with methods to store and retrieve data, track method calls, store input/output history, and implement an expiring web cache. The project is designed to run on **Ubuntu 18.04 LTS** using **Python 3.7** and adheres to specific coding and documentation standards.

---

## Table of Contents

- [Project Overview](#project-overview)
- [Requirements](#requirements)
- [Setup Instructions](#setup-instructions)
- [Tasks](#tasks)
- [Repository Structure](#repository-structure)
- [Usage](#usage)
- [Author](#author)

---

## Project Overview

This project demonstrates the use of Redis, an in-memory data structure store, to perform basic operations and caching. It includes implementing a `Cache` class with methods to store data, retrieve data with type conversion, track method call counts, store call history, and create an expiring web cache. The tasks are implemented in Python, following strict coding and documentation guidelines.

---

## Requirements

- **Environment**: Ubuntu 18.04 LTS
- **Python Version**: Python 3.7
- **Code Style**: Pycodestyle (version 2.5)
- **File Requirements**:
  - All Python files must start with `#!/usr/bin/env python3`.
  - All files must end with a new line.
  - A `README.md` file is mandatory at the root of the project.
- **Documentation**:
  - All modules, classes, and functions must have proper documentation accessible via Python's `.__doc__` attribute.
  - Documentation must be complete sentences explaining the purpose of the module, class, or function.
- **Type Annotations**: All functions and coroutines must be type-annotated.
- **Redis Installation**:
  - Install Redis server: `sudo apt-get -y install redis-server`
  - Install Python Redis client: `pip3 install redis`
  - Configure Redis to bind to localhost: `sed -i "s/bind .*/bind 127.0.0.1/g" /etc/redis/redis.conf`
- **Redis in Containers**: Start Redis with `service redis-server start` in a container.
- **Dependencies**: Install the `requests` module for the web cache task (`pip3 install requests`).

---

## Setup Instructions

1. **Install Redis**:
   ```bash
   sudo apt-get -y install redis-server
   pip3 install redis
   sed -i "s/bind .*/bind 127.0.0.1/g" /etc/redis/redis.conf