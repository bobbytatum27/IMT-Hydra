**Todo - logging events, logging data collected, logging data i/o, edit function and variable names**

# Abstract Class Cam inherits from Sensor, ABC

### Member Fields

- camera: EasyPySpin.VideoCapture
- exposure: int
- gain: int
- brightness: int
- gamma: float
- fps: int
- backlight: int
- current_state: Enum {Quiescent, Storm, Event}
- event_delay: int
- image_type: String
- buffer_size: int
- buffer: Deque

### Methods inherited from Sensor

- power_on()
  - creates a camera reference and stores it in the appropriate member variable
- power_off()
  - a call to the camera reference's release() method; see cSBC.py
- write_data(file_handler?)
  - abstract method (see Python's ABC)
- collect_data()
  - abstract method (see Python's ABC)

### Member Methods

- set_state(next_state: Enum {Quiescent, Storm, Event})
  - changes the state of the cam to the passed parameter
- detect_event()
  - abstract method

# class BubbleCam inherits from Cam

### Member Fields inherited from Cam

- camera: EasyPySpin.VideoCapture
- exposure: int
- gain: int
- brightness: int
- gamma: float
- fps: int
- backlight: int
- current_state: Enum {Quiescent, Storm, Event}
- event_delay: int
- image_type: String
- buffer_size: int
- buffer: Deque

### Methods inherited from Sensor (via Cam)

- power_on()
  - creates a camera reference and stores it in the appropriate member variable
- power_off()
  - a call to the camera reference's release() method; see cSBC.py
- write_data(file_handler?)
  - write the data in the buffer to file
- collect_data()
  - continuously log data in a double-ended queue.

### Member Methods inherited from Cam

- set_state(next_state: Enum {Quiescent, Storm, Event})
  - changes the state of the cam to the passed parameter
- detect_event()
  - implemented version of the abstract method
  - triggers the Bubble Cam event response -> collects data and logs event time
