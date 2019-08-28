from os import system
from random import randint
from time import sleep


class Game:

    def __init__(self):
        self.colors = ['R', 'G', 'Y', 'W']
        self.buffer = [self.colors[randint(0, 3)], self.colors[randint(0, 3)]]
        self.scores = list()
        self.player = list()
        self.name = ""
        self.velocity = 0.25
        self.level = 0

        self.menu()

    def menu(self):
        system("cls")
        print("\tWelcome to Twister color game...\n")
        self.read()
        sleep(1)
        print("Please insert your name:")
        while True:
            self.name = input()
            if len(self.name) > 0 and '|' not in self.name:
                break
            else:
                print("Error, please insert again the name and don´t use this letter: '|'.")
        sleep(0.5)
        self.start()

    def read(self):
        self.scores = list()

        file = open("./data/data.txt", 'r')
        for i in file.readlines():
            self.scores.append(i.replace("\n", ''))
        self.scores.sort(reverse=True)
        aux = self.scores[0].split('|')
        print(f"The best score is: {aux[0]}.\nThe best player is: {aux[1]}\n\n")

        file.close()

    def start(self):
        vel = 1.75

        while True and self.level < 100:
            system("cls")
            if self.levelGame(vel):
                self.level += 1

                system("cls")
                print("\n\n\tCongratulations, you will pass to the next level...")
                sleep(0.7)
                if vel > (0.54 + self.velocity):
                    vel -= self.velocity
            else:
                system("cls")
                self.lose()
                break
        if self.level == 100:
            system("cls")
            print("\n\nCongratulation, you finished my game...")
            sleep(1)

    def lose(self):
        print("\n\n\tError, you lose...")
        sleep(0.3)
        print(f"{self.name}, your score is: {self.level}.")

        flag = True
        file = open("./data/data.txt", 'w')

        for i in self.scores:
            aux = i.split('|')
            if self.name == aux[1]:
                flag = False
                if self.level > int(aux[0]):
                    aux[0] = self.level
            if len(str(aux[0])) == 1:
                file.write(f"0{aux[0]}|{aux[1]}\n")
            else:
                file.write(f"{aux[0]}|{aux[1]}\n")

        file.close()

        if flag:
            file = open("./data/data.txt", 'a')
            if len(str(self.level)) == 1:
                file.write(f"0{self.level}|{self.name}\n")
            else:
                file.write(f"{self.level}|{self.name}\n")
            file.close()
        sleep(0.7)

    def levelGame(self, vel):
        self.buffer.append(self.colors[randint(0, 3)])

        for i in self.buffer:
            print("Wait for it...")
            print("Remember:\n")
            print(f"\t{i}")
            sleep(vel)
            system("cls")

        return True if self.play(self.buffer) else False

    def play(self, buffer):
        print("Enter the movements:")
        for i in buffer:
            while True:
                select = input()

                if len(select) == 1 and select.upper() == 'Y' or select.upper() == 'G' or select.upper() == 'W' or \
                        select.upper() == 'R':
                    break
                else:
                    print("Error, please insert again the last letter.")
            if select.upper() != i:
                return False

        return True


if __name__ == '__main__':
    test = Game()
