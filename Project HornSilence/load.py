'''USED TO LOAD LOCATIONS INTO SYSTEM'''
import serial;

#ser = serial.Serial("/dev/ttyACM0",9600);

def main():
	#Get current location
	#Calculate Quadrant
	#load file for specific quadrant
	locs = open("./files/loc.txt","r");
	locations = list();
	for loc in locs.readlines():
		loc = loc.split(",");
		x = loc[0];
		y = loc[1];
		if "\n" in x:
			x = x.strip("\n");
		if "\n" in y:
			y = y.strip("\n");
		locations.append({float(x),float(y)})
	locs.close();
	return(locations);
	
def getpos(): 
	#Used to get the current position
	pos = list();
	
	lat = "Lattitude : 1906.9101";#ser.readLine();
	lon = "Longitude : 07252.6660";#ser.readLine();
	
	lat = float(lat.split(":")[1].lstrip().rstrip());
	lon = float(lon.split(":")[1].lstrip().rstrip());
	
	lat=lat/100;
	lon=lon/100;
	
	pos.append(lat); #X Coordinate : FLOAT
	pos.append(lon); #Y Coordinate : FLOAT
	
	return(pos);
