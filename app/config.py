"""Configuration loading (PyYAML)."""
import yaml


def load_settings(text):
    # No Loader argument: warns on 5.1+, still works until 6.0 made Loader required.
    return yaml.load(text)


def load_safe(text):
    return yaml.safe_load(text)
