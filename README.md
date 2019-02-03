# cookdsp
DSP library for Reaper’s plugin language JS

The CookDSP library is a set of functions and objects to help the creation of plugins inside the Reaper software with the built-in JS language. JS is a scripting language which is compiled on the fly and allows you to modify and/or generate audio and MIDI processes, as well as draw custom vector based UI and analysis displays.

One must import the file cookdsp.jsfx-inc in the plugin before using any of the functions documented here. Importing a file is very easy with the import keyword:

    import cookdsp.jsfx-inc

Installation
------------

To install the CookDSP library, put the file _cookdsp.jsfx-inc_  and the folder _cookdsp_ in the Reaper's Effects directory. The location of this directory is (where \<username\> should be replaced by the name of the user's home folder) :

Windows XP :

    C:\Documents and Settings\<username>\Application Data\REAPER\Effects

Windows Vista/7/8 :

    C:\Users\<username>\AppData\Roaming\REAPER\Effects

OSX :

    /Users/<username>/Library/Application Support/REAPER/Effects 

linux (native Reaper) :

    ~/.config/REAPER/Effects

linux (Reaper with Wine) :

    ~/.wine/drive_c/users/<username>/Application Data/REAPER/Effects 

Documentation and tutorials
---------------------------

For a complete documentation, examples and tutorials, visit the CookDSP official web site:

[http://ajaxsoundstudio.com/software/cookdsp/](http://ajaxsoundstudio.com/software/cookdsp/)
