from kafka import KafkaConsumer


# Должен работать из watcher
consumer = KafkaConsumer(
    'dbserver1.inventory.customers', # topics
    bootstrap_servers=['kafka:9092'], #connect
    auto_offset_reset='earliest',
    enable_auto_commit=False
)

print(consumer.bootstrap_connected())
print(consumer.subscription())
print(len(consumer))
#for message in consumer:
#    print(message)