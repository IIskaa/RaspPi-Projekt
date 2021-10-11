from flask import Flask, render_template, flash
import datetime

text_add= "D:/Yrgo/Ela20/Hårdvarunära Programering/GruppProjekt/RaspPi-Projekt/flask-example/vizualisr/temptext.txt"
# This creates the flask application and configures it
# flask run will use this to start the application properly
app = Flask(__name__)
app.config.from_mapping(
    # This is the session key. It should be a REALLY secret key!
    SECRET_KEY="553e6c83f0958878cbee4508f3b28683165bf75a3afe249e"
)

# The mapping of units in accordance with our specification
UNITS = {
    0: "°C",
    1: "RH"
}


# This is a placeholder that returns a fixed set of meters
# in a proper system this would look in a database or in
# the file system for a list of meters in the system
def get_id_data():
    id_list=set()
    with open(text_add,"r") as file:
        for line in file:
            data = line.split(";")
            id = data[0]
            index = data[2]
            id_list.add((id, index))
    return list(id_list)

# [  (12233, 0), (12233, 1), (3434434, 0)]

def get_meters():
    list_of_sensors = get_id_data()
    return list_of_sensors


# This is a placeholder that returns a fixed set of 
# measurement data. In a proper system this would read
# the data from a database or the file system
def get_measurements(meter, channel):

    # this just generates a fixed set of measurement values
    # to have something to show...
    temp_list = set()
    with open(text_add, "r") as file:
        for line in file:
            data = line.split(";")
            time = data[1]
            temp = data[3]
            enhet = data[4]
            temp = float(temp)
            temp = temp/1000
            if meter == data[0] and channel == data[2]: 
                temp_list.add((time, temp, enhet))
    return list(temp_list)

# @app.route registers a handler for a specific URL
# in this case the URL / (i.e. the root of the server)

@app.route("/")
def start_page():
    meters = get_meters()
    return render_template("start.html", meters=meters)

# using @app.route with <something> makes "something" into
# a path variable. In the case /meter/1234/channel/5678
# the meter-argument would be set to (the string!) 1234
# and channel to 5678.

@app.route("/meter/<meter>/channel/<channel>")
def show_measurements(meter, channel):
    measurements = get_measurements(meter, channel)
    return render_template("meter.html", meter=meter, channel=channel, measurements=measurements)