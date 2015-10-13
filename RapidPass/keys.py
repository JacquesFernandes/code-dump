'''
Distance based on "key" units
"origin" is "Q"
"-" is treated as unsusable
'''

class Key:
	
	key = str();
	x = float();
	y = float();
	isused = bool();
	up = str();
	down = str();
	left = str();
	right = str();
	
	def __init__(self,key,near):
		self.key = key;
		self.up = near[0];
		self.down = near[1];
		self.left = near[2];
		self.right = near[3];
	
	def keyindir(self,pos):
		if pos is 1:
			return(self.up);
		elif pos is 2:
			return(self.down);
		elif pos is 3:
			return(self.left);
		elif pos is 4:
			return(self.right);

	def __str__(self):
		return(self.key);
