import time
import ClassPet

game_started = 0
print("Welcome!!")
print("Would you like to adopt one of our tamagotchi?")
while True:
    if game_started == 0:
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
                    game_started += 1
                else:
                    print("")
                    print("Farewell, Ashen One")
                    break
            else:
                print("")
                print("I don't understand you. Can you repeat?")
                print("")
        else:
            print("")
            print("I don't understand you. Can you repeat?")
            print("")
    else:
        print("")
        print("List of options:")
        print("1. Feed")
        print("2. Teach")
        print("3. Play")
        print("4. Voice")
        print("5. Status")
        print("6. Quit")
        print("")

        command = input()

        try:
            pet.death()
        except Exception:
            break

        if time.time() - start_time >= 300:
            for i in range(int((time.time() - start_time)) // 300):
                pet.change_status()
            start_time = time.time()

        if command.isdigit():
            if int(command) in range(7):
                if (command == "1"):
                    pet.feed()
                elif (command == "2"):
                    print("")
                    print("Please, enter your sentence")
                    print("")
                    word = input()
                    if word == "":
                        print("")
                        print("Sorry, i can't understand you")
                        print("")
                    else:
                        pet.teach(word)
                elif (command == "3"):
                    print("")
                    print("I know two games. In which one you want to play?")
                    print("1. Thimbler game")
                    print("2. Calculator game")
                    print("3. I don't want to play with you")
                    print("")
                    ans = input()
                    if int(ans) in [1, 2, 3]:
                        if (ans == "1"):
                            pet.play_thimbles()
                        elif (ans == "2"):
                            pet.play_calculator()
                        else:
                            print("")
                            print("Ohh, it's okay")
                            pet.sadness += 3
                            print("")
                    else:
                        print("")
                        print("Sorry i can't understand you")
                        print("")
                elif (command == "4"):
                    pet.voice()
                elif (command == "5"):
                    pet.status()
                elif (command == "6"):
                    print("")
                    print("Farewell, master")
                    break
            else:
                print("")
                print("I can't understand you. Can you repeat?")
                print("")
        else:
            print("")
            print("I can't understand you. Can you repeat?")
            print("")
