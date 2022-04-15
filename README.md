#Gideon
This is a Graphical User Interface Desktop Assistant , that is not completed yet but is still usable. It has been designed using PyQt5. It takes the user's query in the form of speech and gives the desired output.

You will have to download all the files and save them in a folder.
Open a powershell window in the main directory where you have saved your files. To do so shift + right click and select Open Poweshell Window here. Then copy paste the following code in the powershell window -

    $fonts = (New-Object -ComObject Shell.Application).Namespace(0x14)
    Get-ChildItem -Recurse -include *.ttf | % { $fonts.CopyHere($_.fullname) }

Hit enter to run the code. Now close the Powershell Window.

Required modules to use this assistant are -

    1.wolframalpha
    2.pyttsx3
    3.speech_recognition
    4.datetime
    5.wikipedia
    6.requests
    7.pywhatkit
    8.pyqt5

To install these modules - 

    1.pip install wolframalpha
    2.pip install pyttsx3
    3.pip install speech_recognition
    4.pip install datetime
    5.pip install wikipedia
    6.pip install requests
    7.pip install pywhatkit
    8.pip install pyqt5

Now you can run the Assistant by running the AssistantGUI.py