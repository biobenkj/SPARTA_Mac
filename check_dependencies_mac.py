__author__ = 'benkjohnson'

import imp
import os
import glob
import subprocess

class CheckDependencies(object):
    def __init__(self):
        self._answerstate = False


    def installdependencies(self):
        """Ask if the user would like to install dependencies."""

        self._answer = str(raw_input("Would you like SPARTA to try and download and install the missing dependencies? (Y or N):"))
        if self._answer.upper() == "Y" or self._answer.upper() == "YES":
            self._answerstate = True
        else:
            print "You need to install Java, NumPy, matplotlib, R and an appropriate compiler (e.g. gcc) before proceeding."
            print "Now quitting"
            quit()

        return

    def getanswerstate(self):
        """Return self._answerstate"""

        return self._answerstate


    def checkjava(self):
        """Check to see if Java is installed properly and included in the PATH"""

        try:
            subprocess.call(["java", "-version"])

        except:
            print "Couldn't find Java. It might not be installed or not included in the PATH"
            print "If it is not installed, please download and install the latest version of Java"
            print "It can be downloaded from http://www.java.com/en/"
            print "Trimming cannot be performed if Java is not installed. Quitting now."
            quit()


    def checkR(self):
        """Check to see if R is installed properly and included in the PATH"""

        try:
            subprocess.call(["R", "--version"])

        except:
            print "Couldn't find R. It might not be installed or not included in the PATH"
            print "If it is not installed, please install R from within the 'DE_analysis' folder within SPARTA"
            print "Differential gene expression cannot be performed if R is not installed. Quitting now."
            quit()
        return

    def checknumpy(self):
        """Check to see if NumPy module exists"""

        try:
            imp.find_module('numpy')
            self._foundnumpy = True

        except ImportError:
            self._foundnumpy = False

        if self._foundnumpy == False:
            print "You need to install 'NumPy' before proceeding, otherwise HTSeq will not work properly."

        return self._foundnumpy

    def checkhtseq(self):
        """Check to see if HTSeq module exists"""

        try:
            imp.find_module('HTSeq')
            self._foundhtseq = True

        except ImportError:
            self._foundhtseq = False

        if self._foundhtseq == False:
            print "HTSeq doesn't appear to be installed. An attempt will be made to install it for the local user."

        return self._foundhtseq

    # def checkmatplotlib(self):
    #     """Check to see if matplotlib module exists"""
    #
    #     try:
    #         imp.find_module('matplotlib')
    #         foundmatplotlib = True
    #
    #     except ImportError:
    #         foundmatplotlib = False
    #
    #     if foundmatplotlib == False:
    #         print "You need to install 'matplotlib' before proceeding, otherwise HTSeq will not work properly."
    #
    #     return foundmatplotlib

    def getNumPy(self):
        """Get latest NumPy iteration from sourceforge"""

        cd = CheckDependencies()
        subprocess.call(["curl", "-L", "-O", "http://sourceforge.net/projects/numpy/files/latest/download?source=files"])
        spartadir = cd.getSPARTAdir()
        #Make sure the user is in the SpartaDir
        subprocess.call(["mv", os.path.join(spartadir, "download?source=files"), os.path.join(spartadir, "numpy-latest.tar.gz")])
        subprocess.call(["tar", "-zxf", os.path.join(spartadir, "numpy-latest.tar.gz")])
        subprocess.call(["rm", os.path.join("numpy-latest.tar.gz")])
        return

    def installNumPy(self):
        """Install latest NumPy from source"""

        cd = CheckDependencies()
        current_numpy = glob.glob("numpy-*")[0]
        spartadir = cd.getSPARTAdir()
        os.chdir(spartadir + "/" + current_numpy)
        subprocess.call(["sudo python setup.py build install"], shell=True)
        return

    # def getmatplotlib(self):
    #     """Get latest NumPy iteration from sourceforge"""
    #     #IMPORTANT: for htseq-count, matplotlib is NOT required!
    #
    #     subprocess.call(["curl", "-L", "-O", "http://sourceforge.net/projects/matplotlib/files/latest/download?source=files"])
    #     subprocess.call(["mv download\?source\=files matplotlib-latest.tar.gz"], shell=True)
    #     subprocess.call(["tar", "-zxf", "matplotlib-latest.tar.gz"])
    #     subprocess.call(["rm", "matplotlib-latest.tar.gz"])
    #     return
    #
    # def installmatplotlib(self):
    #     """Install latest matplotlib from source"""
    #
    #     current_matplotlib = glob.glob("matplotlib-*")[0]
    #     spartadir = CheckDependencies.getSPARTAdir()
    #     os.chdir(spartadir + "/" + current_matplotlib)
    #     subprocess.call(["python setup.py build"], shell=True) #have not added 'install' yet because several dependencies
    #     #are required to install matplotlib...
    #     return


    def getpwd(self):
        """Get present working directory"""

        present_working_directory = subprocess.Popen("pwd", stdout=subprocess.PIPE).communicate()[0].strip("\n")
        return present_working_directory

    def getdesktoppath(self):
        """Get the path to the desktop"""

        desk_path = os.path.join(subprocess.Popen("echo $HOME", shell=True, stdout=subprocess.PIPE).stdout.readline().strip("\n"), "Desktop")
        return desk_path

    def getSPARTAdir(self):
        """Attempt to figure out where SPARTA is located. Default should be Desktop"""

        desk_path = os.path.join(subprocess.Popen("echo $HOME", shell=True, stdout=subprocess.PIPE).stdout.readline().strip("\n"), "Desktop")
        #This is explicitly coded to ensure that the rest of the functions are able to find the appropriate binaries
        sparta_dir = os.path.join(desk_path, "SPARTA_Mac")
        if not os.path.lexists(desk_path):
            print "Unable to find the Desktop."
        while not os.path.lexists(sparta_dir):
            sparta_dir = str(raw_input("SPARTA_Mac folder is not on the Desktop. Please place the folder on the Desktop or enter the file path for the folder location or enter quit to exit the program:"))
            if sparta_dir.upper() == "Q" or sparta_dir.upper() == "QUIT":
                quit()
            if not os.path.lexists(sparta_dir):
                print("Invalid file path. The path you have selected does not exist or was not written correctly. \nAn example of path on Mac OS X: /Users/yourusername/Desktop/SPARTA_Mac")
        return sparta_dir