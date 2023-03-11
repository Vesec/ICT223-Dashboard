import paho.mqtt.client as mqtt
import json
import time
import calls
import targets


def telemetry_array():
    data = {}
    data['temperature'] = calls.get_ambient_temperature()
    data['cpu_temp'] = calls.get_cpu_temperature()
    data['cor_amb_temp'] = calls.get_corrected_ambient_temperature()
    data['cpu_use'] = calls.get_cpu_use()
    data['pressure'] = calls.get_pressure()
    data['humidity'] = calls.get_humidity()
    data['ram_total'] = calls.get_ram_info()[0]
    data['ram_used'] = calls.get_ram_info()[1]
    data['ram_free'] = calls.get_ram_info()[2]
    data['disk_total'] = calls.get_disk_space()[0]
    data['disk_used'] = calls.get_disk_space()[1]
    data['disk_free'] = calls.get_disk_space()[2]
    data['disk_used_percentage'] = calls.get_disk_space()[3]
    data['acceleration'] = calls.get_accelerometer_data()
    data['pitch'] = calls.get_orientation_degrees()[0]
    data['roll'] = calls.get_orientation_degrees()[1]
    data['yaw'] = calls.get_orientation_degrees()[2]
    return data


# Define function to handle MQTT connection events
def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT broker with result code "+str(rc))

# Define function to handle MQTT publish events
def on_publish(client, userdata, mid):
    print("Data sent to Thingsboard with message id "+str(mid))

def device_connection():
    # Create MQTT client instance
    client = mqtt.Client()

    # Set MQTT client callbacks
    client.on_connect = on_connect
    client.on_publish = on_publish

    # Connect to Thingsboard MQTT broker
    broker, port, token, topic = targets.thingsboard_api_mqtt()
    client.username_pw_set(token)
    client.connect(broker, port, 60)

    return client, topic

def send_device_telemetry():
# Continuously send telemetry data
    while True:
        try:

            #Grab Connection info
            mqtt_client, mqtt_topic = device_connection()

            # Prepare telemetry data to send
            telemetry_data = telemetry_array()

            # Convert telemetry data to JSON format
            payload = json.dumps(telemetry_data)

            # Publish telemetry data to Thingsboard MQTT broker
            mqtt_client.publish(mqtt_topic, payload)

            # Print telemetry data
            print(telemetry_data)

            # Wait for some time before sending next telemetry data
            
            time.sleep(1)

        except KeyboardInterrupt:
            # If the user presses Ctrl-C, disconnect from MQTT broker and exit the script
            mqtt_client.disconnect()
            break

send_device_telemetry()