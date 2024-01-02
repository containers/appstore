from kafka import KafkaAdminClient
from kafka.admin import NewTopic
from kafka.admin import KafkaAdminClient, NewTopic


class Admin:
    def __init__(self, brokers):
        self.admin = KafkaAdminClient(bootstrap_servers=brokers)

    def topic_exists(self, topic_name):
        topics_metadata = self.admin.list_topics()
        return topic_name in topics_metadata

    def create_topic(self, topic_name, num_partitions=1, replication_factor=1):
        if not self.topic_exists(topic_name):
            new_topic = NewTopic(
                name=topic_name,
                num_partitions=num_partitions,
                replication_factor=replication_factor,
            )
            self.admin.create_topics([new_topic])
            print(f"Topic {topic_name} created.")
        else:
            print(f"Topic {topic_name} already exists.")

    def close(self):
        self.admin.close()
