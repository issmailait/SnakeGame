""" the curses module allow as to creat an manipulate a terminal
    Random used to generate random coordinate for the food """

import random , curses

    #initialize Screen return a window obj
s = curses.initscr()

    # hide mouse curses
"""(0 or False == Hiden, 1 == Visible, 2 == Very Visible)"""
curses.curs_set(0) 

    # getmaxyx ( return a tuple (x, y) for the height and width of the terminal)
sh , sw = s.getmaxyx()
    # making a window with newwin method and passing sh and sw as argument 
w = curses.newwin(sh, sw, 0, 0)
    # letting the window accept keyboard strokes (1 or True, 0 or False)
w.keypad(True)

    #refresh every 100 milesecond
refresh = 200
w.timeout(refresh)

#snake coordinates // to return an integer
snk_x = sw//4
snk_y = sh//2

#snake start with 3 parts
snake = [
    [snk_y, snk_x], 
    [snk_y, snk_x-1],
    [snk_y, snk_x-2]
    ]

#food coordinates // to return int
food = [sh//2, sw//2]

# adding the food to the window
w.addch(food[0], food[1], curses.ACS_DIAMOND)

key = curses.KEY_RIGHT


while True:
    # getch(return the key pressed
    """if no key is pressed it return -1)"""
    next_key = w.getch()
    key = key if next_key == -1 else next_key 

    #check if snake hit borders or hit himself, if so then close the game 
    if  snake[0] in snake[1: ] or snake[0][1] in [0, sw] or snake[0][0] in [0, sh] :
        curses.endwin()
        quit()



    new_head = [snake[0][0], snake[0][1]]

    if key == curses.KEY_DOWN:
        new_head[0] += 1
    if key == curses.KEY_UP:
        new_head[0] -= 1
    if key == curses.KEY_LEFT:
        new_head[1] -= 1
    if key == curses.KEY_RIGHT:
        new_head[1] += 1

    snake.insert(0, new_head)
    
    # check if snake eat food (then set food to none and generate new food "nf")
    if snake[0] == food:
        food = None
        while food == None:
            nf = [
            random.randint(1, sh-1),
            random.randint(1, sw-1)
            ]
            food = nf if nf not in snake else None
        w.addch(food[0], food[1], curses.ACS_DIAMOND)

        #increment the speed everytime snake eat food
        if refresh > 20:
            refresh -= 20 
        else: 
            refresh = refresh 
        w.timeout(refresh)
    
    else :
        tail = snake.pop()
        w.addch(tail[0], tail[1], ' ')

    w.addch(snake[0][0], snake[0][1], curses.ACS_BLOCK)
