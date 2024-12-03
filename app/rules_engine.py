import json
import logging

def calc_supplement(data):
    topic_id = data["id"]
    base_amount = 0
    children_amount = 0
    is_eligible = data["familyUnitInPayForDecember"]

    if is_eligible:
        if data["familyComposition"] == "single" and data["numberOfChildren"] == 0:
            base_amount = 60
        elif data["familyComposition"] == "couple" and data["numberOfChildren"] == 0:
            base_amount = 120
        elif data["numberOfChildren"] > 0:
            base_amount = 120
            children_amount = 20 * data["numberOfChildren"]

    supplement_amount = base_amount + children_amount

    return {
        "id": topic_id,
        "isEligible": is_eligible,
        "baseAmount": float(base_amount),
        "childrenAmount": float(children_amount),
        "supplementAmount": float(supplement_amount)
    }

# def on_message(client, message):
#     data = json.loads(message.payload)
#     response = calc_supplement(data)
#     response_topic = "BRE/calculateWinterSupplementOutput/162064ac-bf36-4b19-967b-110026103ee2"
#     client.publish(response_topic, json.dumps(response))

def on_message(client, userdata, message):
    logging.debug(f"Received message: {message.payload}")
    data = json.loads(message.payload)
    result = calc_supplement(data)
    logging.debug(f"Calculated result: {result}")
    result_topic = "BRE/calculateWinterSupplementOutput/HelloTest12"
    client.publish(result_topic, json.dumps(result))
    logging.debug(f"Published result to topic: {result_topic}")
