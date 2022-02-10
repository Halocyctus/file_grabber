import os, shutil, time, string

garbanzos_arroz = [] #ALL POSITIVES
logo = """ \n________________________welcome___to______________________________                                                             \n,-.----.                                                         \n\    /  \                ___                                     \n|   :    \             ,--.'|_                                   \n|   |  .\ :   ,---.    |  | :,'                                  \n.   :  |: |  '   ,'\   :  : ' :              ,----._,.           \n|   |   \ : /   /   |.;__,'  /    ,--.--.   /   /  ' /   ,---.   \n|   : .   /.   ; ,. :|  |   |    /       \ |   :     |  /     \  \n;   | |`-' '   | |: ::__,'| :   .--.  .-. ||   | .\  . /    /  | \n|   | ;    '   | .; :  '  : |__  \__\/: . ..   ; ';  |.    ' / | \n:   ' |    |   :    |  |  | '.'| ," .--.; |'   .   . |'   ;   /| \n:   : :     \   \  /   ;  :    ;/  /  ,.  | `---`-'| |'   |  / | \n|   | :      `----'    |  ,   /;  :   .'   \.'__/\_: ||   :    | \n`---'.|                 ---`-' |  ,     .-./|   :    : \   \  /  \n  `---`                         `--`---'     \   \  /   `----'   \n                                              `--`-'\n________________________Filegrabber____________By k1909742________"""

print(logo)
idea_de_hambre = input("\nWould you like to create a search log?(y/n)")
print("------Important add the extension at the end fo the file! Example: filename.txt--------")
hambre = input("\nPLease input the name of the file you want to analyse: ")


def preparar_la_mesa():
    if os.name == "posix":
        vamo_a_come(hambre, "/")
        print("Done!!")
    elif os.name == "nt":
        drives_list = []
        alphabet = list(string.ascii_uppercase)
        for e in range(1, len(alphabet)):
            cch = str(alphabet[e]) + ":\\"
            if os.path.exists(cch):
                print("[i]Examining drive..."+cch)
                vamo_a_come(hambre, cch)
        print("Done!!")
    else:
        print("Please use windows or linux when using this tool!!!!!!")

def vamo_a_come(puchero, crema_catalana):
    paella = os.getcwd()  # current working directory
    os.makedirs(os.path.dirname(paella + "/investigate/"), exist_ok=True)  # creates directory in cwd
    i = 0
    for root, dirs, files in os.walk(crema_catalana):  # looks for file in the entire system
        #print(str(os.path.join(root)))
        if puchero in files:
            if i <= 6:#so it does not borring
                time.sleep(2)  # if not everything would be printed at light speed
            print("""[+] File found at: """ + str(os.path.join(root, puchero))+" ~Investigation_name: "+ str(i) + "_" + puchero)# finds file and show
            i = i + 1
            socarrat = paella + "/investigate/" + str(i) + "_" + puchero  # destination files to analyse
            shutil.copy(os.path.join(root, puchero), socarrat)  # gets the ingirdients, enjoy your meal
            garbanzos_arroz.append("""[+] File found at: """ + str(os.path.join(root, puchero))+" ~Investigation_name: "+ str(i) + "_" + puchero)#for log files later

def digestion(calentito,reflujo):
    if reflujo.lower() == "y":
        acidez = open(os.getcwd()+"/investigate/log.txt", "w")
        acidez.write(logo)
        acidez.write("\nFile has been found at:")
        for i in range(1,len(calentito)):
            acidez.write("\n"+calentito[i])
        acidez.close()
        print("Log file has been created")
    else:
        print("No log has been created")

preparar_la_mesa()
digestion(garbanzos_arroz,idea_de_hambre)

# NOTES FOR FUTURE SELF ------
# For linux. The lookup of the file could also be done by os.popen(find . -name [actual name]) then stream.read()
# Also, the subproces command makes it even more suitable.
# Uses the algorithm of eating in spanish to make following easy for me. However, it applies a layer of obfuscation to the public.
# NOTES FOR FUTURE SELF ------
