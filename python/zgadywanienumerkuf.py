import random

liczebek = random.randint(1,100)
proby = 5
zgadniencie = 0
game = True

def porownanie():
    if zgadniencie == str:
        print("zły nie liczb")
    else:
        if zgadniencie == liczebek:
            print("yes ok brawo boss")
            global game
            game = 0
        elif zgadniencie > liczebek:
            print("za duszo")
        elif zgadniencie < liczebek:
            print("za malo boss")

while game == True:
    zgadniencie = input("allah akbar: ")
    zgadniencie = zgadniencie.strip()
    if zgadniencie == str:
        print("idiot to nie liczb")
    else:
        porownanie()