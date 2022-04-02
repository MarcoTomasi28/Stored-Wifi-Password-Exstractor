import subprocess

data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('ISO-8859-1').split('\n')
#Instead of "Tutti i profii utente" insert the tradution in your language.
profiles = [i.split(":")[1][1:-1] for i in data if "Tutti i profili utente" in i]
f = open("psw.txt","w+")
for i in profiles:
    results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('ISO-8859-1').split('\n')
    #Instead of "contenuto chiave" insert the translation in your language.
    results = [b.split(":")[1][1:-1] for b in results if "Contenuto chiave" in b]
    try:
        f.write("{:<30}/{:<}    |".format(i, results[0]))
    except IndexError:
        f.write("{:<30}/{:<}    |".format(i, ""))

f.close()

#Creator: Marco Tomasi
#Github: MarcoTomasi28

#Before using this code I encourage you to read the README file and the LICENCE