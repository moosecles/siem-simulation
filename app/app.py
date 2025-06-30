# app.py
import time
import json
import random
from datetime import datetime, timezone

log_levels = [
    "INFO",
    "WARNING",
    "ERROR",
]  # Couple of random levels for logs that could pop up


def generate_log():  # Generates a JSON of logs that have a timestamp, level, user_Id, and random message
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


with open(
    "app.log", "a"
) as f:  # Creates and writes a log every two seconds to the file
    while True:
        log_entry = generate_log()
        f.write(json.dumps(log_entry) + "\n")
        f.flush()
        time.sleep(2)
