#!/usr/bin/env python
# coding: utf-8

# In[8]:


# external libraries
import os
import time
import playsound

# modules
import config as c
import printings as p

def print_message(messages = [], notes_activated = 0, status = []):
    """
    Function that prints the tasks or the notes.
    """
    color_code = {
            'notes': c.Color.INPROGRESS,
            'tasks': c.Color.ADDTASKS   
                }
    s5 = '     '
    s10 = s5*2
    if messages:
        multiline = 0
        for i,val in enumerate(messages):
            if i+1 > 9:
                multiline = 1
            if notes_activated:
                p.print_task(f"[{i+1}]. {val}", '', multiline, notes_activated)
            else:
                p.print_task(f"[{i+1}]. {val}", status[i], multiline, notes_activated)   
    else:
        message = s5 + "  [Empty Notepad]" if notes_activated else "  [No pending activities]"    
        complement_space = c.WIDTH - 2*len(s5) - len(s10+s10+message)
        color = color_code['notes'] if notes_activated else color_code['tasks']
        print(c.Color.DESIGN + "||   " + color + s10+s10+message
              + ' '*complement_space  + c.Color.DESIGN + "   ||"
             )

def edit_task(activities = []):
    """
    This function edits an element of the list of tasks. It will check if 
    it exists and if it does it will return a new list.
    """
    selected_task = input(c.Color.DESIGN + "Which task do you want to edit? " + c.Color.NORMAL)
    if selected_task.isdigit():
        selected_task = int(selected_task) - 1
        if activities and selected_task < len(activities):
            user_e = input(c.Color.ADDTASKS + "Rewrite here: " + c.Color.NORMAL)
            activities[selected_task] = user_e
        else:
            print(c.Color.DESIGN + "Your input seems wrong. Try again." + c.Color.NORMAL)
            time.sleep(1.5)
            return []
    else:
        print(c.Color.DESIGN + "Your input seems wrong. Try again." + c.Color.NORMAL)
        time.sleep(1.5)
        return []
    
    return activities

def delete_task(activities = []):
    """
    This function deletes a task. It checks if the desired index exists and if it does
    it returns it so it can be later erased.
    """
    selected_task = input(c.Color.DESIGN + "Which task do you want to delete? " + c.Color.NORMAL)
    if selected_task.isdigit():
        selected_task = int(selected_task) - 1
        corroborate = input(c.Color.DESIGN 
                            + "Sure? Yes (" 
                            + c.Color.ADDTASKS + "y"
                            + c.Color.DESIGN + ") "
                            + c.Color.NORMAL)
        if corroborate.lower() == 'y' and (activities and selected_task < len(activities)):
            return selected_task
        else:
            print(c.Color.DESIGN + "Your input seems wrong. Try again." + c.Color.NORMAL)
            time.sleep(1.5)
            return -1
    else:
        print(c.Color.DESIGN + "Your input seems wrong. Try again." + c.Color.NORMAL)
        time.sleep(1.5)
        return -1

def check_task_as(status = [], phrase = ''):
    """
    This function changes the status of a task as defined by the phrase.
    The initial status is always 'in progress'. This can be modified to
    'done' or 'tomorrow'. 
    """
    selected_task = input(c.Color.DESIGN + "Which task's status do you want to change? " 
                                      + c.Color.NORMAL)
    if selected_task.isdigit():
        selected_task = int(selected_task) - 1
        if status and 0 <= selected_task < len(status):
            status[selected_task] = phrase
            return status
        else:
            print(c.Color.DESIGN + "Your input seems wrong. Try again." + c.Color.NORMAL)
            time.sleep(1.5)
            return []
    else:
        print(c.Color.DESIGN + "Your input seems wrong. Try again." + c.Color.NORMAL)
        time.sleep(1.5)
        return []

def pomodoro_timer(timer = 0, POMODORO_TIME = 50, MUSIC_TRACK = ''):
    """
    This function simulates a pomodoro timer. 
    It stops with a sound.
    """
    os.chdir('pomodoro_sounds')
    time_passed = 0
    printed = 1
    filling = 0
    TIME_INTERVAL = POMODORO_TIME/5
    while time_passed < POMODORO_TIME:
        if printed:
            print(c.Color.POMODORO + 
              f"Pomodoro Initialized: {POMODORO_TIME} min" 
              + c.Color.NORMAL
             )
            printed = 0

        if filling:
            print(c.Color.DESIGN + "Time passed: " + f"{time_passed} min" + c.Color.NORMAL)
            filling = 0
            time.sleep(TIME_INTERVAL*60)

        new_timer = time.time() 
        if (new_timer - timer)/60 - time_passed > TIME_INTERVAL :
            time_passed += TIME_INTERVAL
            filling = 1

    if time_passed >= POMODORO_TIME:
        print(c.Color.POMODORO + 'COMPLETED.' + ' Take a break.   ' + c.Color.NORMAL)
        if MUSIC_TRACK:
            playsound.playsound(MUSIC_TRACK) 
            os.chdir("..")

