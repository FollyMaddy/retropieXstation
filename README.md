# Now there is a bash alternative, see for more info on :

# https://github.com/FollyMaddy/RetroRun

#

# Pyhthon3 versions should work now !

#

# retropieXstation.py (python3 version) python2/retropieXstation.py (python2.7 version)

use :

retropieXstation.py is a simple project to run allmost all ROMS of RetroPie from your windows desktop enviroment (X).

#

dependancies :

This program only works if RetroPie is installed on your computer.

Also make sure you have installed the desired python-modules.

#

How to run :

Make the program executable, dubbleclick and choose open in terminal.

You can run it also directly from the terminal with : 

```
python retropieXstation.py
```

Or run it from the terminal with : 

```
./retropieXstation.py
```

With `uv`, if installed : 

```
uv run retropieXstation.py
```

or online :
```
curl https://raw.githubusercontent.com/FollyMaddy/retropieXstation/refs/heads/master/retropieXstation.py|uv run -
```

#

# retropieXstation-verbose.py (python3 version) python2/retropieXstation-verbose.py (python2.7 version)

Use : 

retropieXstation-verbose is a program to start ROMS of RetroPie in verbose mode from your windows desktop enviroment (X).

Sometimes roms or emulators do not work. This program is created to find the problems.

# Beware : It only works with retroarch libretro cores and zip files are not supported !

#

Dependencies : 

This program only works if RetroPie is installed on your computer.

Also make sure you have installed the desired python-modules.

#

How to run :

Make the program executable, dubbleclick and choose open in terminal.

You can run it also directly from the terminal with : 

```
python retropieXstation-verbose.py
```

Or run it from the terminal with : 

```
./retropieXstation-verbose.py
```

With `uv`, if installed : 

```
uv run retropieXstation-verbose.py
```

or online :
```
curl https://raw.githubusercontent.com/FollyMaddy/retropieXstation/refs/heads/master/retropieXstation-verbose.py|uv run -
```

#

# retropieXstation-800x600.py (python3 version) python2/retropieXstation-800x600.py (python2.7 version)

Use : 

retropieXstation-800x600 is a simple program created to run allmost all ROMS of RetroPie from your windows desktop enviroment (X).

Mainly created for old x86 pc's with old gfx-card.

Old gfx cards don't run the program emulationstation very well and are slow in high resolutions. 

With this program you bypass this problem !

- It get's the standard resolution;

- When running the emulator it changes to 800x600 ;

( An exception is made for the system 'pc' .sh scripts. It will start in standard resolution);

- It changes back to the standard resolution if you stop the emulator.

# Beware : It only works with Xorg, Wayland is not supported !

#

dependancies :

This program only works if RetroPie is installed on your computer.

Also make sure you have installed the desired python-modules.

#

How to run :

Make the program executable, dubbleclick and choose open in terminal.

You can run it also directly from the terminal with : 

```
python retropieXstation-800x600.py
```

Or run it from the terminal with : 

```
./retropieXstation-800x600.py
```

With `uv`, if installed : 

```
uv run retropieXstation-800x600.py
```

or online :
```
curl https://raw.githubusercontent.com/FollyMaddy/retropieXstation/refs/heads/master/retropieXstation-800x600.py|uv run -
```

# use-vesa.conf

(for use on X86 computers)

If the resolution 800x600 is not possible with RetroRun :

Try another monitor and/or paste and use the file /usr/share/xorg.conf.d/use-vesa.conf .

A reboot is necessary to turn the computer into VESA mode, if file is used.

Remove the file if you want to turn back to the normal state.


With Debian Buster I found that this solution did not work ! :

(Here I did not use the file use-vesa.conf at all !)

If you run "xrandr" in terminal and you get "WAYLAND0 connected" then,

"uncommented" a line in deamon.conf (can also be another file check with (cat \*.\*))

sudo nano /etc/gdm3/daemon.conf

#WaylandEnable=false

change to :

WaylandEnable=false



