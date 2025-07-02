# SIEM/SOAR Simulation Pipeline

A fully containerized, end-to-end log pipeline using **Python**, **Kafka**, **Fluent Bit**, and **Splunk**, simulating realistic log ingestion, transformation, and security monitoring workflows.

---

## Demo

Will update with demo of a sample Splunk dashboard once I play around more!

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

| Tool                      | Why It’s Used                                                                                                     |
| ------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| **Docker/Docker Compose** | Allows for easy orchestration of multi-container environments                                                     |
| **Kafka**                 | Fast message delivery system that helps different parts of an app work independently.                             |
| **Fluent Bit**            | Lightweight log processor and forwarder                                                                           |
| **Splunk**                | Tool used to search through data, track activity, and gain insights.                                              |
| **Python**                | Used in `generator.py` to create sample logs and in `consumer.py` to read logs from Kafka and send them to Splunk |

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

- `Technologies:` Gained hands-on experience with the entire tech stack used in this project including Kafka, Fluent Bit, Docker, and Splunk. I learned not just how to use them, but why each one is so valued for it's intended task.

- `Race conditions:` Faced errors when certain containers (like the consumer) started before the containers they depended on were ready. Solved this by using Docker Compose's 'depends-on:' property as well as other various techniques to ensure no errors occured.

- `SSL Issues with Splunk:` Splunk enabled SSL by default, which caused communication issues when consuming. I overwrite this cleanly by using a default.yml to set certain flags instead of having to use direct commands.

## What you can learn from using the project:

- How a realistic log pipeline simulation using Fluent Bit, Kafka, and Splunk is created.

- How to analyze/display sample mock SOAR/SIEM logs using Splunk's tools.

## Questions?

Feel free to open an issue or reach out via email: jayson.murphy99@gmail.com
