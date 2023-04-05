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
    
    The user input can take on diffecorent values.
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
        print(c.Color.DESIGN)
        design.title(c.WIDTH, today_date)
        design.topMenu(c.WIDTH)
        
        # printing of tasks/notes
        if notes_activated:
            menu.printMessage(notes, notes_activated, [])
        else:
            menu.printMessage(activities, 0, status)
            
        # bottom design of the program starts printing here out 
        print(c.Color.DESIGN + "||" + " "*(c.WIDTH-4) + "||")
        design.bottomMenu(c.WIDTH)
        print(c.Color.NORMAL)
        
        # ++++++++++++++++++++++++++++++++++++++
        # POMODORO
        if timer:
            menu.pomodoroTimer(timer, POMODORO_TIME, c.MUSIC_TRACK )
        
        # ++++++++++++++++++++++++++++++++++++++
        # AUTOMATICALLY ASKS USER FOR INPUT FOR A TASK/NOTE
        if not timer:
            if notes_activated:
                user = input(c.Color.INPROGRESS + "Add your note: " + c.Color.NORMAL)
            else:    
                user = input(c.Color.ADDTASKS + "Add your task: " + c.Color.NORMAL)
        else:
            timer = 0
            user = '[00time_passed00]'

        # IF THE USER ONLY WRITES A SINGLE LETTER THE FOLLOWING MAY HAPPEN
        # ++++++++++++++++++++++++++++++++++++++
        if user.lower() == 'e': # EDIT
            if notes_activated:
                aux = menu.editTask(notes)
                if aux:
                    activities = aux
            else:
                aux = menu.editTask(activities)
                if aux:
                    activities = aux

        elif user.lower() == 'd': # DELETE TASK
            if notes_activated:
                selected_task = menu.deleteTask(notes) 
                if selected_task >= 0:
                    del notes[selected_task]
            else:
                selected_task = menu.deleteTask(activities) 
                if selected_task >= 0:
                    del activities[selected_task]
                    del status[selected_task]
                
        # ++++++++++++++++++++++++++++++++++++++
        elif user.lower() == 'r' and not notes_activated: # TASK READY
            aux = menu.checkTaskAs(status, '[done]   ')
            if aux:
                status = aux
                aux = []
                    
        elif user.lower() == 't' and not notes_activated: # FOR TOMORROW
            aux = menu.checkTaskAs(status, '[tomorrow] ')
            if aux:
                status = aux
                aux = []
        
        elif user.lower() == 'p' and not notes_activated: # IN PROGRESS
            aux = menu.checkTaskAs(status, '[in progress]')
            if aux:
                status = aux
                aux = []
                
        # +++++++++++++++++++++++++++++++++++++++
        elif user.lower() == '+': #POMODORO STARTS
            POMODORO_TIME = input(c.Color.DESIGN + "Amount of minutes? " + c.Color.NORMAL)
            if POMODORO_TIME.isdigit():
                POMODORO_TIME = int(POMODORO_TIME)
                timer = time.time()
            else:
                print(c.Color.DESIGN + "Your input seems wrong. Try again." + c.Color.NORMAL)
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
            print(c.Color.DESIGN + "Not available yet." + c.Color.NORMAL)
            time.sleep(2)
            
        elif user.lower() == 'x': # EXIT
            user = 'off'
            print(c.Color.DESIGN + "\nHave a good one!")

        else: # HERE IT AUTOMATICALLY ADDS TASKS TO A LIST WITH ITS CORRESPONDING STATUS         
            if notes_activated:
                notes.append(user)
            else:
                activities.append(user)
                status.append('[in progress]')

