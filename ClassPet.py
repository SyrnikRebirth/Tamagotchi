import random
import time

class Tamagotchi():


    def __init__(self, name):
        self.name = name
        self.hunger = random.randrange(1, 10)
        self.sadness = random.randrange(1, 10)
        self.sounds = []

    def change_status(self):
        self.sadness += 1
        self.hunger += 1

    def status(self):
        print("")
        print(self.name + " status:")
        print("Hunger: " + str(self.hunger))
        print("Sadness: " + str(self.sadness))
        print("vocabulary: I already know " + str(len(self.sounds)))
        print("")


    def voice(self):
        if len(self.sounds) == 0:
            print("")
            print("You didn't teach me anything.")
            print("")
        else:
            print("")
            print(self.sounds[random.randrange(len(self.sounds))])
            print("")
            self.reduce_sadness()

    def teach(self, word):
        print("")
        print("Ohh, new words?  I like everything new!")
        print("")
        self.sounds.append(word)
        self.reduce_sadness()

    def feed(self):
        print("")
        print("You finally remembered, that I'm starving")
        print("")
        self.reduce_hunger()

    def play_calculator(self):
        print("")
        print("Let's check how well you know how to count numbers")
        print("You will see two numbers and a sign of calculation between them")
        print("your goal is to calculate them in less than 5 seconds")
        print("")
        i = 0
        correct = 0
        while i < 5:
            random.seed()
            operator = random.randint(1, 2)
            a = random.randint(1, 100)
            b = random.randint(1, 100)
            if operator == 1:
                print(a, '+', b, '=')
                answer = a + b
            else:
                print(a, '-', b, '=')
                answer = a - b
            start = time.time()
            input_answer = input()
            if input_answer.isdigit():
                input_answer = int(input_answer)
                if time.time() - start >= 5:
                    print("You didn't manage to do it in time")
                else:
                    if answer == input_answer:
                        correct += 1
                        print("Correct")
                    else:
                        print("Incorrect")
                i += 1
                print("")
                print("You have already answered " + str(i) + " from 5 questions")
                print("")
            else:
                print("")
                print("It's not an answer!!")
                print("")
        print("")
        if correct > 3:
            print("Your score is " + str(correct) + " out of 5")
            print("Congratulations! You are really good at counting!")
        else:
            print("Your score is " + str(correct) + " out of 5")
            print("You need to train more if you want to have better results")
        self.reduce_sadness()
        print("")



    def play_thimbles(self):
        print("")
        print("Let's play thimbles together!")
        print("I've got three thimbles here. I'll hide the ball under one of them, and then I'll shuffle them.")
        print("Try to guess which of the three thimbles is the ball")
        print("")
        while True:
            it = input()
            if it.isdigit():
                it = int(it)
                if it in [1, 2, 3]:
                    random.seed()
                    ans = random.randrange(1, 4)
                    print("")
                    print("The correct answer was: " + str(ans))
                    if it == ans:
                        print("You have won, congratulations...")
                        print("")
                        self.sadness = min(10, self.sadness + 1)
                        break
                    else:
                        print("Muhahahah I am the greatest thimber player of all times!!")
                        print("")
                        self.sadness = max(0, self.sadness - 3)
                        break
                else:
                    print("")
                    print("Here are just three thimbles, silly.")
                    print("")
            else:
                print("")
                print("You need to choose a number. Try again.")
                print("")


    def reduce_hunger(self):
        self.hunger = max(0, self.hunger - 2)

    def reduce_sadness(self):
        self.sadness = max(0, self.sadness - 2)

    def death(self):
        if self.sadness > 10:
            print("")
            print("Your pet " + str(self.name) + " is leaving you.")
            print("Now it will travel around the world in search of a better life ")
            print("")
            raise Exception
        if self.hunger > 10:
            print("")
            print("Your tamagotchi starved to death.")
            print("Good night sweet prince...")
            print("")
            raise Exception