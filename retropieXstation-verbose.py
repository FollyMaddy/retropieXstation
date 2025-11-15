#!/usr/bin/python3
#
# Program : retropieXstation-verbose.py3
# Version : 1
# Use :
# retropieXstation-verbose is a program to start ROMS of RetroPie in verbose mode from your windows desktop enviroment (X).
# Sometimes roms or emulators do not work, This program is created to find the problems.
# Beware : It only works with retroarch libretro cores and zip files are not supported !
# Dependencies : 
# This program only works if RetroPie is installed on your computer.
# Also make sure you have installed the desired python-modules.
# How to run :
# Make the program executable, dubbleclick and choose open in terminal.
# You can run it also directly from the terminal with : python retropieXstation-verbose.py
# Or run it from the terminal with : ./retropieXstation-verbose.py
#
# Author : Folkert van der Meulen
# Date   : 02/12/2019
#
# Copyright 2019 Folkert van der Meulen
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#--------------------------------------

import tkinter as tk
import tkinter.filedialog
import os

# get filename for use in commandline
root = tk.Tk()
root.withdraw()
ROM = tk.filedialog.askopenfilename(initialdir = '~/RetroPie/roms' , title='Load RetroPie Game') 

# cut system type from directory structure for use in commandline
SYSTEM = ROM.split("/", ROM.count("/"))[5]

# read emulators.cfg of the selected SYSTEM, if available, and get the default commandline
# program stops if no emulators.cgf file is found (ports have no emulators.cgf)
lines = [line.rstrip('\n') for line in open("/opt/retropie/configs/%s/emulators.cfg" %(SYSTEM),"r")]

# create commandline as string (insert system type and filename to run)
for line in lines:
   result = line.startswith('default')
   if result == True:
      defaultemu = line.split("\"", line.count("\""))[1]
for command in lines:
   result = command.startswith('%s' %(defaultemu))
   if result == True:
      cmd_run_emu = command.split("\"", command.count("\""))[1]
      if 'retroarch' in cmd_run_emu:
         cmd_run_emu = cmd_run_emu.replace("-L ", "-v -L \"").replace(" --config", "\" --config").replace("%ROM%", "\"" + ROM + "\"")
         print("This pure commandline is generated to start your game :")
         print("\n")
         print(cmd_run_emu)
         print("\n")
         print("\n")
         # run command
         print("Verbose output:")
         print("\n")
         os.system(cmd_run_emu)
         print("\n")
         print("\n")
         print("Read the verbose output on the terminal !")
         print("Use it to find your problem.")
         print("I hope it helps !")
      else:
         print("This program only starts \"Retroarch librtro cores\" in verbose mode.") 
         print("Try again.")
      
# read variable exit, after input the program stops 
print("\n")
exit = input("enter to exit :")

