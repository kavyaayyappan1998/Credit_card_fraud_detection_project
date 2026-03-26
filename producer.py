from faker import Faker
from kafka import KafkaProducer
import random
import json
import time

fake = Faker()

def generate_transaction():
    transaction = {
        "card_number": fake.credit_card_number(),
        "amount": round(random.uniform(1, 1000), 2),
        "timestamp": fake.date_time().isoformat(),
        "location": {
            "city": fake.city(),
            "state": fake.state_abbr()
        },
        "merchant": fake.company(),
        "merchant_category": random.choice([
            "grocery",
            "electronics",
            "restaurant",
            "fuel",
            "travel",
            "fashion"
        ]),
        "currency": "USD",
        "device_type": random.choice(["mobile", "web", "pos"])
    }
    return transaction

producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

print("Sending transactions to Kafka topic: credit_card_transactions")

while True:
    transaction = generate_transaction()
    producer.send("credit_card_transactions", value=transaction)
    producer.flush()
    print("Sent:", transaction)
    time.sleep(1)