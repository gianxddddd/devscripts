DevScripts
build 4403, 06-01-21 4:09:20
---------------------------------------
devscripts (or simply called as devscript) is a terminal tool used by developers for purposes.

devscripts features ArtASCII, Binary Converter,
Base64 Encoder/Decoder, jadx, youtube_dl
and many more..

Some features are made by the creator:
audiocomp - Audio player for nerds.
viscomp - a Shady visualizer made for low-latency audio.

devscripts and it's features are written in Python, Java, Bash, Batch, and C++
---------------------------------------
-- Required Libraries and Runtime --

To run devscripts, you have to install some of the required libraries & runtimes
if you haven't installed them:

[GNU/Linux]
- Bash
- mplayer [optional]
- OpenJDK 11

[Windows]
- Batch
- mplayer [optional]
- OpenJDK 8

[macOS]
devscripts is not tested yet on macOS, feel free to contact borcillofg2020@gmail.com for testing.

-----------------------------------------
-- Running devscripts --

If you have installed all the required libraries & runtimes, you can now fully run devscripts.

[GNU/Linux]
1. If the folder "__pycache__" exists in some folders, delete as it optimizes Python memory.
2. Open terminal, then do "cd devscripts_path_here"
3. After setting the directory to the main directory of Devscripts, do "sh devscript_linux.sh"

[Windows]
1. Do the same from step 1 of GNU/Linux
2. Open Command Prompt or cmd.exe, then do "cd devscripts_path_here"
3. Now do "devscript_windows.bat"

[macOS]
devscripts is not tested yet on macOS, feel free to contact borcillofg2020@gmail.com for testing.

------------------------------------------
-- Troubleshooting --

Q. devscripts consumes alot of my RAM or CPU.
A. Delete the folder "__pycache__" if it exists in some folders.

Q. devscripts gets killed after executing a scriptfile.
A. If the main script is modified, reinstall devscripts.

Q. Exiting one of the scripts says "No child processes."
A. You might have to remove "os.wait()" at the line 15
   in the script "main.py" if the code exists.

Q. youtube_dl takes so long to download a video.
A. That's because it is randomized to pick it's video quality,
   the more higher the quality is, the more filesize is larger,
   Re-run the scriptfile if it really takes so long to download.

Q. Executing a scriptfile tooks so long to execute.
A. Reinstall Python, as devscripts is written in Python.

Q. devscripts raises error saying "Unknown terminal type."
A. If you are running devscript in some Integrated Development Environments, you might experience this issue.
   If you get annoyed this error too far, remove the code "os.system('clear')" because that is occuring this issue,
   If you are running devscript in Terminal, the terminal might have an issue.

If you have caught a bug/error, please send the report to borcillofg2020@gmail.com
----------------------------------------
-- Author --

GianXD
borcillofg2020@gmail.com
----------------------------------------
Thanks for using DevScripts!