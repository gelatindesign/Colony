# ------------------------ Colony ------------------------
# @author Gelatin Design, Laurence Roberts
# @datestart 12th September 2012
# 
# @version Pre-Alpha 0.0.0
# --------------------------------------------------------


# ------------------------ Imports ------------------------

# Load config
import colony.Config

# Logging
import logging
import logging.config
logging.config.fileConfig( 'config/logging.conf' )
logger = logging.getLogger( 'root' )

# Panda3d imports
from panda3d.core import loadPrcFile

# Import app logic
from colony.App import App
from colony.Camera import CameraHandler
from colony.world.Terrain import Terrain


# ------------------------ Panda3D Config ------------------------

loadPrcFile("./config/config.prc")


# ------------------------ Main ------------------------

# Create app instance
app = App( )

t = Terrain( )

# Create the camera
camera = CameraHandler( )

# Set background colour
base.setBackgroundColor( 0, 0, 0 )

# Set the app to run
app.run( )