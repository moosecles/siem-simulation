# SIEM/SOAR Simulation Pipeline

A fully containerized, end-to-end log pipeline using **Python**, **Kafka**, **Fluent Bit**, and **Splunk**, simulating realistic log ingestion, transformation, and security monitoring workflows.

---

## Demo

<!-- Will update with demo of dashboard once I play around more! -->

---

## Components within this project

| Component             | Role                                                      |
| --------------------- | --------------------------------------------------------- |
| `log-generator`       | Simulates JSON logs with timestamps, user IDs, and events |
| `kafka` & `zookeeper` | Message broker and coordination                           |
| `fluent-bit`          | Parses and routes logs to Kafka                           |
| `kafka-consumer`      | Pulls logs from Kafka and pushes to Splunk HEC            |
| `splunk`              | Collects and indexes logs, provides a GUI for searching   |

---

## Technologies Used

| Tool                      | Why It’s Used                                           |
| ------------------------- | ------------------------------------------------------- |
| **Docker/Docker Compose** | Easy orchestration of multi-container environments      |
| **Kafka**                 | High-throughput message streaming for decoupled systems |
| **Fluent Bit**            | Lightweight log processor and forwarder                 |
| **Splunk**                | Enterprise-grade search, monitoring, and analysis       |
| **Python**                | Kafka Consumer script for parsing and forwarding logs   |

---

## Getting Started

### 1. Clone the Repo

```bash
git clone https://github.com/yourname/siem-simulation.git
cd siem-simulation
```

### 2. Set Up Environment Variables

Create a .env file in the root directory with the following contents:

```bash
KAFKA_TOPIC_NAME=logs
KAFKA_BOOTSTRAP=kafka:9092
SPLUNK_HEC_LINK=http://splunk:8088/services/collector
SPLUNK_TOKEN=ENTER_YOUR_SPLUNK_HEC_TOKEN_HERE
SPLUNK_PASSWORD=ENTER_YOUR_WANTED_SPLUNK_PASSWORD_HERE
```

### 3. Run Everything

To start the services just do:

```bash
docker-compose up --build
```

It may take a minute or two but once Splunk is fully initialized, the Kafka consumer will automatically begin sending logs.

## File Structure (preferred)

```plaintext
siem-simulation/
├── docker-compose.yml
├── .env
├── log-generator/
│   └── generator.py
├── kafka-consumer/
│   └── consumer.py
├── fluent-bit/
│   └── fluent-bit.conf
├── splunk/
│   └── default.yml  # Used to disable Splunk automatically enabling SSL
```

## Learning Lessons & Challenges Faced

- Technologies: Learne how to use all technologies as well as why they were used, besides Python, listed during this project which was challenging in itself

- Race conditions: Kept having certain containers spin up before it was needed, leading to a bunch of errors due to race conditions. Used 'depends-on:' as well as various techniques to keep Avaibility up.

- Auto Enabling SSL on container spin up: Disabled Splunk's SSL cleanly by using a default.yml to set certain flags instead of direct commands/methods.

## What you can learn from using the project:

- How a realistic log pipeline simulation using Fluent Bit, Kafka, and Splunk is created.

- How to mess around with Splunk Dashboards and sample SOAR/SIEM data.

## Questions?

Feel free to open an issue or reach out via email: jayson.murphy99@gmail.com
