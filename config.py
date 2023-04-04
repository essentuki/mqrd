#!/usr/bin/env python
# coding: utf-8

# In[ ]:


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
Path to sound when a pomodoro is over.
"""
MUSIC_PATH = '/usr/share/sounds/LinuxMint/stereo/dialog-warning.ogg'

"""
Original Palette of Colors
"""
class col:
    DESIGN = '\033[94m'
    INPROGRESS = '\033[96m'
    FORTOMORROW = '\033[92m'
    ADDTASKS = '\033[93m'
    POMODORO = '\033[41m'
    FILLING = '\033[44m'
    DONE = '\033[91m'
    NORMAL = '\033[0m'

