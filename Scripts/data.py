import requests
import time
import calls
import targets

url = targets.thinsboard_api()
headers = {'Content-Type': 'application/json'}

while True:
    # Generate some data to send
    data = {}
    data['temperature'] = calls.get_ambient_temperature()
    data['cpu_temp'] = calls.get_cpu_temperature()
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


    # Send the data to Thingsboard API
    response = requests.post(url, json=data, headers=headers)

    # Check for request success
    if response.status_code == 200:
        print("Data sent successfully")
    else:
        print("Failed to send data")

    # Wait for some time in seconds before sending the next data
    time.sleep(0.1)
