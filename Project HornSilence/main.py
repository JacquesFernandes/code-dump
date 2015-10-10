'''MAIN EXECUTION FILE'''
import load;
import math;

def dist(ax,ay,bx,by):
	x2 = (ax-bx)*(ax-bx);
	y2 = (ay-by)*(ay-by);
	res =math.sqrt(x2+y2);
	return(res);

def calcQuad(x,y):
	x_int = int(str(x).split(".")[0]);
	stry = str(y);


'''MAIN CODE '''
locations = load.main();
print(locations);

pos = list();
buff = list();

pos = load.getpos();

midx = pos[0];
midy = pos[1];

x0 = midx-0.005;
y0 = midy-0.005;

x1 = midx+0.005;
y1 = midy+0.005;

# Window/buffer is made. Now to populate the buffer
buff = locations;	
# Buffer populated. Checking...

for i in range(0,len(buff)):
	tloc = buff[i]; #Target location (no honking center)
	ntlocx = tloc.pop();
	ntlocy = tloc.pop();
	res = dist(ntlocx,ntlocy,pos[0],pos[1])
	if res <= 0.0018:
		print("\nDISABLING HORN @ "+str(res)+" \n target_coord: "+str(ntlocx)+","+str(ntlocy)+"\n current position: "+str(pos[0])+","+str(pos[1]));
	pos = load.getpos();
