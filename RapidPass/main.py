from keys import Key;
import os;
from random import randint;

#setup
a = Key("a","qz-s");
b = Key("b","g-vn");
c = Key("c","d-xv");
d = Key("d","ecsf");
e = Key("e","3dwr");
f = Key("f","rvdg");
g = Key("g","tbfh");
h = Key("h","yngj");
i = Key("i","8kuo");
j = Key("j","umhk");
k = Key("k","i-jl");
l = Key("l","o-k-");
m = Key("m","j-n-");
n = Key("n","h-bm");
o = Key("o","9lip");
p = Key("p","0-o-");
q = Key("q","1a-w");
r = Key("r","4fet");
s = Key("s","wxad");
t = Key("t","5gry");
u = Key("u","7jyi");
v = Key("v","f-cb");
w = Key("w","2sqe");
x = Key("x","s-zc");
y = Key("y","6htu");
z = Key("z","a--x");

keys = {"a":a,"b":b,"c":c,"d":d,"e":e,"f":f,"g":g,"h":h,"i":i,"j":j,"k":k,"l":l,"m":m,"n":n,"o":o,"p":p,"q":q,"r":r,"s":s,"t":t,"u":u,"v":v,"w":w,"x":x,"y":y,"z":z};

os.system("clear");

length = int(input("Enter the length of the password \n->"));
dist = input("Distinct letters?\n 1 - yes \t2 - no\n->");
if dist is "1":
	dist = True;
else:
	dist = False;
	
init = input("Enter a letter: \n->");

paswd = init;
prevkey = init;

for i in range(0,length-1):
	direct = randint(1,4);
	nextkey = keys[prevkey].keyindir(direct);
	if dist is True:
		while nextkey in paswd:
			direct = randint(1,4);
			nextkey = keys[prevkey].keyindir(direct);
	while nextkey is "-":
		direct = randint(1,4);
		nextkey = keys[prevkey].keyindir(direct);
	paswd = paswd + nextkey;
	if not nextkey.isdigit():
		prevkey = nextkey;

print("password: "+paswd);
