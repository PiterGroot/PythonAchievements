import os
import time

asciiWelcome = """\
 __    __    ___  _         __   ___   ___ ___    ___
|  |_-_|  |  /  _]| |       /  ] /   \ |   |   |  /  _]
|  |  |  | /  [_ | |      /  / |     || _   _ | /  [_
|  |  |  ||    _]| |___  /  /  |  O  ||  \_/  ||    _]
|  `  '  ||   [_ |     |/   \_ |     ||   |   ||   [_
 \      / |     ||     |\     ||     ||   |   ||     |
  \_/\_/  |_____||_____| \____| \___/ |___|___||_____|
"""
def Start():
    os.system('cls')
    print(asciiWelcome + "\n")
    print("Welkom bij hangman! De regels zijn simpel: " + "\n" + "Je speelt gewoon galgje, iedere keer als je een woord \n goed raad dan zie je of je het goed of fout hebt. Je typt iedere keer de letter in die je wil invoeren.")
    print("Als je een foute letter invoert, dan komt er een streepje bij de galg. \n Je gaat door totdat je het woord hebt geraden. Als het je niet lukt om het woord te raden, is het game over (als de galg af is)")
    print("Voor de commando's typ in '/cmds' en om dit bericht opnieuw te bekijken '/help'. Veel suc6!")
Start()
##
while True:
    command = input()
    if(command == "/quit" or command == "/QUIT" or command == "/q" or command == "/Q"):
        os.system('cls')
        system.time(10)
        exit()
    if(command == "/cmds"):
        #define logic
        print("\n" + "Typ '/QUIT' ('/q') om het programma te sluiten" + "\n" + "Typ '/help' voor begin tekst")
        print("Om een heel woord te raden typ je 'w' voor je woord bijv: 'w kaas', 'w oceaan' ect.")
        print("Om het schem te legen typ '/cls'")
    if(command == "/help"):
        Start()
    if(command == "/cls"):
        os.system('cls')
        time.sleep(1)
        command = "/help"
