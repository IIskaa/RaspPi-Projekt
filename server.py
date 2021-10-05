import struct
import paho.mqtt.client as mqtt
import struct
from datetime import datetime

# The callback for when the client connects to the server
def on_connect(client, userdata, flags, rc):
# Subscribing in on_connect() means that
# reconnect will renew then subscriptions
    client.subscribe("yrgo/hispi/iksa/hh", qos=1)
# The callback for receiving message
def on_message(client, userdata, msg):
    id, timestamp, index, temp, enhet = struct.unpack("!QIBiB", msg.payload)
    time = datetime.fromtimestamp(timestamp)
    enhet = enhet + 55
    print(f"message: {id}, {time}, {index}, {temp} {chr(enhet)})")
# Create a MQTT client with callbacks
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("172.20.10.5", port=1883, keepalive=60)
# Blocking call that processes network traffic, dispatches
# callbacks and handles reconnecting.

client.loop_forever()