from confluent_kafka import Producer
import pandas as pd

# Initialize Kafka producer
producer = Producer({'bootstrap.servers': 'localhost:9092'})

# Function to publish message to Kafka topic
def publish_message(topic, message):
    producer.produce(topic, message.encode('utf-8'))
    producer.flush()

# Function to read CSV file and publish its data to Kafka topic
def publish_csv_to_kafka(csv_file, topic):
    try:
        # Read CSV file
        df = pd.read_csv(csv_file)

        # Publish each row of CSV to Kafka topic
        for index, row in df.iterrows():
            # Convert row to JSON format (you can adjust this according to your data structure)
            json_data = row.to_json()
            # Publish data to Kafka
            publish_message(topic, json_data)
    
    except Exception as ex:
        print('Exception in publishing CSV to Kafka:', ex)
    finally:
        producer.flush()

# Example usage
if __name__ == '__main__':
    # Path to your CSV file
    csv_file_path = 'your_file.csv'
    
    # Kafka topic to publish to
    kafka_topic = 'your_topic_name'
    
    # Publish CSV data to Kafka topic
    publish_csv_to_kafka(csv_file_path, kafka_topic)

