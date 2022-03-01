# Python Standard Library Modules
from abc import ABC, abstractmethod
from collections import deque
import multiprocessing as mp

# Third Party Modules
import EasyPySpin # PySpin Module

# Local Modules
from ..sensor import Sensor # Abstract class Sensor
from ..state import State # Glider State

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
    event_delay : int
    image_type : String
    buffer_size : int
    buffer : Deque
    glider_state: Multiprocessing.Value

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
                event_delay: int,
                image_type: str,
                buffer_size: int,
                initial_state: State):
        self.exposure = exposure
        self.gain = gain
        self.brightness = brightness
        self.fps = fps
        self.backlight = backlight
        self.event_delay = event_delay
        self.image_type = image_type
        self.buffer_size = buffer_size
        self.buffer = deque([], self.buffer_size)
        self.glider_state = mp.Value("i", initial_state)
    
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
        with self.glider_state.get_lock():
            self.glider_state.val = next_state
    
    @abstractmethod
    def detect_event(self):
        pass
