# -------- Actor.py --------
# Generic actor parent class
# --------------------------

# General imports
import logging
logger = logging.getLogger( __name__ )

# Panda3d imports
import direct.actor.Actor
from direct.interval.IntervalGlobal import Sequence
from panda3d.core import Point3

# Colony imports
import colony.Config

# -------- Actor --------
class Actor( direct.actor.Actor ):
	uid = None
	src = None
	states = None

	# Init
	#
	# @param self
	# @return void
	def __init__( self, uid ):
		self.uid = uid

		if self.src == None:
			logger.error( "No src given on actor {0}".format(self.uid) )

		if self.states == None:
			logger.error( "No states given on actor {0}".format(self.uid) )

		# Create actor
		self.actor = Actor( self.src, self.states )
		self.actor.setScale( 0.005, 0.005, 0.005 )
		self.actor.reparentTo( render )
	
	# Move
	#
	# @param self
	# @param int direction
	# @param int distance
	# @return void
	def move( self, direction, distance ):
		pos_interval = self.