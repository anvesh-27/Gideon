This is a Graphical User Interface Desktop Assistant , that is not completed yet but is still usable. It has been designed using PyQt5. It takes the user's query in the form of speech and gives the desired output.

You will have to download all the files and save them in a folder.
Open a powershell window in the main directory where you have saved your files. To do so shift + right click and select Open Poweshell Window here. Then copy paste the following code in the powershell window -

    $fonts = (New-Object -ComObject Shell.Application).Namespace(0x14)
    Get-ChildItem -Recurse -include *.ttf | % { $fonts.CopyHere($_.fullname) }

Hit enter to run the code. Now close the Powershell Window.

Required modules to use this assistant are -

1.wolframalpha

    pip install wolframalpha

2.pyttsx3

    pip install pyttsx3

3.speech_recognition

    pip install SpeechRecognition

4.datetime

    pip install datetime

5.wikipedia

    pip install wikipedia

6.requests

    pip install requests

7.pywhatkit

    pip install pywhatkit

8.pyqt5

    pip install pyqt5

9.PySide2

    pip install PySide2

10.flask

    pip install flask


If you get an error regarding the pyaudio module. Refer this video https://www.youtube.com/watch?v=-3am_5jMzJ4 or Follow the following steps -

    1. Go to https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio this website.
    2. Select your python version and download the required file.
    3. Open a powershell window where you have installed pyaudio.
    4. Now enter the following code

        pip install PyAudio

    5. Hit Tab key, it will autocomplete the file name.
    6. Hit Enter key.

Now you can run the Assistant by running the AssistantGUI.py