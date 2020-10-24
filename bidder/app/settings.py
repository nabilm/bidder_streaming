import os


KAFKA_HOST = os.environ.get("KAFKA_HOST")

MONGODB_DSN = os.environ.get("MONGODB_DSN")

EVENTS_TOPIC = os.environ.get("EVENTS_TOPIC")

USERS_COLLECTION = os.environ.get("USERS_COLLECTION")

ITEMS_COLLECTION = os.environ.get("ITEMS_COLLECTION")

EVENTS_COLLECTION = os.environ.get("EVENTS_COLLECTION")

MONGODB_STORAGE = os.environ.get("MONGODB_STORAGE")

EVENTS_INVALID_TOPIC = os.environ.get("EVENTS_INVALID_TOPIC")
