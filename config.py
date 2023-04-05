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
NO_COLOR = '\033[0m'
WHITE = "\033[97m"
BLACK = "\033[30m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
LIGHT_GRAY = "\033[37m"
DARK_GRAY = "\033[90m"

LIGHT_RED = "\033[91m"
LIGHT_GREEN = "\033[92m"
LIGHT_YELLOW = "\033[93m"
LIGHT_BLUE = "\033[94m"
LIGHT_MAGENTA = "\033[95m"
LIGHT_CYAN = "\033[96m"

HIGHLIGHTED_DARK_RED = "\033[41m"
HIGHLIGHTED_RED = "\033[101m"
HIGHLIGHTED_GREEN = "\033[102m"
HIGHLIGHTED_YELLOW = "\033[103m"
HIGHLIGHTED_BLUE = "\033[104m"
HIGHLIGHTED_MAGENTA = "\033[105m"
HIGHLIGHTED_CYAN = "\033[106m"

STRIKETHROUGH = "\033[9m"

# Color style
class Color:    
    # MQRD Palette of Colors
    DESIGN = LIGHT_BLUE
    INPROGRESS = LIGHT_CYAN
    FORTOMORROW = LIGHT_GREEN
    ADDTASKS = LIGHT_YELLOW
    POMODORO = HIGHLIGHTED_DARK_RED
    STRIKE = STRIKETHROUGH
    DONE = LIGHT_RED
    NORMAL = NO_COLOR   

"""
class Color:
    # Two-tones palette
    DESIGN = white
    INPROGRESS = LIGHT_gray
    FORTOMORROW = dark_gray
    ADDTASKS = LIGHT_gray
    POMODORO = dark_gray
    DONE = dark_gray
    NORMAL = no_color
"""

