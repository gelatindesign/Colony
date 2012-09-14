# -------- App.py --------
# Handles all general application logic
# ------------------------

# Standard imports
from math import pi, sin, cos

# Panda3d imports
from direct.showbase.ShowBase import ShowBase
from direct.task import Task

# App imports


# -------- App --------
class App( ShowBase ):

	# Init
	# 
	# @param object Self
	# @return void
	def __init__( self ):
		ShowBase.__init__( self )

		# Load the environment model
		self.environ = self.loader.loadModel( "environment" )

		# Re-parent the model to render
		self.environ.reparentTo( self.render )

		# Apply scale and position transforms on the model
		self.environ.setScale( 0.25, 0.25, 0.25 )
		self.environ.setPos( -8, 42, 0 )