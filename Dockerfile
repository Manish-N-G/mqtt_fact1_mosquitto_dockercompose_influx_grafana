# Use the official Python image
#FROM python:3.9 --
FROM eclipse-mosquitto:latest
# apt-get install -y apt-utils nano python3 &&
    #  apt-get update  &&"

# Install the Mosquitto MQTT client
RUN apk update && \
    apk add nano python3
# apk works with busybox, which is found in the elipse container.It allows us to use some of the files.

# Set the working directory
#WORKDIR /app   --

# Copy the Python script into the container
#COPY publisher.py .    --

# Set the command to run the Python script
#CMD ["python", "publisher.py"] --
