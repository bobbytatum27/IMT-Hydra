## Endpoints

- imtlab@hydratopsidecam.ucsd.edu (Latte Panda) - topside is foam/whitecap cam
- grant@hydrabubblecam.ucsd.edu (Latte Panda)
- pi@hydrapowercontrol.ucsd.edu (RPi) - for toggling power to SBCs remotely (I don't really use this one anymore)
- pi@hydrasupervisor.ucsd.edu (RPi)

## Sample ssh for bubblecam

```
ssh -L 59000:localhost:5901 -C -N -l grant hydrabubblecam.ucsd.edu
```
