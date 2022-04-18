# IMT-Hydra

Repository for the Scripps Institute of Oceanography IMT Lab's Hydra project.

**WIP - Repo structure is not finalized**

Repository Structure:

- setup-scripts
- sensor-modules
- environment-validation
- to-dos

# ROADMAP

- [x] Adapt Imran's Test Suite to utilize OOP-BubbleCam Implementation
- [ ] Use Bubble Cam Implementation to Capture/Save Images
  - [ ] Determine byte threshold for "interesting" Bubble Cam images
  - [ ] Determine i/o speed for a completely full buffer
- [ ] Revise Bubble Cam Implementation Method Names/Inheritance Hierarchy
  - [ ] Determine list of all sensors that we can actually power on/off
  - [ ] Change event trigger to a timer
- [ ] Determine byte threshold for "interesting" images on Foam/Whitecap Cam
- [x] Create Class Hierarchy Diagram
- [x] Create State Transition Flowchart
- [x] Create Flowchart for sensors and add pseudocode
- [ ] Implement Sensor Module/Submodules
- [ ] Implement Comms Module
- [ ] Implement Power Module
  - Note: Include bidrectional comms support
- [ ] Implement Logging Module

# Spring Quarter

## Week 2

Questions for meeting

- What times work best for undergrad meeting? _TBD_
- Can we just use the GPS to set system time of the SBCs? _Do we need 1pps and if so how would we use it? Log 1pps pulse with measurement logs and sync them up later. Find out how to connect GPS with Latte Pandas._
- What logging convention should we use (for cams, for SITA/MET1)? _Low data rate. Human readable. Serves as activity log for cameras._
- Recruiting: _Job posting. Share with student-orgs: ACM, Triton Robotics (tritonrobotics@ucsd.edu)._

- [x] GPS time logging for RPi
- [X] Implement cam Module (composition)

## Week 3

- [X] Implement logger module (concurrent to bubblecam)
- [X] Implement bubblecam module (compisition)

## Week 4

Questions for meeting
- What lockout time are we expecting? (currently averaging 3.3 seconds for 150-image write -- slow at the start)
- For the buffer, is there a rate of capture that we want, or do we want every single frame (according to the cam fps)?
- What size buffer do we want? (seconds into frames)
- What format do we want to write data in? (currently png -- compressed)

- [ ] Test logger module
- [ ] Test reimplementation of bubblecam (current functionality + data quality check)
- [ ] Reimplement foam and white cap cam
- [ ] Test reimplementation of foam and white cap cam

## Week 5

- [ ] GPS time logging for Latte Pandas
- [ ] Napkin math for SITA and MET1 storage capacity (needs logging sample)
- [ ] Get MET1 feather working with the supervisor
- [ ] Implement pub/sub for state between RPi (supervisor) and cams (Latte Pandas)
- [ ] Test SITA and MET1

## Week 6 onwards

- [ ] Implement Power Module
