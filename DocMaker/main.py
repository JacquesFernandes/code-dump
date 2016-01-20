#!/usr/bin/python3
import os;

if (os.system("which cowsay") is 256):

	print("Welcome To DocMaker!");
	print("For a nicer welcoming experience, please install 'cowsay' if you are using a linux machine :D");

else:
	os.system("cat welcome.txt | cowsay -e '^^'");


fpath = input("location of file: ");

if not fpath.__contains__(".java") and not fpath.__contains__(".py"):
	print("hmm... File type doesn't seem to be implemented (yet)");
	exit();
