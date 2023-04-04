#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# modules
import menu
import design
import config as c

# python libraries
import os
import time

# installed libraries via pip
from datetime import datetime, timedelta, date

def Program(user = '', activities = [], status = []):
    """
    This function runs the main commands of the program.
    It creates the outer design and takes the user input to 
    determine what to do.
    
    The user input can take on different values.
    The automatic one is adding a new pending activity.
    user == 'e' it enters into EDITING mode
    user == 'd' it enters into REMOVING mode
    user == 'n' it enters into/exits from NOTES mode
    user == 'x' it exits the program
    user == 'r' it changes the STATUS to 'done'
    user == 't' it changes the STATUS to 'tomorrow'
    user == 'p' it changes the STATUS to 'in progress'
    user == '+' it starts a POMODORO
    user == '-' it allows personalization of some features
    """
    # INITIALIZE VARIABLES WITH DEFAULT VALUE
    notes = []
    notes_activated = 0
    # time variables
    timer = 0
    
    while user != 'off':
        # ++++++++++++++++++++++++++++++++++++++++
        # top design of the program starts printing here out 
        os.system('clear')
        today_date = date.today().strftime("%b %d, %Y")
        print(c.col.DESIGN)
        design.title(c.WIDTH, today_date)
        design.topMenu(c.WIDTH)
        
        # printing of tasks/notes
        if notes_activated:
            menu.printMessage(notes, notes_activated, [])
        else:
            menu.printMessage(activities, 0, status)
            
        # bottom design of the program starts printing here out 
        print(c.col.DESIGN + "||" + " "*(c.WIDTH-4) + "||")
        design.bottomMenu(c.WIDTH)
        print(c.col.NORMAL)
        
        # ++++++++++++++++++++++++++++++++++++++
        # POMODORO
        if timer:
            menu.pomodoroTimer(timer, POMODORO_TIME, c.MUSIC_PATH )
        
        # ++++++++++++++++++++++++++++++++++++++
        # AUTOMATICALLY ASKS USER FOR INPUT FOR A TASK/NOTE
        if not timer:
            if notes_activated:
                user = input(c.col.INPROGRESS + "Add your note: " + c.col.NORMAL)
            else:    
                user = input(c.col.ADDTASKS + "Add your task: " + c.col.NORMAL)
        else:
            timer = 0
            user = '[00time_passed00]'

        # IF THE USER ONLY WRITES A SINGLE LETTER THE FOLLOWING MAY HAPPEN
        # ++++++++++++++++++++++++++++++++++++++
        if user.lower() == 'e': # EDIT
            aux = menu.editTask(activities)
            if aux:
                activities = aux

        elif user.lower() == 'd': # DELETE TASK
            selected_task = menu.deleteTask(activities) 
            if selected_task >= 0:
                del activities[selected_task]
                del status[selected_task]
                
        # ++++++++++++++++++++++++++++++++++++++
        elif user.lower() == 'r': # TASK READY
            aux = menu.checkTaskAs(status, '[done]   ')
            if aux:
                status = aux
                aux = []
                    
        elif user.lower() == 't': # FOR TOMORROW
            aux = menu.checkTaskAs(status, '[tomorrow] ')
            if aux:
                status = aux
                aux = []
        
        elif user.lower() == 'p': # IN PROGRESS
            aux = menu.checkTaskAs(status, '[in progress]')
            if aux:
                status = aux
                aux = []
                
        # +++++++++++++++++++++++++++++++++++++++
        elif user.lower() == '+': #POMODORO STARTS
            POMODORO_TIME = input(c.col.DESIGN + "Amount of minutes? " + c.col.NORMAL)
            if POMODORO_TIME.isdigit():
                POMODORO_TIME = int(POMODORO_TIME)
                timer = time.time()
            else:
                print(c.col.DESIGN + "Your input seems wrong. Try again." + c.col.NORMAL)
                time.sleep(1.5)
        
        elif user == '[00time_passed00]': # WHEN A POMODORO ENDS
            time.sleep(3)
        
        # ++++++++++++++++++++++++++++++++++++++++++
        elif user.lower() == 'n': #Starts/Ends notes' screen
            if notes_activated:
                notes_activated = 0
            else:
                notes_activated = 1
        
        elif user == '-': # Starts configuration screen
            print(c.col.DESIGN + "Not available yet." + c.col.NORMAL)
            time.sleep(2)
            
        elif user.lower() == 'x': # EXIT
            user = 'off'
            print(c.col.DESIGN + "\nHave a good one!")

        else: # HERE IT AUTOMATICALLY ADDS TASKS TO A LIST WITH ITS CORRESPONDING STATUS         
            if notes_activated:
                notes.append(user)
            else:
                activities.append(user)
                status.append('[in progress]')

