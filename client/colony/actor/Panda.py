# -------- Panda.py --------
# Handles being a panda
# --------------------------

# Panda3d imports
from direct.actor.Actor import Actor
from direct.interval.IntervalGlobal import Sequence
from panda3d.core import Point3

# App imports
import Config

# -------- Panda --------
class Panda( ):
	src = "panda-model"
	states = {
		"walk": "panda-walk4"
	}
	scale = 0.005, 0.005, 0.005

	# Init
	#
	# @param self
	# @return void
	def __init__( self ):
		# Create actor
		self.actor = Actor( self.src, self.states )
		self.actor.setScale( 0.005, 0.005, 0.005 )
		self.actor.reparentTo( render )

		# Loop animation
		self.actor.loop( "walk" )

		# Set the panda to roam
		self.roam( )

	# Roam
	#
	# @param self
	# @return void
	def roam( self ):
		# Create the four lerp intervals to walk back and forth
		posInterval1 = self.actor.posInterval(
			13,
			Point3( 0, -10, 0 ),
			startPos = Point3( 0, 10, 0 )
		)

		posInterval2 = self.actor.posInterval(
			13,
			Point3( 0, 10, 0 ),
			startPos = Point3( 0, -10, 0 )
		)

		hprInterval1 = self.actor.hprInterval(
			3,
			Point3( 180, 0, 0 ),
			startHpr = Point3( 0, 0, 0 )
		)

		hprInterval2 = self.actor.hprInterval(
			3,
			Point3( 0, 0, 0 ),
			startHpr = Point3( 180, 0, 0 )
		)

		self.roamSequence = Sequence(
			posInterval1,
			hprInterval1,
			posInterval2,
			hprInterval2,
			name = "roam"
		)

		self.roamSequence.loop( )