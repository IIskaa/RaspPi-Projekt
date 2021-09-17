import paho.mqtt.client as mqtt
import random

slump = random.randint(0, 100)
# Create a MQTT client and register a callback for connect events
client = mqtt.Client()
# Connect to a broker
client.connect("broker.hivemq.com", port=1883, keepalive=60)
# Start a background loop that handles all broker communication
client.loop_start()
# Send the message
msg = client.publish("yrgo/hispi/iksa/hello", payload=f"slump tal = {slump}", qos=1)
msg = client.publish("yrgo/hispi/iksa/annat", payload=f"haha", qos=1)
# If python exits immediately it does not have the time to send
# the message
msg.wait_for_publish()
client.disconnect()