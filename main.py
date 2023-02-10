import json
import requests
import time
import os
import calls

# Constants
INTERVAL            = 3  #Data capture and upload interval in seconds.
API_KEY             = "s47B3i4t0oNlwFl67D5u"  #Thingsboard Token
THINGSBOARD_HOST    = "10.0.0.95:8080"  #Thingsboard server address and port.

thingsboard_url     = "http://{0}/api/v1/{1}/telemetry".format(THINGSBOARD_HOST, API_KEY)


data = {}
next_reading = time.time()

try:
    while True:
        data = {}
        data['temperature'] = calls.get_temperature()
        data['pressure'] = calls.get_pressure()
        data['humidity'] = calls.get_humidity()
        data['cpu_temp'] = calls.getCPUtemperature()
        data['cpu_use'] = calls.getCPUuse()
        data['ram_total'] = calls.getRAMinfo()[0]
        data['ram_used'] = calls.getRAMinfo()[1]
        data['ram_free'] = calls.getRAMinfo()[2]
        data['disk_total'] = calls.getDiskSpace()[0]
        data['disk_used'] = calls.getDiskSpace()[1]
        data['disk_free'] = calls.getDiskSpace()[2]
        data['disk_used_percentage'] = calls.getDiskSpace()[3]
        data['acceleration_x'] = calls.get_accelerometer()[0]
        data['acceleration_y'] = calls.get_accelerometer()[1]
        data['acceleration_z'] = calls.get_accelerometer()[2]
        data['orientation_x'] = calls.get_gyroscope()[0]
        data['orientation_y'] = calls.get_gyroscope()[1]
        data['orientation_z'] = calls.get_gyroscope()[2]
        data['pitch'] = calls.get_orientation_radians()[0]
        data['roll'] = calls.get_orientation_radians()[1]
        data['yaw'] = calls.get_orientation_radians()[2]
        data['pitch'] = calls.get_orientation_degrees()[0]
        data['roll'] = calls.get_orientation_degrees()[1]
        data['yaw'] = calls.get_orientation_degrees()[2]


        #Sending data to Thingsboard
        r = requests.post(thingsboard_url, data=json.dumps(data))

        next_reading += INTERVAL
        sleep_time = next_reading-time.time()
        if sleep_time > 0:
            time.sleep(sleep_time)

except KeyboardInterrupt:
    pass
