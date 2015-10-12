from bs4 import BeautifulSoup;
import urllib2;

class search:
	
	name = {"fname":str(),"lname":str()};
	search_url = str();
	
	def __init__(self,name):
		name = name.strip(" ");
		mixname = name.split(" ");
		self.name["fname"] = mixname[0];
		self.name["lname"] = mixname[1];
		self.search_url = "https://www.facebook.com/public?query="+self.name["fname"]+"+"+self.name["lname"]+"&init=dir&nomc=0";
