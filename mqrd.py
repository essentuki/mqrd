#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#!/usr/bin/env python

# modules
import core
import tasks
import design
import config as c

# python libraries
import os
import sys
import time

# installed libraries via pip install
import pytimedinput
from datetime import date

#++++++++++++++++++++++++++++++++++++++
def main():
    # INITIALIZE VARIABLES WITH DEFAULT VALUE
    user = ''
    activities = []
    status = []
    
# +++++++++++++++++++++++++++++++++++++++++++++    
    # Welcome Screen
    design.intro(0.75, c.col.DESIGN)
    time.sleep(1.5)
    
    # Initializiation & First Screen
    # User will be asked about previous pending tasks
    os.system('clear')
    today_date = date.today().strftime("%b %d, %Y")
    print(c.col.DESIGN)
    design.title(c.WIDTH, today_date)   
    
# +++++++++++++++++++++++++++++++++++++++++++++
    """
    This sections deals with the loading of pending tasks.
    """
    user,timedOut = pytimedinput.timedInput(c.col.DESIGN 
                    + "Load yesterday's pending tasks?"
                    + " [YES = Enter (" + c.col.ADDTASKS + "y" + c.col.DESIGN 
                               + f") / NO = wait {c.WAITING_TIME} s] " 
                               + c.col.NORMAL, timeout = c.WAITING_TIME)
    if timedOut:
        print(c.col.DESIGN + "Time Expired. The program will now continue." + c.col.NORMAL)
        time.sleep(1.5)
    
    """
    The following code loads previous tasks from the previous day.
    """
    if user.lower() == 'y':
        activities = tasks.previousTasks(user, activities)
    """
    This part will load those pending tasks from the same day.
    """
    activities = tasks.todayPendingTasks(activities)
    status = ['[in progress]']*len(activities)

# ++++++++++++++++++++++++++++++++++++++++++++++++
    """
    CORE PROGRAM RUNS HERE
    """
    core.Program(user, activities, status)
# ++++++++++++++++++++++++++++++++++++++++++++++++

    """
    SAVING ACTIVITIES AND STATUS.
    CLOSES FILE.
    """
    tasks.closingTasks(activities, status)
    
    print(c.col.DESIGN + "The program will exit now.\n")
    time.sleep(1.5)
    os.system('clear')

if __name__ == '__main__':
    main()

