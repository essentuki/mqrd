#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os
import time
from datetime import datetime, timedelta, date
from playsound import playsound

from colors import col
from printing_functions import print_task

def core_program(user = '', activities = [], status = []):
    """
    This function runs the main commands of the program.
    It creates the outer design and takes the user input to 
    determine what to do.
    
    The user input can take on different values.
    The automatic one is adding a new pending activity.
    user == 'e' it enters into EDITING mode
    user == 'd' it enters into REMOVING mode
    user == 'x' it exits the program
    user == 'r' it enters into CHECKING as done mode
    user == 't' it enters into POSTPONING an activity for tomorrow mode
    user == '+' it starts a POMODORO
    user == '-' it allows personalization of some features
    """
    # INITIALIZE VARIABLES WITH DEFAULT VALUE
    WIDTH = 80 #standard width (columns) of a terminal window
    # space formats
    s5 = '     '
    s10 = s5*2
    # time variables
    starting_point = 0
    ending_point = 0
    
    today_date = date.today().strftime("%b %d, %Y")
    
    while user != 'off':

        os.system('clear')
        print(col.DESIGN)
        print( s10+s10+ "|||||||||||||||||||||||||||||||||||||")
        print( s10+s10+ "|||   Make Your Day a Good Day!   |||")
        print( s10+s10+ "|||           MQRD v1.1           |||")
        print( s10+s10+f"|||         {today_date}          |||")
        print( s10+s10+ "|||||||||||||||||||||||||||||||||||||")
        print( "\n")
        print( s10+s5 + "   Add  |  Edit (e)  |  Del (d)  |  Exit (x)")
        print( "|"*WIDTH )       
        print("||" + " "*(WIDTH-4) + "||")
        if activities: 
            for i,val in enumerate(activities):
                if i+1 < 10:
                    print_task(f"[{i+1}]. {val}",status[i],0)   
                else:
                    print_task(f"[{i+1}]. {val}",status[i],1)
        else:
            complement_space = WIDTH - 2*len(s5) - len(s10+s10+"  [No pending activities]")
            print(col.DESIGN + "||   "
                 + col.ADDTASKS + s10+s10+"  [No pending activities]"
                 + ' '*complement_space  
                 + col.DESIGN + "   ||"
                 )
        print(col.DESIGN + "||" + " "*(WIDTH-4) + "||")
        print( "|"*WIDTH )
        print( s10+" Ready (r)  |  Tomorrow (t)  |  Pomodoro (+)  |  Config (-)")
        print(col.NORMAL)
        
        # POMODORO PART
        if starting_point:
            printed = 1
            filling = 0
            TIME_INTERVAL = POMODORO_TIME/5
            while time_passed < POMODORO_TIME:
                if printed:
                    print(col.POMODORO + 
                      f"Pomodoro Initialized: {POMODORO_TIME} min" 
                      + col.NORMAL
                     )
                    printed = 0
                
                if filling:
                    print(col.DESIGN + "Time passed: " + f"{time_passed} min" + col.NORMAL)
                    filling = 0
                    time.sleep(TIME_INTERVAL*60)
                         
                ending_point = time.time() 
                if (ending_point - starting_point)/60 - time_passed > TIME_INTERVAL :
                    time_passed += TIME_INTERVAL
                    filling = 1
                    
            if time_passed >= POMODORO_TIME:
                print(col.POMODORO + 'COMPLETED.' + ' Take a break.    ' + col.NORMAL)
                playsound('/usr/share/sounds/LinuxMint/stereo/dialog-warning.ogg')
        
        # AUTOMATICALLY ASKS USER FOR INPUT FOR A TASK
        if not starting_point:
            user = input(col.ADDTASKS + "Add your task: " + col.NORMAL)
        else:
            starting_point = 0
            ending_point = 0
            user = '[00time_passed00]'

        # IF THE USER ONLY WRITES A SINGLE LETTER THE FOLLOWING MAY HAPPEN
        if user.lower() == 'e': # EDIT
            selected_task = input(col.DESIGN + "Which task do you want to edit? " + col.NORMAL)
            if selected_task.isdigit():
                selected_task = int(selected_task) - 1
                if activities and selected_task < len(activities):
                    user_e = input(col.ADDTASKS + "Rewrite here: " + col.NORMAL)
                    activities[selected_task] = user_e
                else:
                    print(col.DESIGN + "Your input seems wrong. Try again." + col.NORMAL)
                    time.sleep(1.5)
            else:
                print(col.DESIGN + "Your input seems wrong. Try again." + col.NORMAL)
                time.sleep(1.5)

        elif user.lower() == 'd': # DELETE TASK
            selected_task = input(col.DESIGN + "Which task do you want to delete? " + col.NORMAL)
            if selected_task.isdigit():
                selected_task = int(selected_task) - 1
                corroborate = input(col.DESIGN 
                                    + "Sure? Yes (" 
                                    + col.ADDTASKS + "y"
                                    + col.DESIGN + ") "
                                    + col.NORMAL)
                if corroborate.lower() == 'y' and (activities and selected_task < len(activities)):
                    del activities[selected_task]
                    del status[selected_task]
                else:
                    print(col.DESIGN + "Your input seems wrong. Try again." + col.NORMAL)
                    time.sleep(1.5)
            else:
                print(col.DESIGN + "Your input seems wrong. Try again." + col.NORMAL)
                time.sleep(1.5)

        elif user.lower() == 'r': # TASK READY
            selected_task = input(col.DESIGN + "Which task did you complete? " 
                                      + col.NORMAL)
            if selected_task.isdigit():
                selected_task = int(selected_task) - 1
                if activities and selected_task < len(activities):
                    status[selected_task] = '[done]   '
                else:
                    print(col.DESIGN + "Your input seems wrong. Try again." + col.NORMAL)
                    time.sleep(1.5)
            else:
                print(col.DESIGN + "Your input seems wrong. Try again." + col.NORMAL)
                time.sleep(1.5)
                    
        elif user.lower() == 't': # FOR TOMORROW
            selected_task = input(col.DESIGN 
                                      + "Which task do you want to postpone? " 
                                      + col.NORMAL)
            if selected_task.isdigit():
                selected_task = int(selected_task) - 1
                if activities and selected_task < len(activities):
                    status[selected_task] = '[tomorrow] '
                else:
                    print(col.DESIGN + "Your input seems wrong. Try again." + col.NORMAL)
                    time.sleep(1.5)
            else:
                print(col.DESIGN + "Your input seems wrong. Try again." + col.NORMAL)
                time.sleep(1.5)
            
        elif user.lower() == '+': #POMODORO STARTS
            POMODORO_TIME = input(col.DESIGN + "Amount of minutes? " + col.NORMAL)
            if POMODORO_TIME.isdigit():
                POMODORO_TIME = int(POMODORO_TIME)
                starting_point = time.time()
                time_passed = 0
            else:
                print(col.DESIGN + "Your input seems wrong. Try again." + col.NORMAL)
                time.sleep(1.5)
        
        elif user == '[00time_passed00]': # WHEN A POMODORO ENDS
            time.sleep(3)
        
        elif user == '-':
            print(col.DESIGN + "Not available yet." + col.NORMAL)
            time.sleep(2)
            
        elif user.lower() == 'x': # EXIT
            user = 'off'
            print(col.DESIGN + "\nHave a good one!")

        else: # HERE IT AUTOMATICALLY ADDS TASKS TO A LIST WITH ITS CORRESPONDING STATUS         
            activities.append(user)
            status.append('[in progress]')

