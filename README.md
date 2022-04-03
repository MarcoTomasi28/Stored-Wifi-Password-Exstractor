# Stored-Wifi-Password-Exstractor

Created by Marco Tomasi

What is this program?
This is a program written entirely in python (program.py) whose purpose is to extract all wifi passwords saved in a computer.
In order to use the program even on systems without python installed I have also included an .exe version of the file.

----------------------------------------------------------------------------------------------------------------------------

How this program works?
The code uses the "netsh wlan show profile" command and saves the results to a .txt file.
The file is created in the same directory where the file is located and is called psw.txt.
After using the proram if you want to reuse it before runnuing it delete the psw.txt file.
The formatting of the file is as follows:

Network_Name    /    Password    |    Network_name     /      Password     |


--IMPORTANT--
Make sure to use the program in the correct language(the language of your OS), you can choose betwen it (italian) and en (english).
If the program run but the psw.txt file is empty it means that you are using the wrong language (or in your os the aren't 
any saved password)

----------------------------------------------------------------------------------------------------------------------------
I apologize for any grammatical errors I have made in this text as English is not my first language.