#!/usr/bin/env python
# coding: utf-8

# In[16]:


from colors import col
"""Function to print tasks and status"""
WIDTH = 80

def cutLines(s,limit):
    """
    The maximum length for a sentence is 49 characters. Beyond that amount, the code 
    tries to find where to cut the sentence and print it in various sentences.
    """
    list_s = []
    if len(s) > limit:
        while len(s) > limit:
            for i in range(limit,-1,-1):
                if s[i] == ' ':
                    if list_s:
                        list_s.append(s[:i])
                        s = '     ' + s[i+1:]
                        break
                    else:
                        list_s.append(s[:i])
                        s = s[i+1:]
                        break
            limit = 49
        if s:
            list_s.append('     ' + s)
    else:
        list_s.append(s)
    return list_s
    
def print_task(task = '', status = [], flag = 0):
    """
    Print Task function.
    It has been considered the standard size of a terminal as (80 x 24).
    print_task(task -> string, status -> string)
    
    This functions prints a TASK and its STATUS. Each of them with a given color.
    """
    multiple_lines_task = cutLines(task,54)
    if len(multiple_lines_task) > 1:
        for idx,line in enumerate(multiple_lines_task):
            if flag == 1:
                print(col.DESIGN + '||  ', end = '')
                right_separation = WIDTH - 9 - len(line)
                flag = 0
            else:
                print(col.DESIGN + '||   ', end = '')
                right_separation = WIDTH - 10 - len(line)
            print(col.ADDTASKS + line, end = '')
            if idx == len(multiple_lines_task) - 1:
                break
            print(' '*right_separation, end = '')
            print(col.DESIGN + '   ||')
    else:
        if flag == 1:
            print(col.DESIGN + '||  ', end = '')
            right_separation = WIDTH - 9 - len(multiple_lines_task[-1]) - len(status)
            flag = 0
        else:
            print(col.DESIGN + '||   ', end = '')
            right_separation = WIDTH - 10 - len(multiple_lines_task[-1]) - len(status)
        print(col.ADDTASKS + multiple_lines_task[-1], end = '')
        
    print(' '*right_separation, end = '')
    if 'progress' in status: 
        print(col.INPROGRESS + status + col.DESIGN + '   ||' + col.NORMAL)
    elif 'done' in status:
        print(col.DONE + status + col.DESIGN + '   ||' + col.NORMAL)
    else:
        print(col.FORTOMORROW + status + col.DESIGN + '   ||' + col.NORMAL)

