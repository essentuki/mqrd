#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#!/usr/bin/env python

# Created modules
import core
import tasks
import design
import config as c

# python libraries
import os
import sys
import time

# Installed libraries via pip install
import pytimedinput
from datetime import date

def main():
#   Initialize variables with default value
    user, activities, status = '', [], []
       
#   Welcome Screen
    design.intro(0.75, c.Color.DESIGN)
    time.sleep(1.5)
    
#   Initializiation & First Screen
    os.system('clear')
    today_date = date.today().strftime("%b %d, %Y")
    print(c.Color.DESIGN)
    design.title(c.WIDTH, today_date)   
    
#   This sections deals with the loading of pending tasks.
    user,timedOut = pytimedinput.timedInput(c.Color.DESIGN 
                    + "Load yesterday's pending tasks?"
                    + " [YES = Enter (" + c.Color.ADDTASKS + "y" + c.Color.DESIGN 
                               + f") / NO = wait {c.WAITING_TIME} s] " 
                               + c.Color.NORMAL, timeout = c.WAITING_TIME)
    if timedOut:
        print(c.Color.DESIGN + "Time Expired. The program will now continue." + c.Color.NORMAL)
        time.sleep(1.5)  
        
#   The following code loads previous tasks from the previous day.
    if user.lower() == 'y':
        activities = tasks.previous_tasks(activities)

#   This part will load those pending tasks from the same day.
    activities = tasks.today_pending_tasks(activities)
    status = ['[in progress]']*len(activities)

#   CORE PROGRAM RUNS HERE
    core.task_distributor(user, activities, status)
    
#   SAVING ACTIVITIES AND STATUS. CLOSES FILE.
    tasks.closing_tasks(activities, status)
    
    print(c.Color.DESIGN + "The program will exit now.\n")
    time.sleep(1.5)
    os.system('clear')

if __name__ == '__main__':
    main()

