# ------------------------ Colony ------------------------
# @author Gelatin Design, Laurence Roberts
# @datestart 12th September 2012
# 
# @version Pre-Alpha 0.0
# --------------------------------------------------------


# ------------------------ Imports ------------------------

# Panda3d imports
from panda3d.core import loadPrcFile

# Load config
import colony.Config

# Import app logic
from colony.App import App
from colony.Camera import CameraHandler
from colony.Panda import Panda



# ------------------------ Panda3D Config ------------------------

loadPrcFile("./config/config.prc")



# ------------------------ Main ------------------------

# Create app instance
app = App( )

# Add the panda
p = Panda( )

# Create the camera
camera = CameraHandler( )

# Set background colour
base.setBackgroundColor( 1, 0.3, 0 )

# Set the app to run
app.run( )