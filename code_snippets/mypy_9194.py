def is_dev() -> str:
    return settings.get("environment") == "dev"
