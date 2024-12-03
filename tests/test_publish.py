# test_publish.py

import paho.mqtt.client as mqtt
import json

def publish_test_message():
    client = mqtt.Client()
    client.connect("test.mosquitto.org", 1883, 60)
    
    test_data = {
        "id": "test123",
        "numberOfChildren": 2,
        "familyComposition": "single",
        "familyUnitInPayForDecember": True
    }
    
    client.publish("BRE/calculateWinterSupplementInput/HelloTest12", json.dumps(test_data))
    client.loop_start()

if __name__ == "__main__":
    publish_test_message()
