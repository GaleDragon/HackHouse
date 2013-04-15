class HouseController:
	# contains threads for RoomListener objects, I cannot currently into threading
	# maybe each thread should run on a single pi unit, and then check for commands on the server?
	pass

class RoomListener:
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
		if self.quiet == True
			listen_for_loud()
		if self.quiet == False:
			get_command():
			

	#Example of simple call to room unit
	def arduino_call(self, command):
		pass
  
	def shades(self, state):
		if state == "open":
			self.call_to_arduino()
		elif state == "close":
			self.call_to_arduino() 
						
		