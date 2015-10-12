#Code to undo virus
import sys;
import os;
from usb import usb;

def safeRem(fname):
	try:
		os.remove(fname);
	except FileNotFoundError:
		print(fname+"not present");

#find pendrive
#METHOD 1 - listing /media contents
user = input("Username: ");
USB = usb(user);
devices = USB.getDevices();
#print(devices);
for i in range(0,len(devices)):
	print(str(i)+" - "+devices[i]);
dev_no = int(input("Enter the number of the device: "));
root = USB.findDevice(devices[dev_no]);
#print("Path: "+path);

print(" -- Entering level 1");
os.chdir(root);
l1 = os.listdir();
print("l1 : "+str(os.listdir()));
#print(l1);
safeRem("~$WM.FAT32");
safeRem("Thumbs.db");
safeRem("autorun.inf");
if "RECYCLER" in l1:
	os.system("rm -rf RECYCLER");
	print("Removed RECYCLER");

#LEVEL 1 CLEANED

print("\n\n -- Entering Level 2");
os.chdir(os.getcwd()+"/"+"_");
print("l2 : "+str(os.listdir()));

if "RECYCLER" in os.listdir():
	os.system("rm -rf RECYCLER");
	print("Removed RECYCLER");

#LEVEL 2 CLEANED

print("\n\n -- Entering Level 3");

try:
	os.chdir("./\xa0");
except FileNotFoundError:
	print("Blank dir not found");

l3 = os.listdir();
print("l3 : "+str(l3));

exes = list();

for doc in l3:
	if doc is "\xa0.exe":
		exes.append(doc);
	if ".vbs" in doc:
		os.remove(doc);
	if ".ini" in doc:
		os.remove(doc);
	if doc is "RECYCLER":
		os.system("rm -rf RECYCLER");
	if ".Trash" in doc:
		os.system("rm -rf "+doc);
	if "Autorun.inf" in doc:
		os.system("rm -rf "+doc);	
			
print("\n\n -- .exes : "+str(exes));

for exe in exes:
	name = exe.strip(".exe");
	if name+".exe" in l3:
		os.remove(exe);
		exes.remove(exe);
		print("Removed : "+exe);

print("\n\n -- new : "+str(os.listdir()));

l3 = os.listdir();

print("\n\n -- Commencing reverting procedure");

if len(os.listdir()) is not 0:
	os.system("mv -v * ../");
	
os.chdir("../");
os.rmdir("./\xa0");

print("\n\n -- l2: "+str(os.listdir()));

if len(os.listdir()) is not 0:
	os.system("mv -v * ../");
	
os.chdir("../");
os.rmdir("./_");
