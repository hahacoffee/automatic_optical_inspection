
d=dataObject
cam=dataIO("openCVGrabber",0)
cam.startDevice()
cam.disableAutoGrabbing()
print("1CS=",cam.getAutoGrabbing())
cam.acquire()
cam.getVal(d)
cam.stopDevice()
print("2CS=",cam.getAutoGrabbing())
plot(d)