import os;

class usb:
	
	username = str();
	run_empty = True;
	media_empty = True;
	
	def __init__(self,name):
		self.username = name;
		
	def checkRun(self):
		try:
			os.chdir("/run/media/"+self.username);
		except FileNotFoundError:
			print("nothing in "+os.getcwd());
			self.run_empty = True
			return(None);
		files = os.listdir();
		if files.__len__() is 0:
			return(None);
		else:
			self.run_empty = False;
			return(files);
	
	def checkMedia(self):
		try:
			os.chdir("/media/"+self.username);
		except FileNotFoundError:
			print("nothing in "+os.getcwd());
			media_empty = True;
			return(None);
		files = os.listdir();
		if files.__len__() is 0:
			return(None);
		else:
			self.media_empty = False;
			return(files);
		
	def getDevices(self):
		devs = list();
		if self.checkMedia() is None and self.checkRun() is None:
			print("NO DEVICES FOUND");
			exit();
			
		if self.checkRun() is not None:
			for x in self.checkRun():
				devs.append(x);
			
			
		if self.checkMedia() is not None:
			for x in self.checkMedia():
				devs.append(x);
				
		return(devs);
		
	def findDevice(self,dev_name):
		try:
			os.chdir("/media/"+self.username);
			if dev_name in os.listdir():
				return(os.getcwd()+"/"+dev_name);
		except FileNotFoundError:
			print("E : device not found in /media");
		try:
			os.chdir("/run/media/"+self.username);
			if dev_name in os.listdir():
				return(os.getcwd()+"/"+dev_name);
		except FileNotFoundError:
			print("E : device not found in /run/media");
