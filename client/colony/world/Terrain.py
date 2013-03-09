# -------- Terrain.py --------
# Generates and transfers terrain
# ----------------------------

# Panda3d imports
from pandac.PandaModules import GeoMipTerrain

# -------- Terrain --------
class Terrain( ):

	# Init
	#
	# @param object Self
	# @return void
	def __init__( self ):
		self.LoadTestTerrain( )
	

	# Load test terrain
	def LoadTestTerrain( self ):

		# Create new terrain object
		test = GeoMipTerrain( "test" )

		# Set the heightfield
		test.setHeightField( "data/maps/test01.png" )

		# Reparent to render
		test.getRoot( ).reparentTo( render )

		# Generate terrain
		test.generate( )