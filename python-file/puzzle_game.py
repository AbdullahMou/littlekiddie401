import pygame
import sys
import random
from pygame.locals import *
'''
we create this game with this tutorial (https://inventwithpython.com/pygame/chapter4.html)
'''

'''
these variables indicates the basic structure(color , size)
'''
width = 4
height_screen = 4
tile_size = 80
screen_width= 640
screen_height = 480
FPS = 30
BLANK = None


black =         (  0,   0,   0)
pink = (250, 202, 185)
BLUE =         (169, 255, 221)

background_color = pink
boxes_color = BLUE
text_color = black
border_color = black
font_size = 20

button_color = black
button_text_color = black
msg_color = black

x_margin = int((screen_width - (tile_size * width + (width- 1))) / 2)
y_margin = int((screen_height  - (tile_size * height_screen + (height_screen - 1))) / 2)

UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'

def main():
    global fbs_clock, display_surf, basic_font, reset_surf, reset_rect, new_surf, new_rect, solve_surf, solve_rect
    '''
    clock.tick() :This method should be called once per frame. It will compute how many . milliseconds have passed since the previous call.
    pygame.Surface()pygame: object for representing images to create a new image object.(we used it for squares)
    pygame.font.Font(): we used it to select the text type and size 
    reset_surf, RESET_RECT : we used it to reset the game 
    NEW_SURF, NEW_RECT: we used it to create a new round 
    SOLVE_SURF, SOLVE_RECT: we used it to solve the game 
    
    Main function : we create the buttons options (reset , new game , solve)
    '''
    pygame.init()
    fbs_clock = pygame.time.Clock()
    display_surf = pygame.display.set_mode((screen_width, screen_height ))
    pygame.display.set_caption('Puzzle Game')
    basic_font = pygame.font.Font('freesansbold.ttf', font_size)


    reset_surf,  reset_rect = makeText('Reset',    text_color,  screen_width - 120, screen_height - 90)
    new_surf,   new_rect   = makeText('New Game', text_color,  screen_width - 120, screen_height  - 60)
    solve_surf, solve_rect = makeText('Solve',    text_color,  screen_width - 120, screen_height  - 30)
    '''
    generate 50 moves randomly and assign it to (mainBoard , solutionSeq) 
    '''
    mainBoard, solutionSeq = generateNewPuzzle(50)
    '''
    to solve the game here we returned the board to the origin order of numbers .
    '''
    solved_board = getStartingBoard()
    allMoves = []
    '''
    this part check if the player solved the slide puzzle in right way 
    '''
    while True:
        slideTo = None
        msg = 'Move the tile or press arrow keys to move'
        if mainBoard == solved_board:
            msg = 'Congrats You Solved it!'

        drawBoard(mainBoard, msg)

        checkForQuit()
        '''
        here we check the moves of the user mouseclick, we will check X and Y for the user clicks ,if X,Y not NONE so
         he playing the game , If X and Y = NONE then the user click on one of the options button (new game,reset,solve)   
        '''
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONUP:
                spotx, spoty = getSpotClicked(mainBoard, event.pos[0], event.pos[1])

                if (spotx, spoty) == (None, None):

                    if  reset_rect.collidepoint(event.pos):
                        resetAnimation(mainBoard, allMoves)
                        allMoves = []
                    elif new_rect.collidepoint(event.pos):
                        mainBoard, solutionSeq = generateNewPuzzle(50)
                        allMoves = []
                    elif solve_rect.collidepoint(event.pos):
                        resetAnimation(mainBoard, solutionSeq + allMoves)
                        allMoves = []
                else:
                    '''
                    here we check the moves of tiles if (right , left , Up , Down) depending on the X , Y blank square 
                    '''

                    blankx, blanky = getBlankPosition(mainBoard)
                    if spotx == blankx + 1 and spoty == blanky:
                        slideTo = LEFT
                    elif spotx == blankx - 1 and spoty == blanky:
                        slideTo = RIGHT
                    elif spotx == blankx and spoty == blanky + 1:
                        slideTo = UP
                    elif spotx == blankx and spoty == blanky - 1:
                        slideTo = DOWN

            elif event.type == KEYUP:
                '''
                here we check the moves of arrows and determined where is the blank square to let the appropriate 
                tile to move. we give the ability of the (WASD) arrows to move the tiles also. 
                '''
                if event.key in (K_LEFT, K_a) and isValidMove(mainBoard, LEFT):
                    slideTo = LEFT
                elif event.key in (K_RIGHT, K_d) and isValidMove(mainBoard, RIGHT):
                    slideTo = RIGHT
                elif event.key in (K_UP, K_w) and isValidMove(mainBoard, UP):
                    slideTo = UP
                elif event.key in (K_DOWN, K_s) and isValidMove(mainBoard, DOWN):
                    slideTo = DOWN

        if slideTo:
            '''
            whatever the user used arrows or mouse we will call the slideAnimation() function to update the variables
            of the game state(MainBoard) and display the new move in the screen with this msg and speed of moving. 
            '''
            slideAnimation(mainBoard, slideTo, 'Move the tile or press arrow keys to move', 8)
            '''
            makemove() update the structure for the mainboard 
            '''
            makeMove(mainBoard, slideTo)
            '''
            allmoves[] : it's a list have the moves that the user did it. so when he reset ,it will make the undo for us 
            easier
            '''
            allMoves.append(slideTo)
        pygame.display.update()
        fbs_clock.tick(FPS)


