#!/usr/bin/env python
# coding: utf-8

# In[18]:


import os
import time

def intro(TIMING_STYLE = 0.75, COLOR = '\033[94m'):
    """
    Function to display the presentation to the program when initialized.
    First variable represents the amount of transition time between M Q R D.
    Second variable represents the color of the characters.
    """ 
    os.system('clear')
    print(COLOR + """   .....     
     ............##.....##.
       ..........###...###.
         ........####.####.
           ......##.###.##.
             ....##.....##.
               ..##.....##.
                 ##.....##.
                  .........""")
    time.sleep(TIMING_STYLE)
    os.system('clear')
    print("""   .......................     
     ............##.....##..#######..
       ..........###...###.##.....##.
         ........####.####.##.....##.
           ......##.###.##.##.....##.
             ....##.....##.##..##.##.
               ..##.....##.##....##..
                 ##.....##..#####.##.
                  ...................""")
    time.sleep(TIMING_STYLE)
    os.system('clear')
    print("""   .................................    
     ............##.....##..#######..########..
       ..........###...###.##.....##.##.....##.
         ........####.####.##.....##.##.....##.
           ......##.###.##.##.....##.########..
             ....##.....##.##..##.##.##...##...
               ..##.....##.##....##..##....##..
                 ##.....##..#####.##.##.....##.
                  .............................""")
    time.sleep(TIMING_STYLE)
    os.system('clear')
    print("""   ...................................................     
     ............##.....##..#######..########..########.
       ..........###...###.##.....##.##.....##.##.....##..
         ........####.####.##.....##.##.....##.##.....##....
           ......##.###.##.##.....##.########..##.....##......
             ....##.....##.##..##.##.##...##...##.....##........
               ..##.....##.##....##..##....##..##.....##..........
                 ##.....##..#####.##.##.....##.########.............
                  ...................................................."""
         )
    time.sleep(TIMING_STYLE*1.5)
    
    print("                    .............  v1.2 - 03/24/2023   ................")
    time.sleep(0.67 * TIMING_STYLE)
    print("                      ..........         Make Your Day       ............   ")
    time.sleep(0.67 * TIMING_STYLE)
    print("                        ........           A Good Day!            .........    ")
    time.sleep(1.5)

def title(WIDTH = 80, today_date = 'Not given'):
    """
    Top screen title. In order to be correctly aligned we specify the screen's WIDTH.
    The default value is set to 80 columns.
    """
    text_on_screen = "|||||||||||||||||||||||||||||||||||||"
    left_space = WIDTH - len(text_on_screen)
    side = ' ' * int( (left_space)//2 ) # two sides
    
    print( side + "|||||||||||||||||||||||||||||||||||||" )
    print( side + "|||   Make Your Day a Good Day!   |||" )
    print( side + "|||           MQRD v1.2           |||" )
    print( side +f"|||     Today is: {today_date}    |||" )
    print( side + "|||||||||||||||||||||||||||||||||||||" )
    print( "\n" )
    
def topMenu(WIDTH = 80):
    """
    Options appearing at the top menu. In order to be correctly aligned we specify 
    the screen's WIDTH. The default value is set to 80 columns.
    """
    text_on_menu = "Edit (e)" + "|" + "Ready (r)" + "|" + "Tomorrow (t)" + "|"+ "Exit (x)"
    left_space = WIDTH - len(text_on_menu)
    sep = ' ' * round( (left_space*0.3)/6 ) # six separations in the inner menu
    side = ' ' * int( (left_space*0.7)/2 ) # two sides
    
    print( side + "Edit (e)" + sep + "|" + sep + "Ready (r)" 
          + sep + "|" + sep + "Tomorrow (t)" + sep + "|" + sep + "Exit (x)" )
    print( "|" * WIDTH ) 
    print("||" + " "*(WIDTH-4) + "||")

def bottomMenu(WIDTH = 80):
    """
    Options appearing at the bottom menu. In order to be correctly aligned we specify 
    the screen's WIDTH. The default value is set to 80 columns.
    """
    text_on_menu = "Delete (d)|Notes (n)|Pomodoro (+)|Config (-)"
    left_space = WIDTH - len(text_on_menu)
    sep = ' ' * round( (left_space*0.3)/6 ) # six separations in the inner menu
    side = ' ' * int( (left_space*0.7)/2 ) # two sides
    
    print( "|" * WIDTH ) 
    print( side + "Delete (d)" + sep + "|" + sep + "Notes (n)" 
          + sep + "|" + sep + "Pomodoro (+)" + sep + "|" + sep + "Config (-)" )

