from os import system
from random import randint
from time import sleep


class Principal:

    def __init__(self):
        self.words = list()
        self.attempts = 0
        self.read_words()
        self.menu()

    def read_words(self):
        file = open("./data/data.txt", "r")

        for i in file:
            self.words.append(i.replace("\n", ""))

        file.close()

    def menu(self):
        while True:
            system("cls")
            print("Welcome...\n\n")
            print("Choose any option:\n")
            print("1. Play.")
            print("2. Create.")
            print("3. Delete.")
            print("4. Exit.\n")
            print("-> ", end='')
            opc = input()

            if self.validate_numbers(opc) and 1 <= int(opc) <= 4:
                break
            self.error()
        if opc == '4':
            return
        elif opc == '1':
            self.start_game()
        elif opc == '2':
            self.create()
        else:
            self.delete()
        self.menu()

    def validate_numbers(self, opc):
        try:
            int(opc)
            return True
        except ValueError:
            return False

    def error(self):
        system("cls")
        print("\n\nAn error has occurred. Please enter the data again..")
        sleep(1)

    def start_game(self):
        aux = randint(0, len(self.words) - 1)
        cover_word = ''

        for i in self.words[aux]:
            if i == ' ':
                cover_word += "/"
            else:
                cover_word += "_"

        self.loop(aux, cover_word)

    def loop(self, aux, cover_word):
        uses = list()
        self.attempts = int(len(self.words[aux]) / 2)

        while True:
            while True:
                system("cls")
                print("Guess the phrase letter by letter:\n\n")
                self.print_word(cover_word, uses)
                print("Insert a letter:\n")
                print("-> ", end='')
                letter = input()

                if letter.isalpha() and len(letter) == 1 and letter.islower() and letter not in uses:
                    break
                self.error()
            uses.append(letter)
            if letter in self.words[aux]:
                aux_list = list(cover_word)

                for i in range(len(self.words[aux])):
                    if self.words[aux][i] == letter:
                        aux_list[i] = letter
                cover_word = ''.join(aux_list)

                if '_' not in cover_word:
                    # You win
                    self.finish(cover_word, uses, True)
                    return
            else:
                self.attempts -= 1

                if self.attempts < 0:
                    # You lose
                    self.finish(cover_word, uses, False)
                    return

    def finish(self, cover_word, uses, win):
        system("cls")
        if win:
            print("Congratulation, you win...\n\n")
            self.print_word(cover_word, uses)
        else:
            print("\n\nFail, you lose...\n\n")
        sleep(2)
        system("cls")

    def print_word(self, cover_word, uses):
        print(f"--->  ", end='')
        for i in range(len(cover_word)):
            if i == 0:
                print(cover_word[i].upper(), end='')
            elif cover_word[i - 1] == "/":
                print(cover_word[i].upper(), end='')
            else:
                print(cover_word[i], end='')
            if i < len(cover_word) - 1:
                print(" ", end='')
        print("\n\n")

        print("Used letters -> ", end='')
        if len(uses) != 0:
            for i in range(len(uses)):
                print(uses[i], end='')
                if i < len(uses) - 1:
                    print(", ", end='')
                else:
                    print(".\n")
        else:
            print("Not even one.\n")

        print(f"Number of attempts -> {self.attempts}\n")

    def create(self):
        system("cls")
        while True:
            print("Create new entries...\n\n")
            print("Please enter the number of entries you will make:\n")
            print("-> ", end='')
            amount = input()
            if self.validate_numbers(amount) and int(amount) >= 1:
                break
            self.error()

        for i in range(int(amount)):
            while True:
                print(f"\nEnter entry number {i + 1}:\n")
                print("-> ", end='')
                entry = input()
                entry += ' '
                if not entry.isalnum() and 3 <= len(entry) - 1 <= 30 and self.transform_entry(entry):
                    break
                self.error()
        self.reprint_persistence()

    def transform_entry(self, entry):
        # Transform to lowercase, remove trailing and leading spaces, divide into sections to avoid more than one
        # space together
        parts = entry.strip().lower().split()

        for i in parts:
            if not i.isalpha():
                return False
        self.words.append(' '.join(parts))
        return True

    def reprint_persistence(self):
        file = open("./data/data.txt", "w")

        for i in self.words:
            file.write(f"{i}\n")
        file.close()
        self.read_words()

    def delete(self):
        system("cls")
        while True:
            print("Delete entries...\n\n")
            for i in range(len(self.words)):
                print(f"{i + 1}. {self.words[i]}.")

            print("Choose one:\n")
            print("-> ", end='')
            opc = input()
            if self.validate_numbers(opc) and 1 <= int(opc) <= len(self.words):
                break
            self.error()
        del self.words[int(opc) - 1]
        self.reprint_persistence()


if __name__ == '__main__':
    Principal()
