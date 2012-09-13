# -------- App.py --------
# Handles all general application logic
# ------------------------

# Standard imports
from math import pi, sin, cos

# Panda3d imports
from direct.showbase.ShowBase import ShowBase
from direct.task import Task

# App imports
from Panda import Panda

# -------- App --------
class App( ShowBase ):

	# Init
	# 
	# @param object Self
	# @return void
	def __init__( self ):
		ShowBase.__init__( self )

		# Load the environment model
		self.environ = self.loader.loadModel( "resources/models/environment" )

		# Re-parent the model to render
		self.environ.reparentTo( self.render )

		# Apply scale and position transforms on the model
		self.environ.setScale( 0.25, 0.25, 0.25 )
		self.environ.setPos( -8, 42, 0 )

		# Add the spinCameraTask to the task manager
		self.taskMgr.add( self.spinCameraTask, "SpinCameraTask" )

		# Add the panda
		p = Panda( self )
		p.loop( "walk" )

	# Spin the camera. A procedure, or 'task', to move the camera
	#
	# @param object Self
	# @param string Task name
	# @return task constant
	def spinCameraTask( self, task ):
		angleDegrees = task.time * 6.0
		angleRadians = angleDegrees * ( pi / 180.0 )

		# Set camera position
		self.camera.setPos( 20 * sin(angleRadians), -20 * cos(angleRadians), 3 + (4 * sin(angleRadians)) )

		# Set camera heading, pitch, roll
		self.camera.setHpr( angleDegrees, 0, 20 * sin(angleRadians) )

		return Task.cont