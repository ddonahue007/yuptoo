from confluent_kafka import Consumer
from yuptoo.lib.config import KAFKA_AUTO_COMMIT, INSIGHTS_KAFKA_ADDRESS, ANNOUNCE_TOPIC, kafka_auth_config


def init_consumer():
    connection_object = {
        'bootstrap.servers': INSIGHTS_KAFKA_ADDRESS,
        'group.id': 'qpc-group',
        'auto.offset.reset': 'earliest',
        'enable.auto.commit': KAFKA_AUTO_COMMIT
    }
    kafka_auth_config(connection_object)
    consumer = Consumer(connection_object)
    consumer.subscribe([ANNOUNCE_TOPIC])

    return consumer
