from kafka import KafkaConsumer

def mgs_kafka():
    consumer = KafkaConsumer(
        'test_msg',
        bootstrap_servers='harmless-llama-10955-eu2-kafka.upstash.io:9092',
        sasl_mechanism='SCRAM-SHA-256',
        security_protocol='SASL_SSL',
        sasl_plain_username='aGFybWxlc3MtbGxhbWEtMTA5NTUkSWlsftAT5bb2G5AxTAXsG48EcNi8Pk20sDU',
        sasl_plain_password='YzI5N2JhYzQtZGJjMi00YjJmLThjOTQtMTEwNzhiZjQ3MmNm',
        group_id='YOUR_CONSUMER_GROUP',
        auto_offset_reset='earliest'
    )

    try:
        for message in consumer:
            print(f"Received message: {message.value}")
    except KeyboardInterrupt:
        pass
    finally:

        consumer.close()