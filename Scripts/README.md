## Calls.py ##


Stores all of the functions to retrieve the data for JSON RPC resonses sent by data.py. 

### Host Information: ###


- get_cpu_temperature: Returns the CPU temperature as a string in Celsius.
- get_cpu_use: Returns the percentage of CPU used by the user as a percent value.
- get_ram_info: Returns a list of information about RAM usage.
- get_disk_space: Returns a list of information about disk space usage.

### SenseHat Information: ###

- get_ambient_temperature: Returns the temperature readings of the environment.
- get_pressure: Returns the atmospheric pressure readings.
- get_humidity: Returns the humidity readings of the environment.
- get_gyro_data: Returns the angular velocity readings in the x, y, and z directions.
- get_accelerometer_data: Returns the acceleration readings in the x, y, and z directions.
- get_orientation_degrees: Returns the orientation readings in degrees for pitch, roll, and yaw.

## Data.py ##


Retrieves the values from a defined list of functions, the main modules used are SeneHat and os.

## Targets.py ##


Stores the API Url's and Keys to be used by Data.py when sending JSON RPC Responses to the intended target destination.
