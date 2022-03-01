**Todo - logging events, logging data collected, logging data i/o**

# class SITA inherits from Sensor

### Member Fields

- ser: Serial
- measureTimeLimit: int
- measureInterval: int
- baud_rate: int
- port: String
- timer: Timer

### Member methods inherited from Sensor

- power_on()
  - turns on the SITA by making a serial connection
- power_off()
  - turn off the SITA by closing serial connection
- write_data(file_handler?)
  - write sensor data to file
- collect_data()
  - collect data and call write_data()

### Other member Methods

- start_collection_workflow()
  - helper method to call collect_data() every 30 minutes
