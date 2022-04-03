import subprocess

data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('ISO-8859-1').split('\n')
profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
f = open("psw.txt","w+")
for i in profiles:
    results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('ISO-8859-1').split('\n')
    results = [b.split(":")[1][1:-1] for b in results if "Key content" in b]
    try:
        f.write("{:<30}/{:<}    |".format(i, results[0]))
    except IndexError:
        f.write("{:<30}/{:<}    |".format(i, ""))

f.close()

#Creator: Marco Tomasi
#Github: MarcoTomasi28

#Before using this code I encourage you to read the README file and the LICENCE