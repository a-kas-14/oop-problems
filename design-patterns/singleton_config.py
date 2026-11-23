import json
import os


class ConfigManager:
    _instance = None   # the one and only instance, shared by everyone

    def __init__(self):
        if ConfigManager._instance is not None:
            raise RuntimeError("Use ConfigManager.get_instance() instead")
        # config.json sits next to this script
        path = os.path.join(os.path.dirname(__file__), "config.json")
        print("Loading config from file...")
        with open(path, "r") as f:
            self._config = json.load(f)

    @classmethod
    def get_instance(cls):
        # Create the instance only the first time
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    # get("database.host") -> config["database"]["host"]
    def get(self, key, default=None):
        value = self._config
        for part in key.split("."):
            if isinstance(value, dict) and part in value:
                value = value[part]
            else:
                return default
        return value

    # set("payment.environment", "production") -> visible to everyone
    def set(self, key, value):
        parts = key.split(".")
        current = self._config
        for part in parts[:-1]:
            current = current.setdefault(part, {})
        current[parts[-1]] = value


# database.py
def connect_database():
    config = ConfigManager.get_instance()
    print(f"Connecting to database at {config.get('database.host')}:{config.get('database.port')}")


# email_service.py
def send_email(to: str, subject: str):
    config = ConfigManager.get_instance()
    print(f"Sending email from {config.get('email.sender')} via {config.get('email.smtp_host')}")


# payment_service.py
def process_payment(amount: float):
    config = ConfigManager.get_instance()
    print(f"Processing {amount}€ in {config.get('payment.environment')} mode")


# app.py
def start_application():
    config = ConfigManager.get_instance()
    print(f"Starting {config.get('app.name')} (debug={config.get('app.debug')})")


if __name__ == "__main__":
    start_application()
    connect_database()
    send_email("user@test.com", "Welcome")
    process_payment(99.99)

    # Same object everywhere
    a = ConfigManager.get_instance()
    b = ConfigManager.get_instance()
    print("Same instance everywhere:", a is b)

    # A change made in one place is seen everywhere
    a.set("payment.environment", "production")
    process_payment(50.0)
