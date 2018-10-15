#!/usr/bin/python
#
# Program : retropieXstation-800x600.py
# Version : 1.0
#
# Use : 
# retropieXstation-resolution is a simple program created to run allmost all ROMS of RetroPie from your windows desktop enviroment (X).
# Mainly created for old x86 pc's with old gfx-card.
# Old gfx cards don't run the program emulationstation very well and are slow in high resolutions. 
# With this program you bypass this problem !
# - It get's the standard resolution;
# - When running the emulator it changes to 800x600;
# - It changes back to the standard resolution if you stop the emulator.
#
# Dependencies : 
# This program only works if RetroPie is installed on your computer.
# Also make sure you have installed the desired python-modules.
#
# How to run :
# Make the program executable, dubbleclick and choose open in terminal.
# You can run it also directly from the terminal with : python retropieXstation-800x600.py
# Or run it from the terminal with : ./retropieXstation-800x600.py
#
# Author : Folkert van der Meulen
# Date   : 15/10/2018
#
# Copyright 2018 Folkert van der Meulen
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

import subprocess
import Tkinter as tk
import tkFileDialog
import os

# get current resolution , suppress quotes etc by [0], suppress new line /n by [:-1]
DISPLAY_PORT = subprocess.Popen('xrandr | grep "connected primary"| cut -d" " -f1',shell=True, stdout=subprocess.PIPE).communicate()[0][:-1]
STANDARD_RESOLUTION = subprocess.Popen('xrandr | grep "*" | cut -d" " -f4',shell=True, stdout=subprocess.PIPE).communicate()[0][:-1]
EMU_RESOLUTION = subprocess.Popen('xrandr | grep "800x600" | cut -d" " -f4',shell=True, stdout=subprocess.PIPE).communicate()[0][:-1]

# only execute if resolution of 800x600 is possible
if EMU_RESOLUTION == '800x600':
    # get filename for use in commandline
    root = tk.Tk()
    root.withdraw()
    ROM = tkFileDialog.askopenfilename(initialdir = '~/RetroPie/roms' , title='Load RetroPie Game') 
    # cut system type from directory structure for use in commandline
    SYSTEM = ROM.split("/", ROM.count("/"))[5]
    # create commandline as string (change resolution for old pc's, insert system type and filename to run)
    cmd_run_emu = 'xrandr --output %s --mode "%s" && /opt/retropie/supplementary/runcommand/runcommand.sh 0 _SYS_ %s "%s"' %(DISPLAY_PORT,EMU_RESOLUTION,SYSTEM,ROM)
    # run command
    os.system(cmd_run_emu)
    # change to standard resolution
    os.system('xrandr --output %s --mode "%s"' %(DISPLAY_PORT,STANDARD_RESOLUTION)) 