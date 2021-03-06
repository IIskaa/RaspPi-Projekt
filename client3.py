import paho.mqtt.client as mqtt
import time 
import struct
import os
import glob
import datetime


def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

client = mqtt.Client()
client.on_connect = on_connect

client.connect("192.168.137.1", port=1883, keepalive=60)

client.loop_start()


os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')


base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'
device_ID = device_folder.replace(base_dir, '')
ID = device_ID.replace('-','')
ID = int(ID, 16)


def read_temp_raw():
    with open(device_file, "r") as temp_read_file:
        return temp_read_file.readlines()

def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(1)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = temp_string
        return temp_c

while True:

    time.sleep(1)
    index = int(0)
    enhet = "C"
    enhet= int(enhet, 16)
    timestamp = int(datetime.datetime.now().timestamp())   
    temp = int(read_temp(), 16)
    print(temp)
    print(str(temp))

    data = struct.pack("!QIBiB", ID, timestamp, index, temp, enhet)

    client.publish("yrgo/hispi/iksa/hh", payload=data, qos=1)