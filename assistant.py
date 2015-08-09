import time
import math
import os

#config_data[0] = u_name

run = 1
cfg_exists = os.path.isfile('config.txt')

def casual():
		while run == 1:
			clear()
			ru_name = u_name.replace("\n","")
			print "      _______      Hey " + ru_name + "!"
			print " ^   ~\     /~   ^ "
			print " _    ( 0_0 )    _ [1]Desktop"
			print " \\\  /  ___  \  // "
			print " |\\\/  |   |  \//| [2]Programs"
			print " | \\\ /_____\ // | [3]Manage Programs"
			print "|-|-|-|-|-|-|-|-|-|"
			print "-|-|-|-|-|-|-|-|-|-[9]Settings"
			print "===================[0]Quit to Command Line"
			print ""
			usr_in = raw_input("Raspi Assistant -->")
			usr_in = str(usr_in)
			usr_in.lower
			
			if (usr_in == "1") or (usr_in == "desktop"):
				os.system('startx')
			
			elif (usr_in == "2") or (usr_in == "programs"):
				clear()
				print "Major Add-Ons:"
				print "[1]KODI"
				print "[2]EmulationStation"
				print ""
				print "[0]Back"
				usr_in2 = raw_input('>')
				usr_in2 = str(usr_in2)
				usr_in2.lower
				if (usr_in2 == "1") or (usr_in2 == "kodi"):
					os.system('kodi')
				if (usr_in2 == "2") or (usr_in2 == "emulationstation"):
					os.system('emulationstation')
				if (usr_in2 == "0"):
					clear()
					
			elif (usr_in == "3") or (usr_in == "manage programs"):
				clear()
				print "[1]Install Packages"
				print "[2]Update Packages"
				print "[3]Remove Packages"
				print ""
				print "[0]Back"
				usr_in2 = raw_input('>')
				usr_in2 = str(usr_in2)
				usr_in2.lower
				if (usr_in2 == "1"):
					clear()
					print "Automatic Install:"
					print "[1]SciTE"
					print "[2]KODI"
					print "[3]Epiphany Browser"
					print ""
					print "Semi-Manual Install:"
					print "[4]EmulationStation"
					print ""
					print "[9]All listed"
					print "[0]Back"
					usr_in2 = raw_input('>')
					usr_in2 = str(usr_in2)
					usr_in2.lower
					
					program = ["scite","kodi","epiphany-browser"]
					
					if (usr_in2 == "1") or (usr_in2 == "scite"):
						packages(program[0])
					elif (usr_in2 == "2") or (usr_in2 == "kodi"):
						packages(program[1])
					elif (usr_in2 == "3") or (usr_in2 == "epiphany browser") or (usr_in2 == "epiphany"):
						packages(program[2])
					elif (usr_in2 == "4") or (usr_in2 == "emulationstation"):
						ins_retropie()
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
						print ""
						ins_retropie()
						cont()
						clear()
					elif (usr_in2 == "0") or (usr_in2 == "back"):
						clear()
						
				if (usr_in2 == "2"):
					clear()
					print "Running apt-get functions..."
					os.system('sudo apt-get update')
					os.system('sudo apt-get upgrade -y')
					os.system('sudo apt-get dist-upgrade -y')
					os.system('sudo apt-get autoremove -y')
					print ""
					print ""
					print "Update Complete!"
					cont()
					
				if (usr_in2 == "3"):
					clear()
					print "Automatic:"
					print "[1]SciTE"
					print "[2]KODI"
					print "[3]Epiphany Browser"
					print ""
					print "[9]All listed"
					print "[0]Back"
					usr_in2 = raw_input('>')
					usr_in2 = str(usr_in2)
					usr_in2.lower
					
					program = ["scite","kodi","epiphany-browser"]
					
					if (usr_in2 == "1") or (usr_in2 == "scite"):
						rm_packages(program[0])
					elif (usr_in2 == "2") or (usr_in2 == "kodi"):
						rm_packages(program[1])
					elif (usr_in2 == "3") or (usr_in2 == "epiphany browser") or (usr_in2 == "epiphany"):
						rm_packages(program[2])
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
						
						print "Removed " + str(program)
						cont()
						clear()
					elif (usr_in2 == "0") or (usr_in2 == "back"):
						clear()
				
				if (usr_in2 == "0"):
					clear()
			
			elif (usr_in == "9") or (usr_in == "settings"):
				config()
				with open('config.txt', 'r') as file:
					config_data = file.readlines()
				update()
			
			elif (usr_in == "0") or (usr_in == "quit"):
				raise SystemExit
			else:
				print "Try again please."

def ins_retropie():
	clear()
	print "Making sure we are up to date:"
	os.system('sudo apt-get update')
	print ""
	print "Installing git..."
	os.system('sudo apt-get install -y git dialog')
	print ""
	print "Downloading RetroPie-Setup Script (http://www.blog.petrockblocg.com/retropie)"
	os.system('cd')
	os.system("git clone git://github.com/petrockblog/RetroPie-Setup.git")
	print ""
	print "Making the script executable..."
	os.system('chmod +x ~/RetroPie-Setup/retropie_setup.sh')
	print ""
	print "Done with Setup!"
	print "When prompted, choose Binary Based Installation (the first choice)"
	print "See the RetroPie Website for more support. http://www.blog.petrockblocg.com/retropie"
	cont()
	os.system('sudo /home/pi/RetroPie-Setup/retropie_setup.sh')
	clear()

def packages(program):
	print "Installing :" + str(program)
	os.system('sudo apt-get install -y ' +program)
	print "Installed " + str(program)
	
def rm_packages(program):
	print "Removing :" + str(program)
	os.system('sudo apt-get remove -y ' + program)
	print "Removed " + str(program)

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

def create_updater():
	print "Building the Updater file..."
	with open('assistupdate.sh', 'w') as file:
		write1 = "#!/bin/sh\n# assistupdate.sh\n# Update the assistant.py file\nrm assistant.py\nwget https://raw.githubusercontent.com/dtschaedler/assistant/master/assistant.py"
		update_data = ["hold"]
		update_data[0] = write1
		file.writelines( update_data )
	os.system('chmod 755 assistupdate.sh')
	os.system('cd')
	print "Updater FIle Generated"

def update():
	clear()
	print "Building the update script..."
	with open('assistupdate.sh', 'w') as file:
		write1 = "#!/bin/sh\n# assistupdate.sh\n# Update the assistant.py file\nrm assistant.py\nwget https://raw.githubusercontent.com/dtschaedler/assistant/master/assistant.py"
		update_data = ["hold"]
		update_data[0] = write1
		file.writelines( update_data )
	os.system('chmod 755 assistupdate.sh')
	os.system('cd')
	print "Updater FIle Generated"
	print "Double Checking..."
	update_exists = os.path.isfile('assistupdate.sh')
	if update_exists == False:
		print "No Update File Found."
		create_updater()
		print "Built the updater again. Update may fail if not built correctly"
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

