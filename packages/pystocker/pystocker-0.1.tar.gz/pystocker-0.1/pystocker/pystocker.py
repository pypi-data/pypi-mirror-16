#!/usr/bin/env python

"""
Gives general functionality of the curses application
"""

## IMPORTS ##
import curses
import curses.textpad as textpad
import ystockquote
import os
import subprocess

#user created imports
import stocks
import user_input
import permanents

## GLOBALS ##
x = 1
term_size_change = False
option_window_open = False

## FUNCTIONS ##
#initialize the curses window and return scr
def init_scr():
    
    scr = curses.initscr()

    curses.noecho()
    curses.cbreak()
    curses.curs_set(0)
    curses.halfdelay(5)
    scr.keypad(True)
    scr.clear()    

    return scr

#user scr to terminate the window and revert back to terminal
def term_scr(scr):

    curses.nocbreak()
    scr.keypad(False)
    curses.echo()
    curses.endwin()

#returns the number of columns or rows
def get_scr_dim(scr):
    return scr.getmaxyx()

#returns True if there has been a change in the window size, otherwise False
def check_term_size_change(scr, scr_dim):
    
    change = False

    if scr_dim != scr.getmaxyx():
        change = True

    return change

#opens a window that is 2/3 the size of the screen horizontally and vertically
def open_option_window(scr_dim):
    
    win = curses.newwin(int((int(scr_dim[0]) * 2 / 3)), int((int(scr_dim[1]) * 2 / 3)), int((int(scr_dim[0]) / 6) - 1), int((int(scr_dim[1]) / 6) - 1))

    return win

#creates the windows at the top, left and main segments
def open_top(scr_dim):
    
    top_scr = curses.newwin(4, scr_dim[1], 0, 0)

    return top_scr

def open_left(scr_dim):

    left_scr = curses.newwin(scr_dim[0]-5-1, 10, 5, 0)

    return left_scr

def open_main(scr_dim):

    main_scr = curses.newwin(scr_dim[0]-5-1, scr_dim[1]-10, 5, 10)

    return main_scr

def open_strip(scr_dim):

    strip_scr = curses.newwin(1, scr_dim[1], 4, 0)

    return strip_scr

def open_bottom(scr_dim):

    bottom_scr = curses.newwin(1, scr_dim[1], scr_dim[0]-1, 0)

    bottom_scr.addstr(0, 0, "[n]Add [d]Remove [h]Toggle Historical [s]Sort By [0/Esc]Exit")

    return bottom_scr

def window_colors(scr_top, scr_strip, scr_left, scr_main, scr_bottom):

    curses.start_color()

    curses.init_pair(1,curses.COLOR_WHITE,curses.COLOR_BLUE)
    curses.init_pair(2,curses.COLOR_WHITE,curses.COLOR_RED)
    curses.init_pair(3,curses.COLOR_WHITE,curses.COLOR_GREEN)
    curses.init_pair(4,curses.COLOR_WHITE,curses.COLOR_MAGENTA)

    #scr_top.bkgd(curses.color_pair(1))
    scr_strip.bkgd(curses.color_pair(1))
    #scr_left.bkgd(curses.color_pair(2))
    #scr_main.bkgd(curses.color_pair(3))
    scr_bottom.bkgd(curses.color_pair(4))

#refreshes the visible windows in order
def refresh_windows(scr_top, scr_strip, scr_left, scr_main, scr_bottom):

    scr_top.refresh()
    scr_strip.refresh()
    scr_left.refresh()
    scr_main.refresh()
    scr_bottom.refresh()


## WORKFLOW ##
scr = init_scr()
scr_dim = get_scr_dim(scr)

cursor = [0, 0, 0]
stock_data_dict = {}

move_up = False
top_point = False
lockCounter = 0

proc1 = subprocess.Popen(["python", "get_data.py"])

