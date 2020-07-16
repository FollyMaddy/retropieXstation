# Now there is a bash alternative, see for more info on :

# https://github.com/FollyMaddy/RetroRun

#

# Pyhthon3 versions should work now !

#

# retropieXstation.py (python2.7 version) / retropieXstation.py3 (python3 version)

use :

retropieXstation.py is a simple project to run allmost all ROMS of RetroPie from your windows desktop enviroment (X).

#

dependancies :

This program only works if RetroPie is installed on your computer.

Also make sure you have installed the desired python-modules.

#

How to run :

Make the program executable, dubbleclick and choose open in terminal.

You can run it also directly from the terminal with : python retropieXstation.py

Or run it from the terminal with : ./retropieXstation.py

#

# retropieXstation-verbose.py (python2.7 version) / retropieXstation-verbose.py3 (python3 version)

Use : 

retropieXstation-verbose is a program to start ROMS of RetroPie in verbose mode from your windows desktop enviroment (X).

Sometimes roms or emulators do not work. This program is created to find the problems.

Beware : It only works with retroarch libretro cores and zip files are not supported !

#

Dependencies : 

This program only works if RetroPie is installed on your computer.

Also make sure you have installed the desired python-modules.

#

How to run :

Make the program executable, dubbleclick and choose open in terminal.

You can run it also directly from the terminal with : python retropieXstation-verbose.py

Or run it from the terminal with : ./retropieXstation-verbose.py

#

# retropieXstation-800x600.py (python2.7 version) / retropieXstation-800x600.py3 (python3 version)

Use : 

retropieXstation-resolution is a simple program created to run allmost all ROMS of RetroPie from your windows desktop enviroment (X).

Mainly created for old x86 pc's with old gfx-card.

Old gfx cards don't run the program emulationstation very well and are slow in high resolutions. 

With this program you bypass this problem !

- It get's the standard resolution;

- When running the emulator it changes to 800x600 ;

( An exception is made for the system 'pc' .sh scripts. It will start in standard resolution);

- It changes back to the standard resolution if you stop the emulator.

#

dependancies :

This program only works if RetroPie is installed on your computer.

Also make sure you have installed the desired python-modules.

#

How to run :

Make the program executable, dubbleclick and choose open in terminal.

You can run it also directly from the terminal with : python retropieXstation-800x600.py

Or run it from the terminal with : ./retropieXstation-800x600.py


# use-vesa.conf

(for use on X86 computers)

If the resolution 800x600 is not possible with RetroRun :

Try another monitor and/or paste and use the file /usr/share/xorg.conf.d/use-vesa.conf .

A reboot is necessary to turn the computer into VESA mode, if file is used.

Remove the file if you want to turn back to the normal state.


With Debian Buster I found that this solution did not work ! :

If xrandr is used and you get WAYLAND0 connected then,

"uncommented" a line in deamon.conf (can also be another file check with (cat .))

sudo nano /etc/gdm3/daemon.conf

#WaylandEnable=false

change to :

WaylandEnable=false



