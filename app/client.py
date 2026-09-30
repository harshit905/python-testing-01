"""Outbound API client (requests)."""
import requests


def fetch(url):
    return requests.get(url, timeout=5).json()


def session():
    s = requests.Session()
    s.headers.update({"User-Agent": "sca-test/1.0"})
    return s
