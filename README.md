# Stored-Wifi-Password-Exstractor

Created by Marco Tomasi

What is this program?
This is a program written entirely in python (program.py) whose purpose is to extract all wifi passwords saved in a computer.
In order to use the program even on systems without python installed I have also included an .exe version of the file.

----------------------------------------------------------------------------------------------------------------------------

How this program works?
The code uses the "netsh wlan show profile" command and saves the results to a .txt file.
The file is created in the same directory where the file is located and is called psw.txt.
The formatting of the file is as follows:

Network_Name    /    Password    |    Network_name     /      Password     |


---IMPORTANT--
This program in this version only works on computers with windows 10 or 11 in ITALIAN LANGUAGE. I am working on providing 
a version that also supports the English language. Below I write the instructions to use the file with windows in other languages, 
I invite you to follow this procedure only if you have basic knowledge of programming in python.

1-Open the file WifiPassword.py
2-Edit the two strings betwen "" written in italian, above both of them there is a comment to guide you
3-You can try using the translation of those word in your language but i recommend checking by going in the CMD and
  manually execute the commands of the program (netsh wlan show profile and then netsh wlan show profile YOUR_WIFI_NAME key=clear)

----------------------------------------------------------------------------------------------------------------------------
I apologize for any grammatical errors I have made in this text as English is not my first language.