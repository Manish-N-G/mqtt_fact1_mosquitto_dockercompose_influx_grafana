#import paho.mqtt.client as mqtt

"""

# MQTT broker configuration
broker_address = "mqtt-broker-fact1"
#mqtt-broker-fact1 , mosquitto_fact1
port = 1883
topic = "paper_wifi/test/#"
#topic = "test/topic"

# Callback when a message is received
def on_message(client, userdata, msg):
    value = int(msg.payload)
    print(f"Received: {value}")
    # Implement your logic here, modify the math function as necessary

# MQTT client setup
client = mqtt.Client()
client.connect(broker_address, port, 60)

# Set the callback function for when a message is received
client.on_message = on_message

# Subscribe to the topic
client.subscribe(topic)

# Loop to keep the script running
client.loop_forever()

"""
"""
import time

with open('/app/output.txt', 'w') as f:
    f.write("Script started\n")
    while True:
        f.write("Hello, world!\n")
        time.sleep(10)

"""

import time
import subprocess
import random

print("hello world")
i=0 
while i<10:
  try:
    rand = random.randint(0,120)
    'print("hello world")'
    result= subprocess.check_output(['ls', '-l'])
    #result2 = subprocess.check_output(['sudo', 'docker', 'container', 'exec', 'mqtt-broker-fact1', 'mosquitto_sub', '-t', '"paper_wifi/test/"' ])
    print(result.decode('utf-8'))
    print(f"my random value: {rand}")
    i = i +1
    time.sleep(2)
  except subprocess.CalledProcessError as e:
    print("some error: {e}")
    i = i+1
    time.sleep(2)