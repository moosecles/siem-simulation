# app.py
import time
import json
import random
from datetime import datetime, timezone

log_levels = [
    "INFO",
    "WARNING",
    "ERROR",
]


def generate_log():
    log = {
        "timestamp": datetime.now().isoformat(),
        "level": random.choice(log_levels),
        "message": random.choice(
            [
                "User login successful",
                "User failed authentication",
                "Disk space running low",
                "Database connection failed",
                "Email sent to user",
            ]
        ),
        "user_id": random.randint(1000, 9999),
    }
    return log


with open("/logs/app.log", "a") as f:
    while True:
        log_entry = generate_log()
        f.write(json.dumps(log_entry) + "\n")
        f.flush()
        time.sleep(5)
