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

def task_distributor(user = '', activities = [], status = []):
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
    status_dic = {
            'r': '[done]   ',
            't': '[tomorrow] ',
            'p': '[in progress]'
            }
    notes_or_tasks = {
            1 : notes,
            0 : activities,
            }
    # time variables
    timer = 0
    
    while user != 'off':
        # ++++++++++++++++++++++++++++++++++++++++
        # top design of the program starts printing here out 
        os.system('clear')
        today_date = date.today().strftime("%b %d, %Y")
        print(c.Color.DESIGN)
        design.title(c.WIDTH, today_date)
        design.top_menu(c.WIDTH)
        
        # printing of tasks/notes
        menu.print_message(notes_or_tasks[notes_activated], notes_activated, status)
            
        # bottom design of the program starts printing here out 
        print(c.Color.DESIGN + "||" + " "*(c.WIDTH-4) + "||")
        design.bottom_menu(c.WIDTH)
        print(c.Color.NORMAL)
        
        # ++++++++++++++++++++++++++++++++++++++
        # POMODORO
        if timer:
            menu.pomodoro_timer(timer, POMODORO_TIME, c.MUSIC_TRACK )
        
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
            aux = menu.edit_task(notes_or_tasks[notes_activated])
            if aux:
                activities = aux

        elif user.lower() == 'd': # DELETE TASK
            selected_task = menu.delete_task(notes_or_tasks[notes_activated])
            if selected_task != -1:
                del notes_or_tasks[notes_activated][selected_task]
                if not notes_activated:
                    del status[selected_task]
                
        # ++++++++++++++++++++++++++++++++++++++
        elif user.lower() in status_dic and not notes_activated: 
            aux = menu.check_task_as(status, status_dic[user.lower()])
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
            notes_activated = 0 if notes_activated else 1
        
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

