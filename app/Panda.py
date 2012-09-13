# -------- Panda.py --------
# Handles being a panda
# ------------------------

# Panda3d imports
from direct.actor.Actor import Actor

# -------- Panda --------
class Panda( Actor ):
	src = "resources/models/panda-model"
	states = {
		"walk": "resources/models/panda-walk4"
	}
	scale = 0.005, 0.005, 0.005

	# Init
	#
	# @param self
	# @return void
	def __init__( self, app ):
		# Create actor
		Actor.__init__( self, self.src, self.states )
		self.setScale( self.scale )
		self.reparentTo( app.render )

		# Loop animation
		self.loop( "walk" )