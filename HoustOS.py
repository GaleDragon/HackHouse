class HouseController:
	# contains threads for RoomListener objects, I cannot currently into threading
	# maybe each thread should run on a single pi unit, and then check for commands on the server?
	pass

class RoomListener(object):
	#startup sequence
	def __init__(self):
		self.quiet = False
		# temp gets handed off to an arduino for actual adjustments. 
		# I currently think that we should keep all computation on the Pis
		self.temperature = 70
		self.shades = "closed"
		self.door = "closed"
		# door locks should be simple slide bolts that can be opened from the inside in case of emergency
		self.doorLock = "open"
		self.listen()
		
	#basically, how does the object listen for voice commands and move between quiet and loud modes?
	def listen(self):
		# Jeremy: Essentially, with reactive behaviors, everything is in a while loop
		# that keeps checking and checking and checking
		pass
			

	#Example of simple call to room unit
	def arduino_call(self, command):
		pass
  
	def shades(self, state):
		pass
		
		
		
if __name__=='__main__':
	R = RoomLstener()
	del R
						
		