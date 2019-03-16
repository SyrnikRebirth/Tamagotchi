import time
import ClassPet
import sys
import threading


def my_input(stop_event):
    while not stop_event.is_set():
        global command
        command = input()


command = ""
print("Welcome!!")
print("Would you like to adopt one of our tamagotchi?")
print("")
print("1. Get yourself a tamagotchi")
print("2. Quit")
print("")
command = input()
if command.isdigit():
    if int(command) in [1, 2]:
        if (command == "1"):
            print("")
            print("Please name your new pet")
            print("")
            word = input()
            start_time = time.time()
            pet = ClassPet.Tamagotchi(word)
        else:
            print("")
            print("Farewell, Ashen One")
            sys.exit()
    else:
        print("")
        print("I don't understand you. Can you repeat?")
        print("")
else:
    print("")
    print("I don't understand you. Can you repeat?")
    print("")
command = ""
s_stop = threading.Event()
s = threading.Thread(target=my_input, args=(s_stop,), daemon=True)
s.start()
while True:
    print("")
    print("List of options:")
    print("1. Feed")
    print("2. Teach")
    print("3. Play")
    print("4. Voice")
    print("5. Current status")
    print("6. Quit")
    print("")

    while command == "":
        try:
            pet.death()
        except Exception:
            sys.exit()

        if time.time() - start_time >= 300:
            for i in range(int((time.time() - start_time)) // 300):
                pet.change_status()
            start_time = time.time()
            print("")
            print("Your pet has just updated its status")
            pet.status()

    if command.isdigit():
        if int(command) in range(7):
            if (command == "1"):
                pet.feed()
            elif (command == "2"):
                command = ""
                print("")
                print("Please, enter your sentence")
                print("")
                while command == "":
                    time.sleep(1)
                pet.teach(command)
            elif (command == "3"):
                command = ""
                print("")
                print("I know two games. In which one you want to play?")
                print("1. Thimbler game")
                print("2. Calculator game")
                print("3. I don't want to play with you")
                print("")
                print("Please, select an option")
                print("")
                s_stop.set()
                while command == "":
                    time.sleep(1)
                if int(command) in [1, 2, 3]:
                    if (command == "1"):
                        pet.play_thimbles()
                        s_stop.clear()
                        s.join()
                        s = threading.Thread(target=my_input, args=(s_stop,), daemon=True)
                        s.start()
                    elif (command == "2"):
                        pet.play_calculator()
                        s_stop.clear()
                        s.join()
                        s = threading.Thread(target=my_input, args=(s_stop,), daemon=True)
                        s.start()
                    else:
                        print("")
                        print("Ohh, it's okay")
                        pet.sadness += 3
                        print("")
                        s_stop.clear()
                        s.join()
                        s = threading.Thread(target=my_input, args=(s_stop,), daemon=True)
                        s.start()
                else:
                    print("")
                    print("Sorry i can't understand you")
                    print("")
            elif (command == "4"):
                pet.voice()
            elif (command == "5"):
                print("")
                pet.status()
            elif (command == "6"):
                print("")
                print("Farewell, master")
                sys.exit()
        else:
            print("")
            print("I can't understand you. Can you repeat?")
            print("")
    else:
        print("")
        print("I can't understand you. Can you repeat?")
        print("")
    command = ""
s.join()
