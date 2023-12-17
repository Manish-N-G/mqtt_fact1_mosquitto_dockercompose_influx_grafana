import json
import socket #added
import threading #added

# Function to check values and send alerts
def check_values():
    threshold_value = 120

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('localhost', 5555)) #could be soemthing like: server_ip = "127.0.0.1" port = 8000
        s.listen()  #listen(0) or listen(1)

        while True:
            conn, addr = s.accept()
            with conn:
                print('Connected by', addr)   # {conn[0]}:{addr[1]}
            #while True:
                data = conn.recv(1024)  # then after data=data.decode("utf-8") converts bytes to string
                if not data:     # send rewponse to the client which acknowleddges thet the conenction should be closed and break out of the loop
                    break   # of if could have been if data.lower()=="close":  // conn.send("closed".encode("utf-8")) // break
                
                # can add a print here. print(f"received: {data}"")
                values = json.loads(data.decode('utf-8'))

                # Check if values exceed the threshold
                if values["humidity"] > threshold_value or values["temperature"] > threshold_value or values["battery_voltage_mv"] > threshold_value:
                    # Send alert back to python1.py
                    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as alert_socket:
                        alert_socket.connect(('localhost', 5556))
                        alert_message = 'Above threshold!'
                        alert_socket.sendall(alert_message.encode('utf-8'))

# Create a thread for checking values
check_thread = threading.Thread(target=check_values)

# Start the thread
check_thread.start()

# Wait for the thread to finish (if needed)
check_thread.join()
