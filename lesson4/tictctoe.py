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

def drawBoard(board):
    

    print(board[7] +'|' + board[8] + '|' + board[9])
    print('-+-+-')
    print(board[4] +'|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[1] +'|' + board[2] + '|' + board[3])
    print('-+-+-')   

def isSpaceFree(board, move):
    return board[move] == ' '
    
def getPlayerMove(board):
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)) :
        move = input('What is your next step? (1-9) : ')
    return int(move) 

def getBotMove(board):
    pass

def main():
    while True:
        theBoard = [' '] * 10


        playerLetter, botLetter = printWelcome()

        turn = whoGoesFirst()
        print('\n' + turn + 'goes first.')

        gameIsPlaying = True

        while gameIsPlaying:
            # code for palying
            if turn == 'Player':
                drawBoard(theBoard)
                move = getPlayerMove(theBoard)
                makeMove(theBoard, playerLetter, move)


            else:
                move = getBotMove(theBoard)
                makeMove(theBoard, botLetter, move)


            if not input('Do you want to play again? (yes/no) : ').lower().startswith('y') or input().lower().startswith('Y'):
                break




if __name__ =='__main__':
    main()


