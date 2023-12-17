#import paho.mqtt.client as mqtt
#import time
"""
import random
import threading

# MQTT broker configuration
broker_address = "mqtt-broker-fact1"
#mqtt-broker-fact1 , mosquitto_fact1
port = 1883
topic = "paper_wifi/test/#"
#topic = "test/topic"

# Function to publish a random value every 10 seconds
def publish_random_value(client):
    while True:
        value = random.randint(1, 100)
        client.publish(topic, value)
        print(f"Published: {value}")
        time.sleep(10)

# MQTT client setup
client = mqtt.Client()
client.connect(broker_address, port, 60)

# Start a new thread to publish values
publish_thread = threading.Thread(target=publish_random_value, args=(client,))
publish_thread.start()

# Loop to keep the script running
client.loop_forever()
"""

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

"""
print("hello world")
i=0 
while i<10:
    print("hello world")
    i = i +1

