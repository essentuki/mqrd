#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#!/usr/bin/env python

# internal libraries
import title as t
from printing_functions import print_task
from colors import col
from core_program import core_program
from tasks import previous_tasks, today_pending_tasks, closing_tasks

# external libraries
from datetime import datetime, timedelta, date
import time
import os
import pathlib
import sys
from pytimedinput import timedInput
from playsound import playsound

#++++++++++++++++++++++++++++++++++++++
def main():
    # INITIALIZE VARIABLES WITH DEFAULT VALUE
    WIDTH = 80 #standard width (cloumns) of a terminal window
    # main variables employed through the program
    user = ''
    activities = []
    status = []
    # space formats
    s5 = '     '
    s10 = s5*2
    # time variables
    starting_point = 0
    ending_point = 0
    
# +++++++++++++++++++++++++++++++++++++++++++++    
    # Welcome Screen
    t.title()
    time.sleep(1.5)
    
    # Initializiation
    os.system('clear')
    today_date = date.today().strftime("%b %d, %Y")
    print(col.DESIGN)
    print( s10+s10+ "|||||||||||||||||||||||||||||||||||||")
    print( s10+s10+ "|||   Make Your Day a Good Day!   |||")
    print( s10+s10+ "|||           MQRD v1.1           |||")
    print( s10+s10+f"|||         {today_date}          |||")
    print( s10+s10+ "|||||||||||||||||||||||||||||||||||||")
    print( "\n")   
    
# +++++++++++++++++++++++++++++++++++++++++++++
    """
    This sections deals with the loading of pending tasks.
    """
    WAITING_TIME = 5
    user,timedOut = timedInput(col.DESIGN 
                    + "Load yesterday's pending tasks?"
                    + " [YES = Enter (" + col.ADDTASKS + "y" + col.DESIGN 
                               + f") / NO = wait {WAITING_TIME} s] " 
                               + col.NORMAL, timeout = WAITING_TIME)
    if timedOut:
        print(col.DESIGN + "Time Expired. The program will now continue." + col.NORMAL)
        time.sleep(1.5)
    
    """
    The following code loads previous tasks from the previous day.
    """
    activities = previous_tasks(user,activities)
    """
    This part will load those pending tasks from the same day.
    """
    activities = today_pending_tasks(activities)
    status = ['[in progress]']*len(activities)

# ++++++++++++++++++++++++++++++++++++++++++++++++
    """
    CORE PROGRAM RUNS HERE
    """
    core_program(user, activities, status)
# ++++++++++++++++++++++++++++++++++++++++++++++++

    """
    SAVING ACTIVITIES AND STATUS.
    CLOSES FILE.
    """
    closing_tasks(activities, status)
    
    print(col.DESIGN + "The program will exit now.\n")
    time.sleep(1.5)
    os.system('clear')

if __name__ == '__main__':
    main()

