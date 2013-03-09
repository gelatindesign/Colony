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
		test.setHeightfield( "data/maps/test01.png" )

		test.setBlockSize( 32 )
		test.setNear( 40 )
		test.setFar( 100 )
		test.setFocalPoint( base.camera )

		# Reparent to render
		test.getRoot( ).reparentTo( render )
		test.setSz( 100 )

		# Generate terrain
		test.generate( )