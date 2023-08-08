from kafka import KafkaConsumer
#from kafka import TopicPartition
import re

topic = 'dbserver1.inventory.customers'
server = 'kafka:9092'
global consumer
consumer = KafkaConsumer(
    topic, # topics
    bootstrap_servers=[server], #connect
    auto_offset_reset='earliest'
)

#print(consumer.bootstrap_connected())
#print(consumer.subscription())

def one_poll():
    print('here')
    poll = consumer.poll(timeout_ms=1000, max_records=1)
    return poll

def poll2str(poll):
    print(' now here')

    bs_poll = str(poll)
    s_poll = re.sub(r'\\\"', '"', bs_poll) # removing '\' before '"'

    return s_poll

def get_one():
    return poll2str(one_poll())

def kafka_reconnect():
    global consumer
    
    del consumer

    consumer = KafkaConsumer(
    topic, # topics
    bootstrap_servers=[server], #connect
    auto_offset_reset='earliest'
    )

if __name__ == "__main__":
    print(get_one())



#partitions = consumer.partitions_for_topic(topic)
#print(partitions)

#message = next(consumer)
#print(message)
#print("*****************************************")

#msg = consumer.poll(timeout_ms=1000, max_records=1)
#print(msg)
#msg = consumer.poll(timeout_ms=1000, max_records=1)
#msg = consumer.poll(timeout_ms=1000, max_records=1)
#msg = consumer.poll(timeout_ms=1000, max_records=1)
#print(msg)


#msg = consumer.poll(timeout_ms=1000, max_records=1)
#print(msg)



#msg = consumer.seek_to_end(TopicPartition(topic, 0))
#print(msg)



