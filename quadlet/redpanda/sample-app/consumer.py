from kafka import KafkaConsumer
import json
import uuid


class Consumer:
    def __init__(self, brokers, topic, group_id=None):
        if group_id is None:
            group_id = str(uuid.uuid4())
        self.consumer = KafkaConsumer(
            topic,
            bootstrap_servers=brokers,
            group_id=group_id,
            value_deserializer=lambda m: json.loads(m.decode("utf-8")),
        )

    def print_messages(self):
        for msg in self.consumer:
            print(f"{msg.value['user']}: {msg.value['message']}")

    def close(self):
        self.consumer.close()
