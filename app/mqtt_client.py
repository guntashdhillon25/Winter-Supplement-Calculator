import paho.mqtt.client as mqtt
import logging
from rules_engine import on_message

# Setup logging
logging.basicConfig(level=logging.DEBUG)

# Define the on_connect callback function
def on_connect(client, userdata, flags, rc):
    logging.info(f"Connected with result code: {rc}")
    if rc == 0:  # Successful connection
        client.subscribe("BRE/calculateWinterSupplementInput/HelloTest12")
    else:
        logging.error(f"Failed to connect, return code {rc}")

# Define MQTT client
client = mqtt.Client()

# Define callbacks
client.on_connect = on_connect
client.on_message = on_message

def connect_and_subscribe():
    client.connect("test.mosquitto.org", 1883, 60)
    client.loop_forever()

if __name__ == "__main__":
    connect_and_subscribe()
