# -------- App.py --------
# Handles all general application logic
# ------------------------

# Panda3d imports
from direct.showbase.ShowBase import ShowBase

# App imports
from actor.GenericActor import GenericActor

# -------- App --------
class App( ShowBase ):

	# Init
	# 
	# @param object Self
	# @return void
	def __init__( self ):
		ShowBase.__init__( self )