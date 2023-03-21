#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#!/usr/bin/env python

# internal libraries
import title as t

# external libraries
from datetime import datetime, timedelta, date
import time
import os
import pathlib
import sys
from pytimedinput import timedInput
from playsound import playsound

# +++++++++++++++++++++++++++++++++++++
# Function to print tasks and status
    
def print_task(task,status):
    right_separation = 80 - 10 - len(task) - len(status)
    if right_separation < 0:
        print('Too many characters in the sentence.')
    else:
        print(col.DESIGN + '||   ', end = '')
        print(col.ADDTASKS + task, end = '')
        print(' '*right_separation, end = '')
        if 'progress' in status: 
            print(col.INPROGRESS + status + col.DESIGN + '   ||' + col.NORMAL)
        elif 'done' in status:
            print(col.DONE + status + col.DESIGN + '   ||' + col.NORMAL)
        else:
            print(col.FORTOMORROW + status + col.DESIGN + '   ||' + col.NORMAL)

# ++++++++++++++++++++++++++++++++++++++
#          PALETTE OF COLORS
class col:
    DESIGN = '\033[94m'
    INPROGRESS = '\033[96m'
    FORTOMORROW = '\033[92m'
    ADDTASKS = '\033[93m'
    POMODORO = '\033[41m'
    FILLING = '\033[44m'
    DONE = '\033[91m'
    NORMAL = '\033[0m'

#++++++++++++++++++++++++++++++++++++++
def main():
    # INITIALIZE VARIABLES WITH DEFAULT VALUE
    WIDTH = 80 #standard width of a terminal window
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
    
    # Welcome Screen
    t.title()
    time.sleep(1.5)
    
    # Initializiation
    os.system('clear')
    today_date = date.today().strftime("%b %d, %Y")
    print(col.DESIGN)
    print( s10+s10+ "|||||||||||||||||||||||||||||||||||||")
    print( s10+s10+ "|||   Make Your Day a Good Day!   |||")
    print( s10+s10+ "|||           MQRD v1.0           |||")
    print( s10+s10+f"|||         {today_date}          |||")
    print( s10+s10+ "|||||||||||||||||||||||||||||||||||||")
    print( "\n")   
    
    # +++++++++++++++++++++++++++++++++++++++++++++
    WAITING_TIME = 3
    user,timedOut = timedInput(col.DESIGN 
                    + "Load yesterday's pending tasks?"
                    + " [YES = Enter (" + col.ADDTASKS + "y" + col.DESIGN + ") / NO = wait 3 s] " 
                               + col.NORMAL, timeout = WAITING_TIME)
    if timedOut:
        print(col.DESIGN + "Time Expired. The program will now continue." + col.NORMAL)
        time.sleep(1.5)
        
    if user.lower() == 'y':
        yesterday = date.today()-timedelta(days=1)
        folder_name =  yesterday.strftime("%b%Y")
        try:
            # checks path's existence --> os.path.exists(folder_name)
            os.makedirs(folder_name)
        except:
            # folder already exists
            pass
        os.chdir(folder_name)
        
        file_name = yesterday.strftime("%d")
        try:
            g = open(file_name,'r')
            count_sessions = 0
            for line in g:
                if "THIS SESSION ENDED AT" in line:
                    count_sessions += 1

            omit_sessions = 0
            omit_first_two_lines = 0
            g.seek(0)
            for line in g:
                if "THIS SESSION ENDED AT" in line:
                    omit_sessions += 1

                if count_sessions == omit_sessions:
                    if omit_first_two_lines > 2:
                        if 'DONE TASKS' not in line:
                            activities.append(line.split('\n')[0])
                            status.append('[in progress]')
                        else:
                            break
                    else:
                        omit_first_two_lines += 1            
            g.close()
        except:
            print("No previous session found.")
            time.sleep(1)
            pass

        #++++++++++++++++++++++++++++++++++++++++
        os.chdir("..")
        
    
    # we define the name of the folder via the name of the month and year
    present_folder_name = date.today().strftime("%b%Y")
    # if path doesn't exist we create it
    try:
        # checks path's existence --> os.path.exists(folder_name)
        os.makedirs(present_folder_name)
    except:
        # folder already exists
        pass
    os.chdir(present_folder_name)

    # the file will be name by the number of the day within the month
    present_file_name = date.today().strftime("%d")
    try:
        f = open(present_file_name,'a+')
    except:
        pass

    #++++++++++++++++++++++++++++++++++++++++
    f.seek(0) # this is require when using append
    count_sessions = 0
    for line in f:
        if "THIS SESSION ENDED AT" in line:
            count_sessions += 1
            
    omit_sessions = 0
    omit_first_two_lines = 0
    f.seek(0)
    for line in f:
        if "THIS SESSION ENDED AT" in line:
            omit_sessions += 1

        if count_sessions == omit_sessions:
            if omit_first_two_lines >= 2:
                if 'DONE TASKS' not in line:
                    activities.append(line.split('\n')[0])
                    status.append('[in progress]')
                else:
                    break
            else:
                omit_first_two_lines += 1

