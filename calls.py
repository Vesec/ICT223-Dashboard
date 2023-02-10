import os
from sense_hat import SenseHat


def get_cpu_temperature():
    #Return the CPU temperature as a string in Celsius.
    with os.popen("vcgencmd measure_temp") as res:
        return res.readline().replace("temp=", "").replace("'C\n", "")

def get_ram_info():
    #Return a list of information about RAM usage.
    with os.popen("free") as p:
        p.readline()
        return list(map(int, p.readline().split()[1:4]))

def get_cpu_use():
    #Return the percentage of CPU used by the user as a string.
    with os.popen("top -n1 | awk '/Cpu\(s\):/ {print $2}'") as res:
        return res.readline().strip()

def get_disk_space():
    #Return a list of information about disk space usage.
    with os.popen("df -h /") as p:
        p.readline()
        return p.readline().split()[1:5]

def get_ambient_temperature():
    #Returns the temperature readings of the environment.
    temperature = sense.get_temperature()
    return temperature
    
def get_pressure():
    #Returns the atmospheric pressure readings.
    pressure = sense.get_pressure()
    return pressure

def get_humidity():
    #Returns the humidity readings of the environment.
    humidity = sense.get_humidity()
    return humidity

def get_gyro_data():
    #Returns the angular velocity readings in the x, y, and z directions.
    gyro_data = sense.get_gyroscope()
    return gyro_data['x'], gyro_data['y'], gyro_data['z']

def get_accelerometer_data():
    #Returns the acceleration readings in the x, y, and z directions.
    accelerometer_data = sense.get_accelerometer()
    return accelerometer_data['x'], accelerometer_data['y'], accelerometer_data['z']

def get_orientation_radians():
    #Returns the orientation readings in radians for pitch, roll, and yaw.
    orientation_radians = sense.get_orientation_radians()
    return orientation_radians['pitch'], orientation_radians['roll'], orientation_radians['yaw']

def get_orientation_degrees():
    #Returns the orientation readings in degrees for pitch, roll, and yaw.
    orientation_degrees = sense.get_orientation_degrees()
    return orientation_degrees['pitch'], orientation_degrees['roll'], orientation_degrees['yaw']

def get_cpu_temperature():
    #Return the CPU temperature as a string in Celsius.
    with os.popen("vcgencmd measure_temp") as res:
        return res.readline().replace("temp=", "").replace("'C\n", "")

def get_ram_info():
    #Return a list of information about RAM usage
    with os.popen("free") as p:
        p.readline()
        return list(map(int, p.readline().split()[1:4]))

def get_cpu_use():
    #Return the percentage of CPU used by the user as a string
    with os.popen("top -n1 | awk '/Cpu\(s\):/ {print $2}'") as res:
        return res.readline().strip()

def get_disk_space():
    #Return a list of information about disk space usage.
    with os.popen("df -h /") as p:
        p.readline()
        return p.readline().split()[1:5]
