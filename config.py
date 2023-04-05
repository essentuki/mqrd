#!/usr/bin/env python
# coding: utf-8

# In[12]:


"""
The conventional size for a terminal window is 80 columns x 24 rows.
According to this, the WIDTH variable is assigned to 80.
"""
WIDTH = 80

"""
Waiting time when first prompt (loading previous tasks) appears.
"""
WAITING_TIME = 5

"""
Name of sound when a pomodoro is over.
"""
MUSIC_TRACK = 'mqrd_pomodoro.m4a'
 
"""
Palette of Colors
"""
no_color = '\033[0m'
white = "\033[97m"
black = "\033[30m"
red = "\033[31m"
green = "\033[32m"
yellow = "\033[33m"
blue = "\033[34m"
magenta = "\033[35m"
cyan = "\033[36m"
light_gray = "\033[37m"
dark_gray = "\033[90m"

light_red = "\033[91m"
light_green = "\033[92m"
light_yellow = "\033[93m"
light_blue = "\033[94m"
light_mangeta = "\033[95m"
light_cyan = "\033[96m"

highlighted_dark_red = "\033[41m"
highlighted_red = "\033[101m"
highlighted_green = "\033[102m"
highlighted_yellow = "\033[103m"
highlighted_blue = "\033[104m"
highlighted_magenta = "\033[105m"
highlighted_cyan = "\033[106m"

strikethrough = "\033[9m"

class Color:    
    # MQRD Palette of Colors
    DESIGN = light_blue
    INPROGRESS = light_cyan
    FORTOMORROW = light_green
    ADDTASKS = light_yellow
    POMODORO = highlighted_dark_red
    STRIKE = strikethrough
    DONE = light_red
    NORMAL = no_color   

"""
class Color:
    # Two-tones palette
    DESIGN = white
    INPROGRESS = light_gray
    FORTOMORROW = dark_gray
    ADDTASKS = light_gray
    POMODORO = dark_gray
    DONE = dark_gray
    NORMAL = no_color
"""