#main loop
while x != 48 and x != 27:

    max_stock_range = curses.LINES - 6 - 1

    stock_list = stocks.open_stock_codes()
    if max_stock_range > len(stock_list):
        max_stock_range = len(stock_list)

    if x == 261:
        cursor = user_input.cursor_right(cursor)
    elif x == 260:
        cursor = user_input.cursor_left(cursor)
    elif x == 258:
        cursor = user_input.cursor_down(cursor, max_stock_range, move_up)
        if top_point == True:
            lockCounter = 0
        top_point = False    
        move_up = False
    elif x == 259:
        if cursor[2] == 1 and top_point == True:
            lockCounter = lockCounter - 1
        move_up = True
        cursor = user_input.cursor_up(cursor, max_stock_range)
        if cursor[2] == 1:
            top_point = True
    elif x == 100 or x == 263:
        if cursor[1] > 0 and cursor[1] <= total_stock_count:
            cursor[1] = cursor[1] - 1
            cursor[2] = cursor[2] - 1
            if move_up == True:
                delete_num = cursor[1] - (max_stock_range - cursor[2]) + (max_stock_range - cursor[1] + 1)
            else:
                delete_num = cursor[1]
            stock_data_dict = stocks.delete_stock_code(stock_list[delete_num], stock_data_dict)
    elif x == 110 or x == 78:
        cursor = user_input.input_n(cursor, scr_bottom, max_stock_range, stock_list)
        stock_list = stocks.open_stock_codes()
        move_up = False
        if max_stock_range > len(stock_list):
            max_stock_range = len(stock_list)
    elif x == 104:          #historical toggle
        pass
    elif x == 115:          #sort by
        pass

    shown_stocks = [0 + cursor[1] - cursor[2], max_stock_range + cursor[1] - cursor[2]]

    term_size_change = check_term_size_change(scr, scr_dim)

    if term_size_change == True:
        term_scr(scr)
        scr = init_scr()
        scr_dim = get_scr_dim(scr)
        term_size_change == False

    scr_dim = get_scr_dim(scr)

    scr_top = open_top(scr_dim)
    scr_left = open_left(scr_dim)
    scr_main = open_main(scr_dim)
    scr_strip = open_strip(scr_dim)
    scr_bottom = open_bottom(scr_dim)

    window_colors(scr_top, scr_strip, scr_left, scr_main, scr_bottom)

    stock_list = stocks.open_stock_codes()
    
    total_stock_count = len(stock_list)
    
    stock_data_dict = stocks.get_all_data(stock_data_dict)

    counter = 0
    nCounter = counter

    stock_data = {}

    #scr_main.addstr(15, 10, str(total_stock_count))

    for stock in stock_list:
        if nCounter < cursor[1] - cursor[2] and move_up == False:
            nCounter = nCounter + 1
            lockCounter = nCounter
            continue

        if move_up == True and nCounter < lockCounter:
            nCounter = nCounter + 1
            continue

        if counter > max_stock_range - 1:
            continue
        if stock in stock_data_dict:
            data = stock_data_dict[str(stock)]
            stock_data[str(stock)] = stocks.Stock(str(stock), data)
            stocks.print_data(counter, stock_data[str(stock)], scr_left, scr_main, scr_strip, x, cursor)
            counter = counter + 1
        else:
            code_length_missing = 10 - len(stock)
            for space in range(code_length_missing):
                stock = stock + " "
            if cursor[2] == counter + 1:
                scr_left.addstr(counter, 0, str(stock), curses.A_REVERSE)
            else:
                scr_left.addstr(counter, 0, str(stock), curses.A_BLINK)
            counter = counter + 1

    perm_list = permanents.get_perm_list()

    perm_data_dict = permanents.read_perm_data()

    perm_counter = 0

    for row in perm_data_dict:
        perm_length = 0
        for perm in perm_list[perm_counter]:
            if perm in row:
                perm_length = perm_length + permanents.print_permanents(scr_top, perm, perm_counter, perm_length, row[perm])
        perm_counter = perm_counter + 1

    refresh_windows(scr_top, scr_strip, scr_left, scr_main, scr_bottom)

    curses.start_color()

    curses.init_pair(6, curses.COLOR_MAGENTA, curses.COLOR_BLACK)

    scr_top.addstr(0, 0, "pystocker v0.1 - by coffeeandscripts", curses.color_pair(6))
    #scr_top.addstr(0, 45, str(x))
    
    scr_top.refresh()

    x = scr.getch()

#terminating the window
proc1.kill()                #must kill the process that runs get_data.py
term_scr(scr)               #terminate the ncurses screen function
