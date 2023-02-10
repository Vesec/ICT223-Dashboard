import json
import requests
import time
import calls
import psutil
from gpiozero import CPUTemperature
from sense_hat import SenseHat

sense = SenseHat()

# Constants
INTERVAL            = 1  #Data capture and upload interval in seconds.
API_KEY             = "s47B3i4t0oNlwFl67D5u"  #Thingsboard Token
THINGSBOARD_HOST    = "pctips.ca"  #Thingsboard server address and port.

thingsboard_url     = "https://{0}/api/v1/{1}/telemetry".format(THINGSBOARD_HOST, API_KEY)


data = {}
next_reading = time.time()

try:
    while True:
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


        #Sending data to Thingsboard
        r = requests.post(thingsboard_url, data=json.dumps(data))

        next_reading += INTERVAL
        sleep_time = next_reading-time.time()
        if sleep_time > 0:
            time.sleep(sleep_time)


except KeyboardInterrupt:
    pass
