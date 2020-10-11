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
    if random.randint(0,1) == 0:
        return ['O', 'X'] # 'Bot'
    else:
        return ['X', 'O'] # 'Player'

def choiceO():
    return ['0','X']

def choiceX():
    return['0','X']

#print(inputPlayerLetter()) # check?
def printWelcome():
    menu = """
    Welcome to 'Tic-tac-toe'
    Please, choose your character/symbol
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


#print('Player goes', choices[0])
#print('Bot goes', choice[1])


def whoGoesFirst():
    if random.randint(0,1) == 0:
        return 'Player'
    else:
        return 'Bot'


def isWinner(board, letter):
    return(
        (board[1] == letter and board[2] == letter and board[3] == letter) or
        (board[4] == letter and board[5] == letter and board[6] == letter) or
        (board[7] == letter and board[8] == letter and board[9] == letter) or
        (board[1] == letter and board[4] == letter and board[7] == letter) or
        (board[2] == letter and board[5] == letter and board[8] == letter) or
        (board[3] == letter and board[6] == letter and board[9] == letter) or
        (board[1] == letter and board[5] == letter and board[9] == letter) or
        (board[3] == letter and board[5] == letter and board[7] == letter)
    )

def makeMove(board, letter, move):
    board[move] = letter


def main():
    while True:
        theBoard = [''] * 10


        playerLetter, botLetter = printWelcome()


        gameIsPlaying = True

        while gameIsPlaying:
            # code for palying

            print('Do you want to play again?(yes/no)') 
            if not (input().lower().startswith('y')):
                break




if __name__ =='_main_':
    main()


