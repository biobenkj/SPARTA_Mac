Welcome to SPARTA!

SPARTA is a Simple Program for Automated reference-based, bacterial RNA-seq Transcriptome Analysis. It uses Python 2.x.x as means to control the execution of each of the programs and attempt to install any missing dependencies. Python is often already installed on most computers.However, I would recommend downloading and installing the latest Python 2 release from the following location, based on your operating system:

MacOSX: https://www.python.org/downloads/mac-osx/

Windows: https://www.python.org/downloads/windows/

Linux: Use apt to install the latest version of Python 2

To run the software, make sure that the folder “SPARTA_Mac/Windows/Linux” is on the Desktop, along with a folder containing: 1) The FASTQ or FASTQ.gz raw reads, 2) A reference DNA genome file (.fa or .fasta), and 3) A genome feature file (GTF). You can download the reference and genome feature files from: http://bacteria.ensembl.org/info/website/ftp/index.html

IMPORTANT: It is best to make sure that the name of the folder containing your reads, reference, and feature files does NOT contain any spaces. You can use hyphens or underscores if you need separation between terms.

Open the terminal:

MacOSX: Finder -> Applications -> Utilities -> Terminal

Windows: Powershell

Linux: Terminal is likely already on your dock

Navigate to the desktop and into the SPARTA folder:

MacOSX: cd ~/Desktop/SPARTA_Mac

Windows: cd ~/Desktop/SPARTA_Windows

Linux: cd ~/Desktop/SPARTA_Linux

Now that you are in the SPARTA folder, type: python SPARTA.py

This will launch the program. It will attempt to check for dependencies and install any missing dependencies. SPARTA requires: Python, Java, gcc compiler, NumPy, and R. 

If you need to install Java: http://www.java.com/en/

If you need to install R: Within the SPARTA_Mac/Windows/Linux, then in the DE_analysis folder, there is an appropriate package to install R. Follow the instructions and install the software. Finally restart SPARTA.

If you need NumPy or HTSeq, SPARTA will attempt to download and install them. This will require your administrator password to install NumPy. Enter the password when prompted. No characters will appear on the screen, but you are entering characters. Once you’ve put in your password, hit Enter/Return.

From here, hopefully, the software will ask you clear questions about what to do to continue. 

Thanks for using SPARTA!


