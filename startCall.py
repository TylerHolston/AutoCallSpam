# startCall.py
# this will open the faceTime.app
# will throw an exception if the location is incorrect
# if location is incorrect find your full path to FaceTime.app
# and replace the constant var FACETIME_LOCATION

import subprocess

#==============================================================================
# DO NOT TOUCH ABOVE THIS LINE
#==============================================================================

FACETIME_LOCATION = "/System/Applications/FaceTime.app"

#==============================================================================
# DO NOT TOUCH BELOW THIS LINE
#==============================================================================

FACETIME_ERROR = "Error Targeting FaceTime.app at location: %s"%FACETIME_LOCATION

# openFacetime("string param")
# opens subprocess facetime with outgoing call
# directed at telephone param
# Throws
#      Exception - Error Targeting FaceTime.app
def openFacetime(telephone):
    try:
        subprocess.call(["/usr/bin/open", "-W", "-n", "-a", FACETIME_LOCATION,
                 "tel://{}".format(telephone)])
    except Exception as e:
        print(e)
        print(FACETIME_ERROR)