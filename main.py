import sys
import logging
from mqtt_client import client
from gui import app, tree_view

# Configure logging
logging.basicConfig(filename="mqtt_json.log", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Start the MQTT client loop in a separate thread
client.loop_start()

# Run the PyQt application loop
sys.exit(app.exec_())
