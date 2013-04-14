class HouseController:
#contains threads for RoomListener objects, I cannot currently into threading
#maybe each thread should run on a single pi unit, and then check for commands on the server?
	pass

class RoomListener:

#basically, how does the object listen for voice commands and move between quiet and loud modes?
	def self.listen():
		if self.quiet == True
			listen_for_loud()
		if self.quiet == False:
			get_command():
			

#Example of simple call to room unit
	def self.arduino_call():
		call_correct_function(get_voice_command())
  
	def self.shades(state):
		if state == "open":
			call_to_arduino()
		elif state == "close":
			call_to_arduino()
		
#startup sequence
	def __init__():
		self.quiet = False 
						
		#temp gets handed off to an arduino for actual adjustments. I currently think that we should keep all computation on the Pis
		self.Temperature = 70
		
		self.shades = "closed"
		
		self.door = "closed"
		
		#door locks should be simple slide bolts that can be opened from the inside in case of emergency
		self.doorLock = "open"
		
		self.listen()