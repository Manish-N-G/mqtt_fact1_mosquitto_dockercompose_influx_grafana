import socket
import datetime

# Function to listen for alerts from python2.py
def listen_for_alerts():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('localhost', 5556))
        s.listen()

        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                
                alert_message = data.decode('utf-8')
                print(f"Received alert: {alert_message} at time {datetime.datetime.now()}")

# Run the alert listener
listen_for_alerts()