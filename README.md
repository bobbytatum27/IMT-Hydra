# IMT-Hydra
Repository for the Scripps Institute of Oceanography IMT Lab's Hydra project. 

**WIP - Repo structure is not finalized**

Repository Structure:
- setup-scripts
- sensor-modules
- environment-validation
- to-dos

# ROADMAP
- [X] Adapt Imran's Test Suite to utilize OOP-BubbleCam Implementation
- [ ] Use Bubble Cam Implementation to Capture/Save Images
  - [ ] Determine byte threshold for "interesting" Bubble Cam images
  - [ ] Determine i/o speed for a completely full buffer
- [ ] Revise Bubble Cam Implementation Method Names/Inheritance Hierarchy
  - [ ] Determine list of all sensors that we can actually power on/off
- [ ] Implement Foam Cam
- [ ] Implement Whitecap Cam
  - [ ] Change event trigger to a timer
- [ ] Determine byte threshold for "interesting" images on Foam/Whitecap Cam
- [X] Create Class Hierarchy Diagram
- [X] Create State Transition Flowchart
- [X] Create Flowchart for sensors and add pseudocode
- [ ] Implement Sensor Module/Submodules
- [ ] Implement Comms Module
- [ ] Implement Power Module
  - Note: Include bidrectional comms support
- [ ] Implement Logging Module

# Spring Quarter
## Week 2
Questions for meeting
* What times work best for undergrad meeting?
* Can we just use the GPS to set system time of the SBCs? Do we need 1pps and if so how would we use it?
* What logging convention should we use (for cams, for SITA/MET1)?

- [ ] GPS sync time with RPi and Latte Pandas
- [ ] Reimplement bubblecam using composition (vs inheritance)
- [ ] Napkin math for SITA and MET1 storage capacity

## Week 3
- [ ] Test reimplementation of bubblecam (current functionality + data quality check)
- [ ] Implement logger module (concurrent to bubblecam)
- [ ] Test logger module
- [ ] Reimplement foam and white cap cam
- [ ] Test reimplementation of foam and white cap cam

## Week 4
- [ ] Get MET1 feather working with the supervisor
- [ ] Implement pub/sub for state between RPi (supervisor) and cams (Latte Pandas)
