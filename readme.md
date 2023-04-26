MQTT Explorer with PyQt5

This project is an MQTT explorer built using Python and PyQt5. It allows you to connect to an MQTT broker, subscribe to topics, and display the received messages in a tree view. The application also logs the received messages and object creations as JSON objects to a file called mqtt_json.log.

Prerequisites

Python 3.6 or higher
PyQt5
paho-mqtt
Installation

Clone the repository:

Create a virtual environment and activate it inside the repo folder:

python3 -m venv venv
source venv/bin/activate

Install the required Python packages:

pip install -r requirements.txt

Running the Application

Start the application by running the following command:

python main.py

The application will connect to the MQTT broker specified in the mqtt_client.py file. The default broker address is 45.76.236.64 and the default port is 1883.

Once the application is running, it will display the received MQTT messages in a tree view. You can click on an item in the tree view to see its payload in the bottom part of the window.

To stop the application, simply close the main window.

Troubleshooting

If you are experiencing any issues with the application, you can check the mqtt_json.log file for any logged messages or exceptions. This file is generated when the application is run and can help you identify any problems.