#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from colors import col
"""Function to print tasks and status"""
    
def print_task(task,status):
    """
    Print Task function.
    It has been considered the standard size of a terminal as (80 x 24).
    print_task(task -> string, status -> string)
    
    This functions prints a TASK and its STATUS. Each of them with a given color.
    """
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

