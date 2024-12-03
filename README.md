# Winter Supplement Calculator - MQTT Client

This project is a Python-based MQTT client that calculates winter supplement based on received messages and publishes the results to the specified MQTT topics. The client listens to messages on the `BRE/calculateWinterSupplementInput/HelloTest12` topic and publishes calculated results to `BRE/calculateWinterSupplementOutput/HelloTest12`.

## Prerequisites

Before running the project, ensure that you have the following installed:

- Python 3.8 or above
- `pip` (Python package installer)

## Setup

1. **Clone the repository**:

    ```bash
    git clone <repository-url>
    cd <project-directory>
    ```

2. **Create a Virtual Environment**:

    It's highly recommended to use a virtual environment to isolate your dependencies.

    - For macOS/Linux:

      ```bash
      python3 -m venv venv
      ```

    - For Windows:

      ```bash
      python -m venv venv
      ```

3. **Activate the Virtual Environment**:

    - For macOS/Linux:

      ```bash
      source venv/bin/activate
      ```

    - For Windows:

      ```bash
      .\venv\Scripts\activate
      ```

4. **Install Dependencies**:

    Install the required Python dependencies using `pip`. These dependencies are defined in the `requirements.txt` file.

    ```bash
    pip install -r requirements.txt
    ```

5. **Running the MQTT Client**:

    To start the MQTT client, run the following command:

    ```bash
    python app/mqtt_client.py
    ```

    The client will connect to the Mosquitto MQTT broker, subscribe to the `BRE/calculateWinterSupplementInput/HelloTest12` topic, and begin processing incoming messages.

## Files Overview

- **rules_engine.py**: Contains the logic to calculate the winter supplement based on received input.
- **app/mqtt_client.py**: The MQTT client that subscribes to the topic and publishes results.

## Logging

The MQTT client uses Python's built-in `logging` module to log important events such as receiving messages, processing them, and publishing results.

## Broker Configuration

This client connects to the public Mosquitto MQTT broker (`test.mosquitto.org`) by default. If you need to use a different broker, modify the connection settings in the `mqtt_client.py` file.

## Troubleshooting

- If the client fails to connect, ensure that the MQTT broker is accessible from your network.
- Check the topic names and ensure that messages are being published to the correct topic.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
