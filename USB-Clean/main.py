#Code to undo virus
import sys;
import os;
from usb import Usb;

backup = ["~\$WM.FAT32","~$WM.FAT32","Thumbs.db","autorun.inf","Autorun.inf","RECYCLER","\xa0"," .exe"];
db = list();
db_new = list();
depth = 0;
exec_root = os.getcwd();

def bringBack(depth):
	for i in range(1,depth):
		os.system("mv -v * ../");
		os.chdir("../");
		files = os.listdir();
		
		for obj in files:
			if obj is "_":
				linuxRem("_");
			if obj is "\xa0":
				linuxRem("\xa0");
		disinfect();
				
def linuxRem(fname):
	files = os.listdir();
	for obj in files:
		if obj is fname:
			os.system("rm -rfv '"+fname+"'");
			#print("[linuxRem] Removed "+fname+"...");

def disinfect():
	files = os.listdir();
	exes = list();
	
	for test in files:
		if test in db:
			os.system("rm -rfv "+test);
			files.remove(test);
			#print("[disinfect] Removed "+test+"...");
			
#"Learning" about new files
	if len(files) > 0:		
		for test in files:
			if ".ini" in test:
				linuxRem(test);
				db_new.append(test);
			if ".lnk" in test:
				linuxRem(test);
				db_new.append(test);
			if ".vbs" in test:
				linuxRem(test);
				db_new.append(test);
			if ".Trash" in test:
				linuxRem(test);
				db_new.append(test);
			if "{" in test:
				linuxRem(test);
				db_new.append(test);
			if ".BIN" in test:
				linuxRem(test);
				db_new.append(test);
			
		for test in files:
			if ".exe" in test:
				exes.append(test);
		for test in exes:
			if test.strip(".exe") in files:
				linuxRem(test);
				print("removed "+test);
				if test not in db:
					db_new.append(test);
		try:
			os.remove("~$WM.FAT32");
		except FileNotFoundError:
			print("");
			
		try:
			os.remove("\xa0.exe");
		except FileNotFoundError:
			print("");
'''----------------------[setup]'''
os.system("clear");
try:
	db_file = open("list.txt","r");
	for line in db_file.readlines():
		db.append(line.strip("\n"));
	db_file.close();
	print("--Setup: Loading list completed");
except FileNotFoundError:
	print("\n\n --Setup: Error: Virus list not found, using backup list...");
	db = backup;
	print(" --Setup: Creating virus list");
	db_file = open("list.txt","a+");
	for line in backup:
		db_file.write(line+"\n");
	db_file.close();

#find pendrive
user = input("Username: ");
USB = Usb(user);
devices = USB.getDevices();
for i in range(0,len(devices)):
	print(str(i)+" - "+devices[i]);
dev_no = int(input("Enter the number of the device: "));
root = USB.findDevice(devices[dev_no]);
path = root;

#start virus removal

print(" -- Entering level 1");
os.chdir(root);
depth = 1;
l1 = os.listdir();
print("L1 : "+str(os.listdir()));
disinfect();
print("\n\nL1 DONE...\n\n");
#LEVEL 1 CLEANED

print("\n\n -- Entering Level 2");
if "_" in os.listdir():
	os.chdir(os.getcwd()+"/"+"_");
elif "\xa0" in os.listdir():
	os.chdir(os.getcwd()+"/"+"\xa0");
else:
	print("Level 1 doesn't seem to have fake dir present... aborting..");
	bringBack(depth);
	if "_" in os.listdir():
		linuxRem("_");
	if "\xa0" in os.listdir():
		linuxRem("\xa0");
	exit();
path = os.getcwd();
depth=2;
disinfect();

#LEVEL 2 CLEANED

print("\n\n -- Entering Level 3");

if "_" in os.listdir():
	os.chdir(os.getcwd()+"/"+"_");
elif "\xa0" in os.listdir():
	os.chdir(os.getcwd()+"/"+"\xa0");
else:
	print("Level 2 seems to be end of depth...");
	bringBack(depth);
	if "_" in os.listdir():
		linuxRem("_");
	if "\xa0" in os.listdir():
		linuxRem("\xa0");
	exit();
depth=3;
path=os.getcwd();
l3 = os.listdir();
print("l3 : "+str(l3));
disinfect();
print("\n\n -- Commencing reverting procedure");
bringBack(depth);

for doc in os.listdir():
	if "_" in doc:
		linuxRem(doc);
	if "\xa0" in doc:
		linuxRem(doc);

disinfect();
if "\xa0.exe" in os.listdir():
	linuxRem("\xa0.exe");

print("\n\n -- Finished reverting...\nContents:");
print(os.listdir());

print("Updating virus list....\nContents:");
print(db_new);

os.chdir(exec_root);
db_file = open("list.txt","a");
for line in db_new:
	db_file.write(line+"\n");
db_file.close();

print("\n\n -- DONE --");
