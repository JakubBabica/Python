# Tik Tak Toe game implementation in Python

# function to print the game board
def ukaz_plochu(plocha):
    print("   |   |")
    print(" " + plocha[0] + " | " + plocha[1] + " | " + plocha[2])
    print("___|___|___")
    print("   |   |")
    print(" " + plocha[3] + " | " + plocha[4] + " | " + plocha[5])
    print("___|___|___")
    print("   |   |")
    print(" " + plocha[6] + " | " + plocha[7] + " | " + plocha[8])
    print("   |   |")

# function to check for winning combinations
def vitaz(plocha):
    # check horizontal rows
    for i in range(0, 9, 3):
        if plocha[i] == plocha[i+1] == plocha[i+2] != " ":
            return True
    
    # check vertical columns
    for i in range(0, 3):
        if plocha[i] == plocha[i+3] == plocha[i+6] != " ":
            return True
    
    # check diagonals
    if plocha[0] == plocha[4] == plocha[8] != " ":
        return True
    
    if plocha[2] == plocha[4] == plocha[6] != " ":
        return True
    
    return False

# function to check if board is full
def skontroluj_plochu(plocha):
    if " " in plocha:
        return False
    else:
        return True

# function to get player input
def tah_hraca(hrac, plocha):
    while True:
        tah = input(f"hrac {hrac}, zadaj poziciu (1-9): ")
        if tah.isdigit() and int(tah) in range(1, 10):
            tah = int(tah) - 1
            if plocha[tah] == " ":
                return tah
            else:
                print("Pozicia zabrata. Skus znova.")
        else:
            print("Zly input. Skus znova.")

# main function to play the game
def hraj_hru():
    # initialize board and players
    plocha = [" "] * 9
    hraci = ["X", "O"]
    aktualny_hrac = 0
    koniec_hry = False
    
    # loop until game is over
    while not koniec_hry:
        # print board and get player input
        ukaz_plochu(plocha)
        tah = tah_hraca(hraci[aktualny_hrac], plocha)
        
        # update board with player move
        plocha[tah] = hraci[aktualny_hrac]
        
        # check for win or tie
        if vitaz(plocha):
            ukaz_plochu(plocha)
            print(f"hrac {hraci[aktualny_hrac]} vyhral!")
            koniec_hry = True
        elif skontroluj_plochu(plocha):
            ukaz_plochu(plocha)
            print("Remiza!")
            koniec_hry = True
        
        # switch to next player
        aktualny_hrac = (aktualny_hrac + 1) % 2

# start the game
hraj_hru()
