import sl4a
import time

# SET LOCAL FOLDER ON PHONE TO SAVE PICTURES
localfolder = '/storage/499D-1DFA/Archive/'

# EDIT DETAILS DIRECTLY IN SCRIPT BEFORE RUNNING
source = "Bob Dobbs"
box = 1
folder = 1
nowtime = time.strftime("%I %M %p on %A, %B %e, %Y")

filename = source + "_box" + str(box) + "_folder" + str(folder) + "_" + nowtime + ".jpg"

# INITIALIZE ANDROID
droid = sl4a.Android()

# TAKE PICTURE IN ANDROID
# FILE NAME WILL HAVE BOX, FOLDER, AND DATETIME
droid.cameraInteractiveCapturePicture(localfolder + source + "/" + "box" + str(box) + "/" + "folder" + str(folder) + "/" + filename)
