#!/usr/bin/python
#
# Program : retropieXstation.py
# Version : 1.3
# Use : 
# retropieXstation is a simple program created to run allmost all ROMS of RetroPie from your windows desktop enviroment (X).
# Dependencies : 
# This program only works if RetroPie is installed on your computer.
# Also make sure you have installed the desired python-modules.
# How to run :
# Make the program executable, dubbleclick and choose open in terminal.
# You can run it also directly from the terminal with : python retropieXstation.py
# Or run it from the terminal with : ./retropieXstation.py
#
# Author : Folkert van der Meulen
# Date   : 23/08/2018
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

import Tkinter as tk
import tkFileDialog
import os

# get filename for use in commandline
root = tk.Tk()
root.withdraw()
ROM = tkFileDialog.askopenfilename(initialdir = '~/RetroPie/roms' , title='Load RetroPie Game') 
# cut system type from directory structure for use in commandline
SYSTEM = ROM.split("/", ROM.count("/"))[5]
# create commandline as string (insert system type and filename to run)
cmd_run_emu = '/opt/retropie/supplementary/runcommand/runcommand.sh 0 _SYS_ %s "%s"' %(SYSTEM,ROM)
# run command
os.system(cmd_run_emu)