# ++++++++++++++++++++++++++++++++++++++++++++++++
    
    while user != 'off':

        os.system('clear')
        print(col.DESIGN)
        print( s10+s10+ "|||||||||||||||||||||||||||||||||||||")
        print( s10+s10+ "|||   Make Your Day a Good Day!   |||")
        print( s10+s10+ "|||           MQRD v1.0           |||")
        print( s10+s10+f"|||         {today_date}          |||")
        print( s10+s10+ "|||||||||||||||||||||||||||||||||||||")
        print( "\n")
        print( s10+s5 + "   Add  |  Edit (e)  |  Del (d)  |  Exit (x)")
        print( "||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")       
        print("||" + " "*(WIDTH-4) + "||")
        if activities: 
            for i,val in enumerate(activities):
                print_task(f"[{i+1}]. {val}",status[i])       
        else:
            complement_space = WIDTH - 2*len(s5) - len(s10+s10+"  [No pending activities]")
            print(col.DESIGN + "||   "
                 + col.ADDTASKS + s10+s10+"  [No pending activities]"
                 + ' '*complement_space  
                 + col.DESIGN + "   ||"
                 )
        print(col.DESIGN + "||" + " "*(WIDTH-4) + "||")
        print( "||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
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
                print(col.POMODORO + 'COMPLETED.' + ' Take a break.   ' + col.NORMAL)
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
                    right_separation = WIDTH - 10 - len(user_e) - 1 - len('[in progress]')
                    if right_separation < 0:
                        print(col.DESIGN + 'Too many characters in the sentence.' +
                             col.NORMAL)
                    else:
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
                corroborate = input(col.DESIGN + "Sure? Yes (y) " + col.NORMAL)
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
            right_separation = WIDTH - 10 - len(user) - len('[in progress]')
            if right_separation < 0:
                print(col.DESIGN + 'Too many characters in the sentence.' + col.NORMAL)
                time.sleep(1.5)
            else:
                activities.append(user)
                status.append('[in progress]')
            
    # CLOSING STATEMENTS      
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    f.seek(0)
    f.write(f"THIS SESSION ENDED AT {current_time}. \n")
    f.write("IN PROGRESS OR FOR TOMORROW TASKS \n")
    for i,val in enumerate(activities):
        if '[done]' not in status[i]:
            f.write(val + "\n")
            
    f.write('DONE TASKS \n')
    for i,val in enumerate(activities):
        if '[done]' in status[i]:
            f.write(val + " was DONE. \n")
    f.write("END OF SESSION \n \n")

    f.close()
    print(col.DESIGN + "The program will exit now.\n")
    time.sleep(1.5)
    os.system('clear')

if __name__ == '__main__':
    main()


# In[ ]:




