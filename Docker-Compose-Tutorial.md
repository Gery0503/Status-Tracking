Here are detailed notes summarizing the [**Docker Compose YouTube tutorial** by NetworkChuck](https://youtu.be/DM65_JyGxCo?si=PRegTuf2tYEEmy5_), organized for quick reference:

---

### 🔹 **Introduction: Docker Compose = Magic**

* One command: spins up **14 containers**, **3 networks** → complete hacking lab.
* Demonstrates Docker Compose's power: defining **multiple containers/networks** in **one YAML file**.
* Objective: Learn to build Docker environments faster & cleaner.

---

### 🧰 **Prerequisites**

1. **Basic Docker knowledge**: `docker run` familiarity is enough.
2. **Linux environment**: Any distro, VM, or WSL2 is fine (uses Ubuntu Desktop via VirtualBox in demo).
3. **Docker & Docker Compose installed**:

   ```bash
   sudo apt update
   sudo apt install docker.io docker-compose -y
   ```

---

### ⚙️ **Step-by-Step: From `docker run` to Compose**

#### 1. **Manual method (legacy)**:

```bash
sudo docker run -d --name web -p 8080:80 nginx
```

#### 2. **Using Docker Compose (modern)**:

1. Create a directory:

   ```bash
   mkdir coffee_time && cd coffee_time
   ```

2. Create `docker-compose.yml`:

   ```yaml
   version: "3"
   services:
     website:
       image: nginx
       ports:
         - "8081:80"
       restart: always
   ```

3. Launch it:

   ```bash
   sudo docker-compose up -d
   ```

4. Stop or remove:

   ```bash
   sudo docker-compose stop
   sudo docker-compose down
   ```

---

### 🧠 **Docker Compose Concepts**

* **Default filename**: `docker-compose.yml` (don’t rename unless necessary).
* **YAML** format is whitespace-sensitive (like Python).
* **Docker Compose command must run in the same folder** as the YAML file.

---

### 📦 **Add More Containers**

To add another `nginx` container:

```yaml
  website2:
    image: nginx
    ports:
      - "8082:80"
    restart: always
```

---

### 🌐 **Add a Custom Network**

1. Under the top-level:

   ```yaml
   networks:
     coffee:
       ipam:
         driver: default
         config:
           - subnet: "192.168.92.0/24"
   ```

2. Assign a container to the network:

   ```yaml
   networks:
     - coffee
   ipv4_address: 192.168.92.21
   ```

---

### 🛠️ **Advanced: Deploying WordPress**

#### Two services: WordPress + MySQL

```yaml
version: "3"
services:
  wordpress:
    image: wordpress
    ports:
      - "8089:80"
    environment:
      WORDPRESS_DB_HOST: mysql
      WORDPRESS_DB_USER: user
      WORDPRESS_DB_PASSWORD: coffee
      WORDPRESS_DB_NAME: wordpress
    depends_on:
      - mysql
    networks:
      - ohyeah

  mysql:
    image: "mysql:5.7"
    environment:
      MYSQL_DATABASE: wordpress
      MYSQL_USER: user
      MYSQL_PASSWORD: coffee
      MYSQL_ROOT_PASSWORD: coffee
    volumes:
      - ./mysql:/var/lib/mysql
    networks:
      - ohyeah

networks:
  ohyeah:
```

#### Commands:

```bash
docker-compose up -d
docker-compose ps
```

* **MySQL data persists** even if containers are removed (thanks to volume).
* **WordPress site** is now live at `localhost:8089`.

---

### 🧪 **Deploying a Hacking Lab**

* Uses **vulnerable containers** from [Vulhub](https://github.com/vulhub/vulhub).
* Massive `docker-compose.yml` with many services and networks.
* Auto-launches **Kali Linux container** alongside the targets.

---

### 💡 **Bonus Inspiration: Other Compose Projects**

* Minecraft server
* Pi-hole with DNS over HTTPS
* Production deployments at scale

---

### 🧱 **Best Practices**

* Use `depends_on` to set service boot order.
* Always assign containers to custom networks (avoid Docker default).
* Use **volumes** for persistent data (especially for databases).
* You can modify `docker-compose.yml` and re-run `up -d` to update services.

---

### 🧃 Outro Takeaways

* Docker Compose is **fast, scalable, and easy**.
* Helps move from basic `docker run` to full app deployment.
* Great tool for devs, hackers, sysadmins, and IT learners.

---

Let me know if you want me to extract just the **YAML code blocks**, summarize **just the WordPress deployment**, or help you write your own `docker-compose.yml` file!

(Generated from ChatGPT)
