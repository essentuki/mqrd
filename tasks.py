#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os
import time
from datetime import datetime, timedelta, date

def previous_tasks(user, activities = [], status = []):
    """
    This function takes user = 'y' as activation point. It will then try to look for
    a file from previous day and load those pending tasks.
    """
    if user.lower() == 'y':
        yesterday = date.today()-timedelta(days=1)
        folder_name =  yesterday.strftime("%b%Y")
        try:
            os.makedirs(folder_name)
        except:
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
                    if omit_first_two_lines >= 2:
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

def today_pending_tasks(activities = [], status = []):
    """
    This function will automatically look for a previous session within the same day.
    If there is and there are pending tasks, then those will be loaded into the screen.
    """
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
    f.seek(0) # this is require when using append. Takes pointer back to the file's origin.
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
    f.close()
    os.chdir("..")

def closing_tasks(activities = [], status = []):
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

