from discord_webhook import DiscordWebhook, DiscordEmbed
import subprocess, platform
import json
#the logo adn some clear shit stolen from stackoverflow 
def logo():
	if platform.system()=="Windows":
		subprocess.Popen("cls", shell=True).communicate() #I like to use this instead of subprocess.call since for multi-word commands you can just type it out, granted this is just cls and subprocess.call should work fine 
	else: #Linux and Mac
		print("\033c", end="")
	print("   ___     __             __  _                    __")
	print("  / _ |___/ /  _____ ____/ /_(_)__ __ _  ___ ___  / /_")
	print(" / __ / _  / |/ / -_) __/ __/ (_-</  ' \/ -_) _ \/ __/")
	print("/_/ |_\_,_/|___/\__/_/  \__/_/___/_/_/_/\__/_//_/\__/ ")
	print("by SpezialK#4807")
#the startmnue 
def startm():
	logo()
	print("do you want to create or load a advertisment?" )
	usage = input("c/l/e: ")
	if usage == "c" or usage == "C":
		return 1
	elif usage == "l" or usage == "U":
		return 2
	elif usage == "e" or usage == "E":
		return 3
	else : return 0
#creating an advertisment
def questions():
		#input()
	logo()
	print("create your advertisment ")
	what = input("whats the tiel of the advertisment? : ")
	des = input("description : ")
	serverinv = input("your server invite : ")
	usern = input("your DC account : ")
	imgurl= input("select an img(the link to one like a dc link)!!")
	color = input("color input(HEX Data) : ")
	color = presets(color)
	#creating a list with all of the data
	scem =[what, des, serverinv,usern, imgurl,color]
	print("do you want to save your advertisment?")
	sa = input("y/n:")
	if sa == "y" or sa == "Y" or sa == "yes" or sa == "Yes":
		name = scem[0] + ".json"
		save(scem,name)	
		return scem 
	else:
		return scem 
#saving a config to a jason file 
def save(d,fname):
	jsonStr = json.dumps(d)
	with open(fname, "w") as outfile:
		outfile.write(jsonStr)
#importing a file 
def imp(fname):
	with open(fname, "r") as infile:
		data = json.load(infile)
	return data
#color presetes might change them to something more coustom in the future or for special events
def presets(hexc):
	#green
	if hexc == "g" or hexc == "G" or hexc == "green" or hexc == "Green":
		return "00b159"
	#red
	elif hexc == "r" or hexc == "R" or hexc == "red" or hexc == "Red":
		return "d11141"
	#blue
	elif hexc == "blu" or hexc == "Blu" or hexc == "blue" or hexc == "Blue" :
		return "00aedb"
	#Orange
	elif hexc == "o" or hexc == "O" or hexc == "orange" or hexc == "Orange" :
		return "f37735"
	#yellow
	elif hexc == "y" or hexc == "Y" or hexc == "yellow" or hexc == "Yellow" :
		return "ffc425"
	#black
	elif hexc == "bla" or hexc == "Bla" or hexc == "black" or hexc == "Black" :
		return "000000"
	#white
	elif hexc == "w" or hexc == "W" or hexc == "white" or hexc == "White" :
		return "1f1f1"
	#grey
	elif hexc == "grey" or hexc == "Grey":
		return "666666"
	else :
		return hexc
#sending the advertisment
def send(sceme):
	where = input("where should we advertise? : ")
	webhook = DiscordWebhook(url=where)
	embed = DiscordEmbed(title=sceme[0], description=sceme[1], color=sceme[5])#the top text the description under it and the color of the slider
	embed.add_embed_field(name='Server invite', value= sceme[2])#server inv
	embed.add_embed_field(name='DC account ', value=sceme[3])
	embed.set_image(url=sceme[4])#the large imag at the botom 
	embed.set_footer(text='get your Own advertisment today!!! SpezialK#4807')
	webhook.add_embed(embed)
	response = webhook.execute()
def editor():
	logo()
	filename = input("input the name of the file you want to edit : ")
	data = imp(filename)
	editing(data,filename)
#prints out the current config for further editing
def printeditoroptions(e):
		print("1. Titel of the advertisment : " , e[0])
		print("2. description of the advertisment : ", e[1])
		print("3. server invite : " , e[2])
		print("4. the discord Tag : ", e[3])
		print("5. the link to the img/gif : " , e[4] )
		print("6. the hex code of your color : ", e[5])
def editing(data,curfile):
	editing = True
	while editing == True:
		logo()
		print("editing file :", curfile)
		printeditoroptions(data)
		opt = int(input("option you want to edit(number) : "))
		data = editing2(data,opt )
		print("do you want to continure editing?")
		opt2 = input("y/n : ")
		if opt2 == "y" or opt2 == "Y" or opt2 == "yes" or opt2 == "Yes":
			editing = True
		else :editing = False
	print("do you want to save changes?: ")
	opt3 = input("y/n : ")
	if opt3 == "y" or opt3 == "Y" or opt3 == "yes" or opt3 == "Yes":
		save(data,curfile)
		print("file saved")
	else: print("file not saved")
def editing2(dat,w):
	w = w-1
	#catching errores to prevent teh program from crashing
	if w >5: print("ERRORE NUMBER TO HIGH !")
	elif w < 1: print("ERRORE NUMBER TO LOW !")
	#so that you can use normal color presets
	elif w == 5:
		Hexc = input("your new option here: ")
		dat[5]=presets(Hexc)
	# for everything else that isn´t a color 
	else:
		print("editing option " , w+1)
		dat[w] = input("your new option here: ")
	return dat
#main funktion
def main():
	opt = startm()
	#creating a new file
	if opt == 1:
		sceme=questions()
		send(sceme)
	elif opt == 2:
		#loading a sceme 
		print("just complete filename if in same directory otherwise completete path")#removed it from teh funktion to make funktion more verstitle 
		Fname = input("filename : ")
		sceme = imp(Fname)
		send(sceme)
	elif opt == 3:
		editor()
	else:print("you gave a Wrong imput!!")
#execution of the program 
main()
