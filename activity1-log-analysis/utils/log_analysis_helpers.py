"""Helper utilities for Activity 1 log analysis"""
import re
from collections import Counter

def parse_log_line(line):
    """Simple parser that extracts IP and timestamp if present."""
    # naive example
    ip_match = re.search(r"(\d+\.\d+\.\d+\.\d+)", line)
    ts_match = re.search(r"\d{2}/[A-Za-z]{3}/\d{4}", line)
    return {"ip": ip_match.group(0) if ip_match else None, "date": ts_match.group(0) if ts_match else None}

def count_ips(lines):
    return Counter(parse_log_line(l)["ip"] for l in lines if parse_log_line(l)["ip"])
