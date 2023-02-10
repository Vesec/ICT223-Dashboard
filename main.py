import json
import requests
import time
import os

# Import based on using a physical RPi or the emulator
#from sense_emu import SenseHat
from sense_hat import SenseHat

# Constants
INTERVAL            = 3  #Data capture and upload interval in seconds.
API_KEY             = "s47B3i4t0oNlwFl67D5u"  #Thingsboard Token
THINGSBOARD_HOST    = "10.0.0.95:8080"  #Thingsboard server address and port.

thingsboard_url     = "http://{0}/api/v1/{1}/telemetry".format(THINGSBOARD_HOST, API_KEY)

sense = SenseHat()
data = {}
next_reading = time.time()

try:
    while True:
        data = {}
        data['temperature'] = sense.get_temperature()
        data['pressure'] = sense.get_pressure()
        data['humidity'] = sense.get_humidity()
        data['cpu_temp'] = data.getCPUtemperature()
        data['cpu_use'] = data.getCPUuse()
        data['ram_total'], data['ram_used'], data['ram_free'] = data.getRAMinfo()
        data['disk_total'], data['disk_used'], data['disk_free'], data['disk_used_percentage'] = data.getDiskSpace()

        #Sending data to Thingsboard
        r = requests.post(thingsboard_url, data=json.dumps(data))

        next_reading += INTERVAL
        sleep_time = next_reading-time.time()
        if sleep_time > 0:
            time.sleep(sleep_time)
except KeyboardInterrupt:
    pass
