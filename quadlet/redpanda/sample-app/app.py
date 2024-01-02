import json
import uuid
import threading
from admin import Admin
from producer import Producer
from consumer import Consumer

brokers = ["localhost:9092"]
topic = "chat"


def consumer_thread(consumer):
    consumer.print_messages()


if __name__ == "__main__":
    admin = Admin(brokers)
    if not admin.topic_exists(topic):
        print(f"Topic {topic} does not exist. Creating...")
        admin.create_topic(topic)
    username = input("Enter your username: ")
    producer = Producer(brokers, topic)
    consumer = Consumer(brokers, topic)
    consumer_thread = threading.Thread(target=consumer_thread, args=(consumer,))
    consumer_thread.daemon = True
    consumer_thread.start()
    print("Type your message and press enter to send. Press Ctrl-C to quit.")
    try:
        while True:
            message = input()
            producer.send_message(username, message)
    except KeyboardInterrupt:
        print("Exiting...")
        pass
    finally:
        print("Closing connections...")
        producer.close()
        consumer.close()
        admin.close()
