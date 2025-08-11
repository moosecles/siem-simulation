# app.py
import time
import json
import random
from datetime import datetime, timezone

users = [
    {"user": "jsmith", "user_id": 1045, "email": "jsmith@corp.com"},
    {"user": "mcho", "user_id": 1091, "email": "mcho@corp.com"},
    {"user": "awilson", "user_id": 1172, "email": "awilson@corp.com"},
    {"user": "dpatel", "user_id": 1210, "email": "dpatel@corp.com"},
    {"user": "knguyen", "user_id": 1324, "email": "knguyen@corp.com"},
    {"user": "tlee", "user_id": 1342, "email": "tlee@corp.com"},
    {"user": "bramirez", "user_id": 1399, "email": "bramirez@corp.com"},
    {"user": "lmartin", "user_id": 1415, "email": "lmartin@corp.com"},
    {"user": "zcohen", "user_id": 1483, "email": "zcohen@corp.com"},
    {"user": "hwang", "user_id": 1532, "email": "hwang@corp.com"},
    {"user": "janderson", "user_id": 1612, "email": "janderson@corp.com"},
    {"user": "rtaylor", "user_id": 1673, "email": "rtaylor@corp.com"},
    {"user": "cmoore", "user_id": 1698, "email": "cmoore@corp.com"},
    {"user": "lgarcia", "user_id": 1741, "email": "lgarcia@corp.com"},
    {"user": "hrodriguez", "user_id": 1793, "email": "hrodriguez@corp.com"},
    {"user": "amoore", "user_id": 1820, "email": "amoore@corp.com"},
    {"user": "bwhite", "user_id": 1884, "email": "bwhite@corp.com"},
    {"user": "jmiller", "user_id": 1912, "email": "jmiller@corp.com"},
    {"user": "ehall", "user_id": 1965, "email": "ehall@corp.com"},
    {"user": "jtan", "user_id": 2011, "email": "jtan@corp.com"},
    {"user": "nperez", "user_id": 2059, "email": "nperez@corp.com"},
    {"user": "slopez", "user_id": 2103, "email": "slopez@corp.com"},
    {"user": "akim", "user_id": 2157, "email": "akim@corp.com"},
    {"user": "rclark", "user_id": 2190, "email": "rclark@corp.com"},
    {"user": "mthomas", "user_id": 2251, "email": "mthomas@corp.com"},
]

log_templates = [
    {
        "message": "User login successful",
        "action": "success",
        "signature": "Accepted password",
        "severity": "low",
        "log_level": "INFO",
    },
    {
        "message": "User failed authentication",
        "action": "failure",
        "signature": "Failed password",
        "severity": "medium",
        "log_level": "WARNING",
    },
    {
        "message": "User account locked after multiple failures",
        "action": "failure",
        "signature": "Account locked",
        "severity": "high",
        "log_level": "ERROR",
    },
    {
        "message": "Password reset requested",
        "action": "success",
        "signature": "Password reset",
        "severity": "low",
        "log_level": "INFO",
    },
    {
        "message": "Suspicious login location detected",
        "action": "failure",
        "signature": "Geo anomaly",
        "severity": "high",
        "log_level": "ERROR",
    },
    {
        "message": "Brute force login attempt detected",
        "action": "failure",
        "signature": "Excessive attempts",
        "severity": "high",
        "log_level": "ERROR",
    },
    {
        "message": "VPN connection established",
        "action": "success",
        "signature": "VPN login",
        "severity": "low",
        "log_level": "INFO",
    },
    {
        "message": "VPN authentication failure",
        "action": "failure",
        "signature": "VPN auth failed",
        "severity": "medium",
        "log_level": "WARNING",
    },
    {
        "message": "Admin privilege granted",
        "action": "success",
        "signature": "Privilege escalation",
        "severity": "high",
        "log_level": "WARNING",
    },
    {
        "message": "User removed from group",
        "action": "success",
        "signature": "Group removal",
        "severity": "low",
        "log_level": "INFO",
    },
    {
        "message": "Service account used for login",
        "action": "success",
        "signature": "Service account login",
        "severity": "medium",
        "log_level": "INFO",
    },
    {
        "message": "Unusual login time detected",
        "action": "failure",
        "signature": "Login anomaly",
        "severity": "high",
        "log_level": "WARNING",
    },
    {
        "message": "Multi-factor authentication passed",
        "action": "success",
        "signature": "MFA passed",
        "severity": "low",
        "log_level": "INFO",
    },
    {
        "message": "Multi-factor authentication failed",
        "action": "failure",
        "signature": "MFA failed",
        "severity": "medium",
        "log_level": "WARNING",
    },
    {
        "message": "User access revoked",
        "action": "success",
        "signature": "Account disabled",
        "severity": "medium",
        "log_level": "INFO",
    },
]


src_ips = [
    "192.168.1.10",
    "10.0.0.24",
    "172.16.5.12",
    "203.0.113.55",
    "198.51.100.22",
    "10.15.23.5",
    "172.20.12.34",
    "8.8.8.8",
    "156.154.70.1",
    "185.199.108.1",
    "45.77.54.203",
    "212.47.227.113",
    "51.38.121.179",
    "23.88.10.123",
    "162.243.1.101",
]

apps = [
    "ssh",
    "vpn",
    "okta",
    "windows_login",
    "web_portal",
    "rdp",
    "azure_ad",
    "splunkd",
]


def generate_log():
    template = random.choice(log_templates)
    user_info = random.choice(users)

    log = {
        "_time": datetime.now(timezone.utc).isoformat(),
        "log_level": template["log_level"],
        "message": template["message"],
        "action": template["action"],
        "signature": template["signature"],
        "severity": template["severity"],
        "user": user_info["user"],
        "user_id": user_info["user_id"],
        "email": user_info["email"],
        "src": random.choice(src_ips),
        "dest": "auth-server-01",
        "app": random.choice(apps),
        "vendor": "acme_corp",
        "product": "acme_login",
    }

    return log


with open("/logs/app.log", "a") as f:
    while True:
        log_entry = generate_log()
        f.write(json.dumps(log_entry) + "\n")
        f.flush()
        time.sleep(20)
