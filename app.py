"""Entry point: imports every module so reachability sees the packages in use."""
import six

from app import cache, client, config, decoy, http, templates


def main():
    _ = (six, cache, client, config, decoy, http, templates)
    print("sca test app")


if __name__ == "__main__":
    main()
