# Python Standard Library Modules
from abc import ABC, abstractmethod
from collections import deque

# Third Party Modules
import EasyPySpin # PySpin Module

# Local Modules
from .sensor import Sensor # Abstract class Sensor
from .state import State # Enums: {Quiescent, Storm, Event}

# TODO(pkam): Add method headers
class Cam(Sensor, ABC):
    """
    Abstract class for Cam which inherits methods from Sensor
    
    Attributes
    ----------
    
    camera : EasyPySpin.VideoCapture
    exposure : int
    gain : int
    brightness : int
    gamma : float
    fps : int
    backlight : int
    current_state : Enum {Quiescent, Storm, Event}
    event_delay : int
    image_type : String
    buffer_size : int
    buffer : Deque

    Methods
    -------
    
    power_on()
        creates a camera reference and stores it in the appropriate member variable
    power_off()
        a call to the camera reference's release() method; see cSBC.py
    write_data(file_handler?)
        abstract method (see Python's ABC)
    collect_data()
        abstract method (see Python's ABC)
    set_state(next_state: Enum {Quiescent, Storm, Event})
        changes the state of the cam to the passed parameter
    detect_event()
        abstract method

    """

    # Initialize Member Variables
    def __init__(self, 
                exposure: int, 
                gain: int, 
                brightness: int, 
                fps: int, 
                backlight: int, 
                current_state: State,
                event_delay: int,
                image_type: str,
                buffer_size: int):
        self.exposure = exposure
        self.gain = gain
        self.brightness = brightness
        self.fps = fps
        self.backlight = backlight
        self.current_state = current_state
        self.event_delay = event_delay
        self.image_type = image_type
        self.buffer_size = buffer_size
        self.buffer = deque([], self.buffer_size)
    
    # Methods inherited from Sensor

    def power_on(self):
        """
        Creates a camera reference and stores it in the appropriate member variable
        """
        self.camera = EasyPySpin.VideoCapture(0)

    def power_off(self):
        """
        A call to the camera reference's release() method
        """
        self.camera.release()
    
    @abstractmethod
    def write_data(self):
        pass

    @abstractmethod
    def collect_data(self):
        pass

    # Cam Member methods

    def set_state(self, next_state: State):
        """
        Changes the state of the cam to the passed parameter
        """
        self.current_state = next_state
    
    @abstractmethod
    def detect_event(self):
        pass
