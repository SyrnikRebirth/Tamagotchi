import time
import ClassPet
import sys
import threading


def my_input(stop_event, command):
    while not stop_event.is_set():
        command[0] = input()


def handsome_print(input):
    print("")
    print(input)
    print("")


options1 = '''Welcome!!
Would you like to adopt one of our tamagotchi?

1. Get yourself a tamagotchi
2. Quit
'''

options2 = '''
List of options:
1. Feed
2. Teach
3. Play
4. Voice
5. Current status
6. Quit
'''

options3 = '''
I know two games. In which one you want to play?
1. Thimbler game
2. Calculator game
3. I don't want to play with you

Please, select an option
'''

print(options1)
while True:
    command = input()
    if command.isdigit():
        if int(command) in [1, 2]:
            if (command == "1"):
                handsome_print("Please name your new pet")
                word = input()
                start_time = time.time()
                pet = ClassPet.Tamagotchi(word)
                break
            else:
                handsome_print("Farewell, Ashen One")
                sys.exit()
        else:
            handsome_print("I don't understand you. Can you repeat?")
    else:
        handsome_print("I don't understand you. Can you repeat?")

command = [""]
s_stop = threading.Event()
s = threading.Thread(target=my_input, args=(s_stop, command), daemon=True)
s.start()
while True:
    print(options2)
    while command[0] == "":
        try:
            pet.death()
        except Exception:
            sys.exit()

        if time.time() - start_time >= 300:
            for i in range(int((time.time() - start_time)) // 300):
                pet.change_status()
            start_time = time.time()
            handsome_print("Your pet has just updated its status")
            pet.status()

    if command[0].isdigit():
        if int(command[0]) in range(7):
            if (command[0] == "1"):
                pet.feed()
            elif (command[0] == "2"):
                command[0] = ""
                handsome_print("Please, enter your sentence")
                while command[0] == "":
                    time.sleep(1)
                pet.teach(command[0])
            elif (command[0] == "3"):
                command[0] = ""
                print(options3)
                s_stop.set()
                while command[0] == "":
                    time.sleep(1)
                if int(command[0]) in [1, 2, 3]:
                    if (command[0] == "1"):
                        pet.play_thimbles()
                        s_stop.clear()
                        s.join()
                        s = threading.Thread(target=my_input, args=(s_stop, command), daemon=True)
                        s.start()
                    elif (command[0] == "2"):
                        pet.play_calculator()
                        s_stop.clear()
                        s.join()
                        s = threading.Thread(target=my_input, args=(s_stop, command), daemon=True)
                        s.start()
                    else:
                        handsome_print("Ohh, it's okay")
                        pet.sadness += 3
                        s_stop.clear()
                        s.join()
                        s = threading.Thread(target=my_input, args=(s_stop, command), daemon=True)
                        s.start()
                else:
                    handsome_print("Sorry i can't understand you")
            elif (command[0] == "4"):
                pet.voice()
            elif (command[0] == "5"):
                print("")
                pet.status()
            elif (command[0] == "6"):
                handsome_print("Farewell, master")
                sys.exit()
        else:
            handsome_print("I can't understand you. Can you repeat?")
    else:
        handsome_print("I can't understand you. Can you repeat?")

    command[0] = ""
s.join()
