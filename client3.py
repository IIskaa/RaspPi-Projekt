import paho.mqtt.client as mqtt
import time 
import struct
import os
import glob
import time
import datetime

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

# Create a MQTT client and register a callback
# for connect events
client = mqtt.Client()
client.on_connect = on_connect

# Connect to a broker
client.connect("192.168.137.1", port=1883, keepalive=60)

# Start a background loop that handles all
# communication with the MQTT broker
client.loop_start()


os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

#Hittar temperaturgivarens  sokvag
base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'

def read_temp_raw():
    with open(device_file, "r") as temp_read_file:
        return temp_read_file.readlines()

#Omvandlar temperaturdatan till nagot lasbart
def temp_c():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(1)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = int(temp_string)
        return temp_c

timenow = datetime.datetime.now()

# send a random value every second
while True:
    time.sleep(1)
    id = 3
    temp = temp_c()
    print(temp)
    print(str(temp))

    data = struct.pack("!QIB", id, temp)

    # publish the data to the topic some/topic
    # using the packed struct as payload and
    # MQTT QoS set to 1
    client.publish("yrgo/hispi/iksa/hh", payload=data, qos=1)