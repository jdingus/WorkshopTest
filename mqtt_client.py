import logging
import paho.mqtt.client as mqtt
from gui import update_gui

# Define the MQTT broker address and port
broker_address = "45.76.236.64"
broker_port = 1883

# Create the MQTT client object
client = mqtt.Client()

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        logging.info("Connected to MQTT broker")
        client.subscribe("#")
    else:
        logging.error(f"Connection to MQTT broker failed with error code: {rc}")

client.on_connect = on_connect

def on_message(client, userdata, message):
    topic = message.topic
    try:
        payload = message.payload.decode('utf-8')
    except UnicodeDecodeError:
        payload = message.payload.decode('latin-1')

    print(f"Received message: {topic} - {payload}")
    update_gui(topic, payload)

# Set the message received callback function
client.on_message = on_message

# Connect to the MQTT broker
client.connect(broker_address, broker_port)
