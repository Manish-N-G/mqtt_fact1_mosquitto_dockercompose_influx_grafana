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
""" this works very well
import time
import subprocess
import random

#result2 = subprocess.check_output(['sudo', 'docker', 'container', 'exec', 'mqtt-broker-fact1', 'mosquitto_pub', '-t', '"paper_wifi/test/"', '-m', '\'{"humidity":21, "temperature":21, "battery_voltage_mv":12}\'' ])
result2 = subprocess.check_output(['sudo', 'docker', 'container', 'exec', 'mqtt-broker-fact1', 'mosquitto_pub', '-t', 'paper_wifi/test/', '-m', '{"humidity": 21, "temperature": 21, "battery_voltage_mv": 11}'])
print(result2.decode('utf-8'))

print("hello world")
i=0 
while i<25:
  try:
    #rand_humidity = random.randint(0,12)
    rand_humidity = random.uniform(12,30)
    rand_temp = random.uniform(10,20)
    rand_voltage = random.uniform(5,120)
    'print("hello world")'
    #result= subprocess.check_output(['ls', '-l'])
    #result2 = subprocess.check_output(['sudo', 'docker', 'container', 'exec', 'mqtt-broker-fact1', 'mosquitto_sub', '-t', '"paper_wifi/test/"' ])
    #result2 = subprocess.check_output(['sudo', 'docker', 'container', 'exec', 'mqtt-broker-fact1', 'mosquitto_pub', '-t', '"paper_wifi/test/"', '-m', '\'{"humidity":21, "temperature":21, "battery_voltage_mv":11}\'' ])
    result2 = subprocess.check_output(['sudo', 'docker', 
                                       'container', 'exec', 'mqtt-broker-fact1', 
                                       'mosquitto_pub', '-t', 'paper_wifi/test/', '-m', 
                                       f'{{"humidity": {round(rand_humidity, 2)}, "temperature": {round(rand_temp,2)}], "battery_voltage_mv": 11.2}}'])
    #result2 = subprocess.check_output(['sudo', 'docker', 
    #                                   'container', 'exec', 'mqtt-broker-fact1', 
    #                                   'mosquitto_pub', '-t', 'paper_wifi/test/', '-m', 
    #                                   '{"humidity": {rand_humidity}}, "temperature": {rand_temp}], "battery_voltage_mv": 11.2}'])
    #                                   # this works
    print(result2)
    print(result2.decode('utf-8'))
    #print(f"my random value: {rand}")
    i = i +1
    time.sleep(2)
  except subprocess.CalledProcessError as e:
    print("some error: {e}")
    i = i+1
    time.sleep(2)

"""

import time
import subprocess
import random
import socket #added
import threading #added


result2 = subprocess.check_output(['sudo', 'docker', 'container', 'exec', 'mqtt-broker-fact1', 'mosquitto_pub', '-t', 'paper_wifi/test/', '-m', '{"humidity": 11, "temperature": 11, "battery_voltage_mv": 11}'])
print(result2.decode('utf-8'))
print("hello world start")

def send_values():
    i=0 
    while i<25:
        try:
            #rand_humidity = random.randint(0,12)
            rand_humidity = random.uniform(12,30)
            rand_temp = random.uniform(10,20)
            rand_voltage = random.uniform(5,120)
            print(f"hello world ongoing {i}")

            # send values to python2.py
            result2 = subprocess.check_output(['sudo', 'docker', 
                                            'container', 'exec', 'mqtt-broker-fact1', 
                                            'mosquitto_pub', '-t', 'paper_wifi/test/', '-m', 
                                            f'{{"humidity": {round(rand_humidity, 3)}, "temperature": {round(rand_temp,3)}], "battery_voltage_mv": {round(rand_voltage,3)}}}'])
            print(result2.decode('utf-8'))
            
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: # AF_ INET :ipv4, INET6 : ipv6 _UNIX : Unix sockets.. // Sock_strean is for tcp scokets
                s.connect(('localhost', 5555))
                message = f'{{"humidity": {round(rand_humidity, 4)}, "temperature": {round(rand_temp,4)}, "battery_voltage_mv": {round(rand_voltage,4)}}}'
                s.sendall(message.encode('utf-8'))

            i = i +1
            time.sleep(2)
        except subprocess.CalledProcessError as e:
            print("some error: {e}")
            i = i+1
            time.sleep(2)


# Create a thread for sending values
send_thread = threading.Thread(target=send_values)

# Start the thread
send_thread.start()

# Wait for the thread to finish (if needed)
send_thread.join()