Make sure you're connected to UCSD wifi. You can use Cisco AnyConnect.

## Endpoints

- imtlab@hydratopsidecam.ucsd.edu (Latte Panda) - topside is foam/whitecap cam
- grant@hydrabubblecam.ucsd.edu (Latte Panda)
- pi@hydrapowercontrol.ucsd.edu (RPi) - for toggling power to SBCs remotely (I don't really use this one anymore)
- pi@hydrasupervisor.ucsd.edu (RPi)

## Sample ssh for bubblecam

```
ssh -L 59000:localhost:5901 -C -N -l grant hydrabubblecam.ucsd.edu
```

Steps
- ssh into one a Latte Panda or Raspi
- Start vnc server in the SBC using ```vncserver -localhost```
- In another terminal, use the ssh pattern described above
- Connect to localhost:5901 using a remote desktop ("screen sharing" for mac)