def terminate():
    '''
     pygame.quit(): runs code that deactivates the Pygame library
    '''
    pygame.quit()
    '''
    sys.exit() function allows us to exit from Python
    '''
    sys.exit()


def checkForQuit():
    for event in pygame.event.get(QUIT): # getq all the QUIT events
        terminate() # terminate if any QUIT events are present
    for event in pygame.event.get(KEYUP): # get all the KEYUP events
        if event.key == K_ESCAPE:
            terminate() # terminate if the KEYUP event was for the Esc key
        pygame.event.post(event) # put the other KEYUP event objects back


def getStartingBoard():
    # Return a board data structure with tiles in the solved state.
    # For example, if width and height_screen are both 3, this function
    # returns [[1, 4, 7], [2, 5, 8], [3, 6, BLANK]]
    counter = 1
    board = []
    for x in range(width):
        column = []
        for y in range(height_screen):
            column.append(counter)
            counter += width
        board.append(column)
        counter -= width * (height_screen - 1) + width - 1

    board[width-1][height_screen-1] = BLANK
    return board


def getBlankPosition(board):
    # Return the x and y of board coordinates of the blank space.
    for x in range(width):
        for y in range(height_screen):
            if board[x][y] == BLANK:
                return (x, y)


def makeMove(board, move):
    # This function does not check if the move is valid.
    blankx, blanky = getBlankPosition(board)

    if move == UP:
        board[blankx][blanky], board[blankx][blanky + 1] = board[blankx][blanky + 1], board[blankx][blanky]
    elif move == DOWN:
        board[blankx][blanky], board[blankx][blanky - 1] = board[blankx][blanky - 1], board[blankx][blanky]
    elif move == LEFT:
        board[blankx][blanky], board[blankx + 1][blanky] = board[blankx + 1][blanky], board[blankx][blanky]
    elif move == RIGHT:
        board[blankx][blanky], board[blankx - 1][blanky] = board[blankx - 1][blanky], board[blankx][blanky]


def isValidMove(board, move):
    blankx, blanky = getBlankPosition(board)
    return (move == UP and blanky != len(board[0]) - 1) or \
           (move == DOWN and blanky != 0) or \
           (move == LEFT and blankx != len(board) - 1) or \
           (move == RIGHT and blankx != 0)


def getRandomMove(board, lastMove=None):
    # start with a full list of all four moves
    validMoves = [UP, DOWN, LEFT, RIGHT]

    # remove moves from the list as they are disqualified
    if lastMove == UP or not isValidMove(board, DOWN):
        validMoves.remove(DOWN)
    if lastMove == DOWN or not isValidMove(board, UP):
        validMoves.remove(UP)
    if lastMove == LEFT or not isValidMove(board, RIGHT):
        validMoves.remove(RIGHT)
    if lastMove == RIGHT or not isValidMove(board, LEFT):
        validMoves.remove(LEFT)

    # return a random move from the list of remaining moves
    return random.choice(validMoves)


def getLeftTopOfTile(tileX, tileY):
    left =x_margin + (tileX * tile_size) + (tileX - 1)
    top = y_margin + (tileY * tile_size) + (tileY - 1)
    return (left, top)


def getSpotClicked(board, x, y):
    # from the x & y pixel coordinates, get the x & y board coordinates
    for tileX in range(len(board)):
        for tileY in range(len(board[0])):
            left, top = getLeftTopOfTile(tileX, tileY)
            tileRect = pygame.Rect(left, top, tile_size, tile_size)
            if tileRect.collidepoint(x, y):
                return (tileX, tileY)
    return (None, None)


