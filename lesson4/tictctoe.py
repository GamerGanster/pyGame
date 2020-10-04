import random

def inputPlayerLetter():
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        letter = input('Are you choosing X or O ? >').upper()


    if letter == 'X':
        return ['X', 'O']# [player, bot]
    else:
        return ['O', 'X'] # player, bot

def choiceRandom():
    if ranom.randit(0,1) == 0:
        return 'Bot'
    else:
        retun 'Player'

def choiceO():
    return ['0','X']

def choiceX():
    return['0','X']

print(inputPlayerLetter()) # check?
def printWelcome():
    menu = """
    Menu:
    1. Choice X
    2. Choice O
    3. Random
    4. input
    """
    print(menu)
    choice = 0
    while not (choice == 1 or choice == 2 or choice == 3 or choice == 4):
        choice = int(input('')) # str -> int

    if (choice == 1):
        return choiceX()
    elif (choice == 2):
        return choiceO()
    elif (choice == 3):
        return choiceRandom()
    elif (choice == 4):
        return inputPlayerLetter()
    else:
        return -1 # ERROR

choices = printWelcome()
print('Player goes', choices[0])
print('Bot goes', choice[1])