from kafka import KafkaProducer
import json


class Producer:
    def __init__(self, brokers, topic):
        self.topic = topic
        self.producer = KafkaProducer(
            bootstrap_servers=brokers,
            value_serializer=lambda v: json.dumps(v).encode("utf-8"),
        )

    def send_message(self, user, message):
        self.producer.send(self.topic, {"user": user, "message": message})
        self.producer.flush()

    def close(self):
        self.producer.close()
