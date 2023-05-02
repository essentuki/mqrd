#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os
import time
from datetime import datetime, timedelta, date

def loading_from_a_file(filename, activities = []):
    """Opens a file with a context manager. Checks for content. Returns content."""
    with open(filename,'r') as g:
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
                omit_first_two_lines += 1
                if omit_first_two_lines > 2:
                    if 'DONE TASKS' in line:
                        break
                    activities.append(line.split('\n')[0])  
    return activities

def previous_tasks(activities):
    """
    This function will try to look for a file from previous day and load any pending tasks.
    """
    yesterday = date.today() - timedelta(days=1)
    folder_name =  yesterday.strftime("%b%Y")
    try:
        os.makedirs(folder_name)
    except:
        pass
    os.chdir(folder_name)

    file_name = yesterday.strftime("%d")
    activities = loading_from_a_file(file_name, activities)

    os.chdir("..")
    return activities

def today_pending_tasks(activities = []):
    """
    This function will automatically look for a previous session within the same day.
    If there is and there are pending tasks, then those will be loaded into the screen.
    """
    # we define the name of the folder via the name of the month and year
    present_folder_name = date.today().strftime("%b%Y")
    # if path doesn't exist we create it
    try:
        os.makedirs(present_folder_name)
    except:
        # folder already exists
        pass
    os.chdir(present_folder_name)

    # the file will be name by the number of the day within the month
    present_file_name = date.today().strftime("%d")
    activities = loading_from_a_file(present_file_name, activities)
    
    os.chdir("..")
    return activities

def closing_tasks(activities = [], status = []):
    """
    This function takes the tasks with their status and separates them between
    done and pending ones.
    """
    # we define the name of the folder via the name of the month and year
    present_folder_name = date.today().strftime("%b%Y")
    # if path doesn't exist we create it
    try:
        os.makedirs(present_folder_name)
    except:
        pass
    os.chdir(present_folder_name)

    # the file will be name by the number of the day within the month
    present_file_name = date.today().strftime("%d")
    with open(present_file_name,'a+') as f:
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

