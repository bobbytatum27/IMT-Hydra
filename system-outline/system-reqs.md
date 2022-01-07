The system requirements:
1. Sensors log data when they're supposed to.
2. Hardware that doesn't need to be on, isn't on.
3. SBCs communicate the ocean state with each other.


# Main Modules
1. Sensor
2. Comms
3. Power
4. Logging

There are 4 main modules as part of the IMT Hydra system. 

First is the sensor module, which governs the sensor systems as part of the Hydra system. Included within the sensor module
are submodules which group the various types of sensors and data-logging requirements.

Second is the Comms module. It is responsible for ensuring consistent and appropriate communication between each
single board computer (SBC).

Third is the Power module. It is responsible for assessing the electrical power needs of the Hydra hardware, and toggling the power
such that power draw is minimized but all necessary hardware systems are operating.

Fourth is the Logging module. It is responsible for formatting log files and logging important information dictated by each other module. Notably, the main modules (Sensor, Comms, Power) should all implement the Logging interface.

Below is a tree diagram containing the main modules and their submodules.

** PUT DIAGRAM HERE **

# Sensor Module
##### Description
The sensor module is responsible for governing the sensor systems onboard the Hydra. This means it handles SBC to Sensor communication, sensor power, sensor data collection, and sensor data logging. In otherwords, the Sensor module is the primary interface between an SBC and any given sensor.

##### Module Hierarchy
- Sensor Module

##### Direct Submodules
- Camera
- Conditional Loggers
- Contant Loggers

##### Methods
- power_on()
- power_off()
- log_data(logger: Logger)
- capture_data()

### Camera: Sensor Submodule
##### Description:
The Camera module is responsible for governing the FLIR cameras onboard the Hydra. There are a total of 3 cameras: the Bubble Cam, the Foam Cam, and the White Cap Cam. While each camera has different requirements and specifications, all 3 cameras share some common attributes. The Camera submodule is responsible for providing a common interface for these common attributes, namely the following: camera settings, camera data capture rate, and camera event logging. Further specifications on each camera sensor can be found in the Bubble Cam, Foam Cam, and White Cap Cam submodules.

##### Module Hierarchy:
- Sensor > Camera

##### Direct Submodules
- Bubble Cam
- Foam Cam
- White Cap Cam

##### Methods
- TBD

### Bubble Cam: Camera Submodule
##### Description
The Bubble Cam is the primary camera for the Hydra system. It is physically located on the underside of the Wave Glider so that it can capture images of crashing waves. It remains inactive during the **Quiescent State**, but activates during the **Storm State**, remaining on (and logging data) for the **Event State**. Importantly, when activated, the Bubble Cam module will continuously log frames in a rolling buffer, overwriting the oldest images when the buffer fills. However, when an event occurs, the Bubble Cam module will log the buffer of images.

##### Active States
- Storm State
- Event State

##### Logging Frequency
- Once per event

##### Module Hierarchy
- Sensor > Camera > Bubble Cam

##### Direct Submodules
- None

##### Methods
- TBD

### Foam Cam: Camera Submodule
##### Description
The Foam Cam is an additional camera for the Hydra system, physically located on the mast of the Wave Glider. It functions similarly to the Bubble Cam module in that it is inactive during the **Quiescent State** but active during the **Storm State** and **Event State**. Additionally, it also parallels Bubble's Cam data logging model; like Bubble Cam, Foam Cam continously logs data in a rolling buffer (overwriting the oldest image when the buffer fills), and logging the buffer of images when an event occurs.

##### Active States
- Storm State
- Event State

##### Logging Frequency
- Once per event

##### Module Hierarchy
- Sensor > Camera > Foam Cam

##### Direct Submodules
- None

##### Methods
- TBD

### White Cap Cam: Camera Submodule
##### Description
The White Cap Cam is an additional camera for the Hydra system, physically located on the mast of the Wave Glider (like Foam Cam). Its purpose is to capture images of whitecaps during ocean storms. As such, it is only active during **Storm State** and **Event State**, and inactive during **Quiescent State**. Notably, White Cap cam logs an image once every 15 minutes during either **Storm State** or **Event State**.

##### Active States
- Storm State
- Event State

##### Logging Frequency
- 1 picture / 15 min.

##### Module Hierarchy
- Sensor > Camera > White Cap Cam

##### Direct Submodules
- None

##### Methods
- TBD


******************************************

# Comms Module
##### Description
The Comms Module is repsonsible for all inter-process communications among the Hydra systems. In other words, it ensures hardware systems can communicate with each other and themselves.

##### Module Hierarchy
- Comms Module

##### Direct Submodules
- SBC Communicator

##### Methods
- TBD

### SBC Communicator: Comms Submodule
##### Description
The SBC Communicator handles communications between all SBCs on the Hydra. Specifically, it functions primarily to distribute information between the Supervisor SBC and Camera SBCs (Latte Pandas) since the sensors some sensors and data logging functionality controlled by these systems are toggled on/off during **Quiescent States**, **Storm States**, and **Event States**. Importantly, the SBC Communicator follows a Publisher/Subscriber model, wherein the Supervisor SBC serves as the main publisher, and other SBCs are the subscribers. This allows the Supervisor to communicate when a state change occurs and distribute that message simulataneously to many different listeners.

##### Communication Format
- Publish / Subscribe

##### Communication Frequency
- Hydra System State Change (i.e. Quiescent <-> Storm <-> Event)

##### Logging Frequency
- Message propagation

##### Module Hierarchy
- Comms > SBC Communicator

##### Direct Submodules
- None

##### Methods
- TBD

# Power Module
##### Description
The Power Module is responsible for toggling power supplies for various Hydra systems. Currently, the most critical power supply is the Power Distribution Board (which is controlled via the PDB Controller Submodule), but more power supplies/power toggle requirements might be added in the future.

##### Module Hierarchy
- Power Module

##### Direct Submodules
- PDB Controller

##### Methods
- TBD

### PDB Controller: Power Submodule
##### Description
The PDB Controller controls the power distribution board (PDB) on the Hydra. The power distribution board serves as the main power interface for the various hardware systems the IMT Lab has added to the Wave Glider. Therefore, the PDB controller is responsible for toggling power output, depending on the Hydra's state. Notably, it will most frequently toggle the Sensor::Camera Submodule, as the entire Sensor::Camera Submodule does not need power in a **Quiescent State** but does need continuous power in a **Storm State** and **Event State**.

##### Power Toggle Requirements (by Glider State)
- Quiescent State: **Camera Module** powered off
- Storm State: all systems powered on
- Event State: all systems on

##### Logging Frequency
- Once per daughter card interaction

##### Module Hierarchy
- Power > PDB Controller

##### Direct Submodules
- None

##### Methods
- TBD


# Some Ideas to Improve this Doc
- transmit data comms module
- add important method headers
- make a state transition diagram