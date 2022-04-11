Every SBC Has 2 Responsibilities
- Handle Comms
- Handle Sensors

Comms
- Pub/Sub Model
- Publisher = Supervisor
    - Glider State Changes + Event Triggers
- Subscribers = Every other SBC
    - appropriate event handlers for state changes + event triggers

Sensors
-individual sensors run on corresponding SBCs as either their own process OR on its own thread embedded in a Sensor process
