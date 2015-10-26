'''
Application to find and replace "tags" in a template file and create a final doc

exec format: python main.py <temp_name> <op_name>

matching pattern : <$ $>
'''
import sys;

def checkFile(fpath):
	tempfile = None;
	try:
		tempfile = open(fpath,"r");
	except FileNotFoundError:
		print("-- "+fpath+" not found...");
		tempfile = None;
	return(tempfile);

#Main
ifloc = str();
ofloc = str();
taglist = list();
tags = str();
reps = str();
replist = list();

if len(sys.argv) < 2:
	print("missing arguments...");
	exit();
else:
	ifloc = sys.argv[1];
	ofloc = sys.argv[2];
	
#print(floc);

temp = checkFile(ifloc);

if temp is None:
	exit();

tempcontent = list();	
for line in temp.readlines():
	tempcontent.append(line.strip("\n"));
temp.close();

tags = input("Enter the tag names, separate them with ','\n->");
taglist = tags.split(",");

matchdict = dict();

for val in taglist:
	matchdict[val] = input("replace : "+val+" -> ");

#print(matchdict.keys());

of = open(ofloc,"w+");

for line in tempcontent:
	for key in matchdict.keys():
		teststr = "<$"+key+"$>";
		if teststr in line:
			line = line.replace(teststr,matchdict[key]);
	of.write(line);

of.close();
exit();
