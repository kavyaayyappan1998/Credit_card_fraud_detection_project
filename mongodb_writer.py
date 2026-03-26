from kafka import KafkaConsumer
from pymongo import MongoClient
import json

# Connect to MongoDB
client = MongoClient('localhost', 27017)
db = client['fraud_detection']
collection = db['flagged_transactions']

# Kafka consumer
consumer = KafkaConsumer(
    'flagged_transactions',
    bootstrap_servers='localhost:9092',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

print("Listening for flagged transactions...")

for msg in consumer:
    transaction = msg.value
    collection.insert_one(transaction)
    print("Inserted:", transaction)