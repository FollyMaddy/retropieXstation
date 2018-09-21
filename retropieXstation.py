#!/usr/bin/python
#
# Program : retropieXstation.py
# Use : retropieXstation is a simple program created to run allmost all ROMS of RetroPie from your windows desktop enviroment (X).
# Dependencies : This program only works if RetroPie is installed on your computer
#
# Author : Folkert van der Meulen
# Date   : 21/08/2018
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

# select romdirectory and select emulator type
root = tk.Tk()
root.withdraw()
DIR = tkFileDialog.askdirectory(initialdir = '~/RetroPie/roms' , title='Choose ROM-directory / System')
# cut system type from directory structure
SYSTEM = DIR.split("/", DIR.count("/"))[5]
# get filename for use in commandline
root = tk.Tk()
root.withdraw()
ROM = tkFileDialog.askopenfilename(initialdir = '%s' %(DIR), title='Load %s FILE' %(SYSTEM)) 
# create commandline as string (insert system type and filename to run)
cmd_run_emu = '/opt/retropie/supplementary/runcommand/runcommand.sh 0 _SYS_ %s "%s"' %(SYSTEM,ROM)
# run command
os.system(cmd_run_emu)


