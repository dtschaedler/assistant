import time
import math
import os

#config_data[0] = u_name
update_data[0] = "holdvalue"

run = 1
cfg_exists = os.path.isfile('config.txt')

def casual():
		while run == 1:
			clear()
			ru_name = u_name.replace("\n","")
			print "      _______      Hey " + ru_name + "!"
			print " ^   ~\     /~   ^ "
			print " _    ( 0_0 )    _ Default Packages;"
			print " \\\  /  ___  \  // [1]Desktop"
			print " |\\\/  |   |  \//|"
			print " | \\\ /_____\ // | Add-Ons:"
			print "|-|-|-|-|-|-|-|-|-|[2]EmulationStation"
			print "-|-|-|-|-|-|-|-|-|-[3]Kodi"
			print "==================="
			print "                   Tools:"
			print "                   [4]Install Packages"
			print "                   [5]Update Packages"
			print "                   [7]Setup This Script"
			print "                   [8]Update Me"
			print ""
			print "                   [0]Quit to Command Line"
			print ""
			usr_in = raw_input("Raspi Assistant -->")
			usr_in = str(usr_in)
			usr_in.lower
			
			#Default Programs
			if (usr_in == "1") or (usr_in == "desktop"):
				os.system('startx')
			
			#Add-Ons
			if (usr_in == "2") or (usr_in == "emulationstation") or (usr_in == "games") or (usr_in == "emulators"):
				os.system('emulationstation')
			if (usr_in == "3") or (usr_in == "kodi"):
				os.system('kodi')
			
			#Tools
			if (usr_in == "4") or (usr_in == "install packages") or (usr_in == "install"):
				clear()
				print "Please choose a package to install:"
				print ""
				print "[1]SciTE"
				print "[2]KODI"
				print "[3]Epiphany Browser"
				print ""
				print "Harder Packages:"
				print "[4]EmulationStation"
				print ""
				print "[9]All listed"
				print "[0]Back"
				print 
				usr_in2 = raw_input('>')
				usr_in2 = str(usr_in2)
				usr_in2.lower
				
				program = ["scite","kodi","epiphany-browser","emualtionstation"]
				
				if (usr_in2 == "1") or (usr_in2 == "scite"):
					packages(program[0])
				elif (usr_in2 == "2") or (usr_in2 == "kodi"):
					packages(program[1])
				elif (usr_in2 == "3") or (usr_in2 == "epiphany browser") or (usr_in2 == "epiphany"):
					packages(program[2])
				elif (usr_in2 == "4") or (usr_in2 == "emulationstation"):
					clear()
					print "Installing EmulationStation (RetroPie) is Difficult."
					confirm = raw_input("Enter yes to continue: [y/n]>")
					confirm = str(confirm)
					confirm.lower
					if (confirm == "y") or (confirm == "yes"):
						ins_retropie()
					else:
						clear()
				elif (usr_in2 == "9") or (usr_in2 == "all listed") or (usr_in2 == "all"):
					akeep = 1
					num = 0
					while akeep == 1:
						if num == 3:
							akeep = 0
						else:
							clear()
							packages(program[num])
						num = num + 1
					clear()
					
					print "Installed " + str(program)
					cont()
					clear()
				elif (usr_in2 == "0") or (usr_in2 == "back"):
					clear()
			
			if (usr_in == "5") or (usr_in == "update") or (usr_in == "update packages"):
				print "Running apt-get functions..."
				os.system('sudo apt-get update')
				os.system('sudo apt-get upgrade -y')
				os.system('sudo apt-get dist-upgrade -y')
				os.system('sudo apt-get autoremove -y')
				print ""
				print ""
				print "Update Complete!"
				cont()
			if (usr_in == "7") or (usr_in == "setup"):
				config()
				with open('config.txt', 'r') as file:
					config_data = file.readlines()
			
			if (usr_in == "8") or (usr_in == "update me") or (usr_in == "update"):
				update()
			#Quit
			if (usr_in == "0") or (usr_in == "quit"):
				raise SystemExit
			else:
				print "Try again please."

def ins_retropie():
	clear()
	print "First, we have to set some things up..."
	print ""
	print "Making sure we are up to date:"
	os.system('sudo apt-get update')
	time.sleep(1)
	print ""
	print "Installing git..."
	os.system('sudo apt-get install -y git dialog')
	time.sleep(1)
	print ""
	print "Downloading RetroPie-Setup Script (http://www.blog.petrockblocg.com/retropie)"
	os.system('cd')
	os.system("git clone git://github.com/petrockblog/RetroPie-Setup.git")
	print ""
	print "Making the script executable..."
	os.system('chmod +x ~/RetroPie-Setup/retropie_setup.sh')
	print ""
	print "Done with Setup!"
	cont()
	clear()
	print "When prompted, choose Binary Based Installation (the first choice)"
	print "See the RetroPie Website for more support. http://www.blog.petrockblocg.com/retropie"
	cont()
	sudo /home/pi/RetroPie-Setup/retropie_setup.sh
	clear()

def packages(program):
	print "Installing :" + str(program)
	os.system('sudo apt-get install -y ' +program)
	print "Installed " + str(program)

def config():
	clear()
	print "Username?"
	u_name = raw_input(">")
	write_config(0,u_name)
	clear()
	with open('config.txt', 'r') as file:
		config_data = file.readlines()
	clear()
	u_name = config_data[0]

def write_config(line,variable):
	with open('config.txt', 'r') as file:
		config_data = file.readlines()
	
	write_line = str(variable) + '\n'
	config_data[line] = str(write_line)
	
	with open('config.txt', 'w') as file:
		file.writelines( config_data )
	
def make_config():
	f = open('config.txt', 'w')
	f.write("username\n")
	f.close

def launcher(autorun):
	if autorun == 1:
		print "Creating file: launcher.sh..."
		with open('launcher.sh', 'w') as file:
			write1 = "#!/bin/sh\n# launcher.sh\n# Execute assistant.py\nsudo python assistant.py"
			autorun_data[0] = write1
			file.writelines( autorun_data )
		os.system('chmod 755 launcher.sh')
		os.system('cd')
		print "I can now be run with ./launcher.sh."
		cont()
		clear()
	elif autorun == 0:
		print "Removing Launcher..."
		os.system('rm launcher.sh')
		print "Launcher Removed."
		cont()
		clear()
	else:
		clear()
		
def create_updater():
	clear()
	print "Creating the Updater file..."
	with open('assistupdate.sh', 'w') as file:
		write1 = "#!/bin/sh\n# assistupdate.sh\n# Update the assistant.py file\nrm assistant.py\nwget https://raw.githubusercontent.com/dtschaedler/assistant/master/assistant.py"
		update_data[0] = write1
		file.writelines( update_data )
	os.system('chmod 755 assistupdate.sh')
	os.system('cd')
	print "Updater FIle Generated"
	cont()
	clear()

def update():
	clear()
	print "Finding update script..."
	update_exists = os.path.isfile('assistupdate.sh')
	if update_exists == False:
		print "No Update File Found."
		time.sleep(2)
		create_updater()
	else:
		clear()
	print "Double checking..."
	if update_exists == False:
		print "Could not find the script. Update will most likely fail."
		time.sleep(2)
	print "Running updater"
	os.system('./assistupdate.sh')
	print "Update FInished"
	cont()
	clear()
			
def cont():
	hold = raw_input("Press Enter")
	
def clear():
	os.system('clear')

if cfg_exists == False:
	make_config()
	create_updater()
	config()

	
with open('config.txt', 'r') as file:
	config_data = file.readlines()

u_name = config_data[0]

casual()
