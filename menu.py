#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import time
import playsound

import config as c

def editTask(activities = []):
    """
    This function edits an element of the list of tasks. It will check if 
    it exists and if it does it will return a new list.
    """
    selected_task = input(c.col.DESIGN + "Which task do you want to edit? " + c.col.NORMAL)
    if selected_task.isdigit():
        selected_task = int(selected_task) - 1
        if activities and selected_task < len(activities):
            user_e = input(c.col.ADDTASKS + "Rewrite here: " + c.col.NORMAL)
            activities[selected_task] = user_e
        else:
            print(c.col.DESIGN + "Your input seems wrong. Try again." + c.col.NORMAL)
            time.sleep(1.5)
            return []
    else:
        print(c.col.DESIGN + "Your input seems wrong. Try again." + c.col.NORMAL)
        time.sleep(1.5)
        return []
    
    return activities

def deleteTask(activities = []):
    """
    This function deletes a task. It checks if the desired index exists and if it does
    it returns it so it can be later erased.
    """
    selected_task = input(c.col.DESIGN + "Which task do you want to delete? " + c.col.NORMAL)
    if selected_task.isdigit():
        selected_task = int(selected_task) - 1
        corroborate = input(c.col.DESIGN 
                            + "Sure? Yes (" 
                            + c.col.ADDTASKS + "y"
                            + c.col.DESIGN + ") "
                            + c.col.NORMAL)
        if corroborate.lower() == 'y' and (activities and selected_task < len(activities)):
            return selected_task
        else:
            print(c.col.DESIGN + "Your input seems wrong. Try again." + c.col.NORMAL)
            time.sleep(1.5)
            return -1
    else:
        print(c.col.DESIGN + "Your input seems wrong. Try again." + c.col.NORMAL)
        time.sleep(1.5)
        return -1

def checkTaskAs(status = [], phrase = ''):
    """
    This function changes the status of a task as defined by the phrase.
    The initial status is always 'in progress'. This can be modified to
    'done' or 'tomorrow'. 
    """
    selected_task = input(c.col.DESIGN + "Which task did you complete? " 
                                      + c.col.NORMAL)
    if selected_task.isdigit():
        selected_task = int(selected_task) - 1
        if status and selected_task < len(status):
            status[selected_task] = phrase
            return status
        else:
            print(c.col.DESIGN + "Your input seems wrong. Try again." + c.col.NORMAL)
            time.sleep(1.5)
            return []
    else:
        print(c.col.DESIGN + "Your input seems wrong. Try again." + c.col.NORMAL)
        time.sleep(1.5)
        return []

def pomodoroTimer(timer = 0, POMODORO_TIME = 50, MUSIC_PATH = ''):
    """
    This function simulates a pomodoro timer. 
    It stops with a sound.
    """
    time_passed = 0
    printed = 1
    filling = 0
    TIME_INTERVAL = POMODORO_TIME/5
    while time_passed < POMODORO_TIME:
        if printed:
            print(c.col.POMODORO + 
              f"Pomodoro Initialized: {POMODORO_TIME} min" 
              + c.col.NORMAL
             )
            printed = 0

        if filling:
            print(c.col.DESIGN + "Time passed: " + f"{time_passed} min" + c.col.NORMAL)
            filling = 0
            time.sleep(TIME_INTERVAL*60)

        new_timer = time.time() 
        if (new_timer - timer)/60 - time_passed > TIME_INTERVAL :
            time_passed += TIME_INTERVAL
            filling = 1

    if time_passed >= POMODORO_TIME:
        print(c.col.POMODORO + 'COMPLETED.' + ' Take a break.    ' + c.col.NORMAL)
        if MUSIC_PATH:
            playsound.playsound(MUSIC_PATH)

