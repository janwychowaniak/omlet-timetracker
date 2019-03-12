#!/usr/bin/python



from datetime import datetime



STATE_STOPPED = 0
STATE_STARTED = 1


class Mintimer:

	def __init__(self):
		self.state = STATE_STOPPED
		
		
	def start(self):
		if self.state != STATE_STOPPED:
			raise Exception('Timer not stopped')
		self.state = STATE_STARTED
		self.start_moment = datetime.now()

	def stop(self):
		if self.state != STATE_STARTED:
			raise Exception('Timer not started')
		self.stop_moment = datetime.now()
		self.state = STATE_STOPPED

	def get_mins(self):
		if self.state != STATE_STOPPED:
			raise Exception('Timer not stopped')
		difference = self.stop_moment - self.start_moment
		print difference
		return str(difference.seconds/60)




if __name__ == '__main__':
	import time
	timer1 = Mintimer()
	timer1.start()
	time.sleep(60)
	#~ raw_input("Press Enter to continue...")
	timer1.stop()
	print timer1.get_mins()

	timer1.start()
	time.sleep(20)
	#~ raw_input("Press Enter to continue...")
	timer1.stop()
	print timer1.get_mins()

