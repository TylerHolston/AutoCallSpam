***************************************************************

OKAY READ THIS ENTIRE FILE BEFORE RUNNING ANYTHING. IT IS IMPORTANT YOU HAVE ALL OF THE PROPER TOOLS BEFORERUNNING THE PROGRAM. 
(cause the program is pretty shitty and breakable)
The app runs by using calls to the FaceTime.app. If someone wants to help with getting a windows version up and running please help me! 

***************************************************************

Before execution, you need to have some basic things installed on your OS. First of all, python3.6 or higher. I suggest 3.7.6 || 3.7.7 Here is a link to the install page: https://www.python.org/downloads/. 
Make sure to set python to PATH (should be a little checkbox when installing or might just do it automatically I dont remember).

now you need to update pip. Open your terminal (cmd+spacebar then type in "terminal") You might not need to do this, but to make sure your pip is up to date, run "pip install -U pip". If you are having any permissions errors, run with sudo modifier "sudo pip install -U pip"

PACKAGE INSTALLATION:
    You need to run the following commands.
    "pip install pynput"
    "pip install gTTS"

    These are the only two outside packages this project is reliant on. They shouldn't take too long to run. Any issues, run with sudo modifier in front
    EXAMPLE: "sudo pip install pynput"

MP3Player:
    if you dont already have brew installed, you need to install it for the mp3 audio converter. Just go to this site: brew.sh
    Copy paste the line of code under "INSTALL HOMEBREW" into your terminal.
    This will take longer to install than the pip packages.

mpg123:
    Now that HomeBrew is installed you need to run the following command: "brew install mpg123" again... sudo if you are having any perms issues.

Now all of the dependencies are good to go. There are a couple variables inside of the python files that you are allowed to alter if they are not correct:

    in startCall.py there is a location for your facetime.app which should be correct unless you have moved it somewhere weird. If you have, just find the app and copy the path into the variable name. Just run the program and it will tell you if it can't find it.

    in autoNumber.py there are two pixel locations I have estimated to the best of my ability. The program runs and pops up a call/cancel verification code that could not be bypassed so I use a package to click it using internal mouse input. The two instance variables contain ratios that you can alter to try and get the click right if it doesn't work for your resolution. (bottom right corner of your screen is width=1 height=1 top left corner is width=0 height=0)

Now just run the program by calling the makefile. Command "make -s clean" should do the trick and the -s flag should silence most of the unix commands. Follow the prompts and then sit back.