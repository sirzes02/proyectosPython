class Index:

    # Num until 255 for now...
    def __init__(self, num):
        self.list_num = (128, 64, 32, 16, 8, 4, 2, 1)
        self.list_ans = [0, 0, 0, 0, 0, 0, 0, 0]
        print(bin(num))
        print(hex(num))
        self.bin(num)
        self.hexadecimal()

    def bin(self, num):
        for i in range(len(self.list_num)):
            if num >= self.list_num[i]:
                self.list_ans[i] = 1
                num -= self.list_num[i]
                if num == 0:
                    break

        print("\n-------------------------------\nBinaries:\n")
        for i in self.list_num:
            print(i, end='\t')
        print()
        for i in self.list_ans:
            print(i, end='\t')
        print("\n-------------------------------")

    def hexadecimal(self):
        ind1, ind2 = 0, 0
        if self.list_ans[0] == 1:
            ind1 += 8
        if self.list_ans[1] == 1:
            ind1 += 4
        if self.list_ans[2] == 1:
            ind1 += 2
        if self.list_ans[3] == 1:
            ind1 += 1

        if self.list_ans[4] == 1:
            ind2 += 8
        if self.list_ans[5] == 1:
            ind2 += 4
        if self.list_ans[6] == 1:
            ind2 += 2
        if self.list_ans[7] == 1:
            ind2 += 1

        if ind1 == 10:
            ind1 = 'A'
        if ind1 == 11:
            ind1 = 'B'
        if ind1 == 12:
            ind1 = 'C'
        if ind1 == 13:
            ind1 = 'D'
        if ind1 == 14:
            ind1 = 'E'
        if ind1 == 15:
            ind1 = 'F'

        if ind2 == 10:
            ind2 = 'A'
        if ind2 == 11:
            ind2 = 'B'
        if ind2 == 12:
            ind2 = 'C'
        if ind2 == 13:
            ind2 = 'D'
        if ind2 == 14:
            ind2 = 'E'
        if ind2 == 15:
            ind2 = 'F'

        print("Hexadecimals:\n")
        for i in self.list_num:
            print(i, end='\t')
            if i == 16:
                print("|", end="\t")
        print()
        cont = 0
        for i in self.list_ans:
            print(i, end='\t')
            cont += 1
            if cont == 4:
                print("|", end="\t")
        print(f"\n\n{ind1} {ind2}\n-------------------------------")


Index(200)
