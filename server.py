import struct
import paho.mqtt.client as mqtt
import struct
# The callback for when the client connects to the server
def on_connect(client, userdata, flags, rc):
# Subscribing in on_connect() means that
# reconnect will renew then subscriptions
    client.subscribe("yrgo/hispi/iksa/hh", qos=1)
# The callback for receiving message
def on_message(client, userdata, msg):
    id, temp = struct.unpack("!bq", msg.payload)
    print(f"message: {id}, {temp}")
# Create a MQTT client with callbacks
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("192.168.137.1", port=1883, keepalive=60)
# Blocking call that processes network traffic, dispatches
# callbacks and handles reconnecting.

client.loop_forever()