def drawTile(tilex, tiley, number, adjx=0, adjy=0):
    # draw a tile at board coordinates tilex and tiley, optionally a few
    # pixels over (determined by adjx and adjy)
    left, top = getLeftTopOfTile(tilex, tiley)
    pygame.draw.rect(display_surf, boxes_color, (left + adjx, top + adjy, tile_size, tile_size))
    textSurf = basic_font.render(str(number), True, text_color)
    textRect = textSurf.get_rect()
    textRect.center = left + int(tile_size / 2) + adjx, top + int(tile_size / 2) + adjy
    display_surf.blit(textSurf, textRect)


def makeText(text, color, top, left):
    # create the Surface and Rect objects for some text.
    textSurf = basic_font.render(text, True, color)
    textRect = textSurf.get_rect()
    textRect.topleft = (top, left)
    return (textSurf, textRect)


def drawBoard(board, message):
    display_surf.fill(background_color)
    if message:
        textSurf, textRect = makeText(message, msg_color, 5, 5)
        display_surf.blit(textSurf, textRect)

    for tilex in range(len(board)):
        for tiley in range(len(board[0])):
            if board[tilex][tiley]:
                drawTile(tilex, tiley, board[tilex][tiley])

    left, top = getLeftTopOfTile(0, 0)
    width_w = width * tile_size
    height = height_screen * tile_size
    pygame.draw.rect(display_surf, border_color, (left - 5, top - 5, width_w + 11, height + 11), 4)

    display_surf.blit(reset_surf,  reset_rect)
    display_surf.blit(new_surf, new_rect)
    display_surf.blit(solve_surf, solve_rect)


def slideAnimation(board, direction, message, animationSpeed):
    # Note: This function does not check if the move is valid.

    blankx, blanky = getBlankPosition(board)
    if direction == UP:
        movex = blankx
        movey = blanky + 1
    elif direction == DOWN:
        movex = blankx
        movey = blanky - 1
    elif direction == LEFT:
        movex = blankx + 1
        movey = blanky
    elif direction == RIGHT:
        movex = blankx - 1
        movey = blanky

    # prepare the base surface
    drawBoard(board, message)
    baseSurf = display_surf.copy()
    # draw a blank space over the moving tile on the baseSurf Surface.
    moveLeft, moveTop = getLeftTopOfTile(movex, movey)
    pygame.draw.rect(baseSurf, background_color, (moveLeft, moveTop, tile_size, tile_size))

    for i in range(0, tile_size, animationSpeed):
        # animate the tile sliding over
        checkForQuit()
        display_surf.blit(baseSurf, (0, 0))
        if direction == UP:
            drawTile(movex, movey, board[movex][movey], 0, -i)
        if direction == DOWN:
            drawTile(movex, movey, board[movex][movey], 0, i)
        if direction == LEFT:
            drawTile(movex, movey, board[movex][movey], -i, 0)
        if direction == RIGHT:
            drawTile(movex, movey, board[movex][movey], i, 0)

        pygame.display.update()
        fbs_clock.tick(FPS)


def generateNewPuzzle(numSlides):
    # From a starting configuration, make numSlides number of moves (and
    # animate these moves).
    sequence = []
    board = getStartingBoard()
    drawBoard(board, '')
    pygame.display.update()
    pygame.time.wait(500) # pause 500 milliseconds for effect
    lastMove = None
    for i in range(numSlides):
        move = getRandomMove(board, lastMove)
        slideAnimation(board, move, 'Generating new puzzle...', animationSpeed=int(tile_size / 3))
        makeMove(board, move)
        sequence.append(move)
        lastMove = move
    return (board, sequence)


def resetAnimation(board, allMoves):
    # make all of the moves in allMoves in reverse.
    revAllMoves = allMoves[:] # gets a copy of the list
    revAllMoves.reverse()

    for move in revAllMoves:
        if move == UP:
            oppositeMove = DOWN
        elif move == DOWN:
            oppositeMove = UP
        elif move == RIGHT:
            oppositeMove = LEFT
        elif move == LEFT:
            oppositeMove = RIGHT
        slideAnimation(board, oppositeMove, '', animationSpeed=int(tile_size / 2))
        makeMove(board, oppositeMove)


if __name__ == '__main__':
    main()