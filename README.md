# ICT223 - Thingsboard Dashboard

![image](https://user-images.githubusercontent.com/95189970/218229756-f085c006-9477-4089-af92-e772d5f304de.png)

# About #

- This Repository is a Work in Progress for a College Course and as such Subject to intermittent breaks in the code or sudden major changes in structure.

- The repository contains the JSON files for each Widget, Rule Set, Profile and the necessary Python files to send and display data about the system to the Thingsboard dashboard.

- This Dashboard is inteded to display statistics about the Raspberry Pi's environment as well as the System Resources.

## Notes ##

  - A Device Profile Must be added to generate the token needed for responses to be sent to thingsboard.

  - The Device name used with the dashboard is ***RPi 4B*** 
 
  - The Rules, Profiles and Widgets have been exported as Importable JSON files.

  - The ***Targets.py*** file needs to be modified to reflect the api url and token of the offsite dashboard in Thingsboard and is seperated to accomodate for multiple API's.

  - Some functions in ***Calls.py*** require a Raspberry Pi with a SenseHat installed.
  
# Files
```
.
├── LICENSE
├── Modules
│   ├── ambient_temp.json
│   ├── cpu_statistics.json
│   ├── cpu_vs_ambient_temperature.json
│   ├── device_orientation.json
│   ├── disk_usage.json
│   └── humidity.json
├── Profiles
│   └── default.json
├── README.md
├── Rules
│   └── root_rule_chain.json
└── Scripts
    ├── calls.py
    ├── data.py
    ├── README.md
    └── targets.py

5 directories, 13 files

```

