#!/usr/bin/env python
# coding: utf-8

# In[37]:


import config as c

def cut_lines(s = '', notes_activated = 0):
    """ The maximum length for a sentence is 49 characters. Otherwise, it splits."""
    limit = c.WIDTH - 10 if notes_activated else c.WIDTH - 10 - len('[in progress]')   
    list_s = []
    if len(s) <= limit:
        list_s.append(s)
        return list_s
    indent_off = 1
    while len(s) > limit:
        for i in range(limit,-1,-1):
            if s[i] == ' ':
                list_s.append(s[:i]) if indent_off else list_s.append('     ' + s[:i])
                s = s[i+1:]
                break
        if indent_off:
            limit -= 5
            indent_off = 0
    if s:
        list_s.append('     ' + s)
    return list_s
    
def print_task(task = '', status = '', flag = 0, notes_activated = 0):
    """ This functions prints a TASK and its STATUS. Each of them with a given color. 
        It has been considered the standard size of a terminal as (80 x 24).
        flag = 0 means one digit number, flag = 1 means two digit number          
    """
    color = c.Color.INPROGRESS if notes_activated else c.Color.ADDTASKS
    multiple_lines_task = cut_lines(task, notes_activated)
    for idx,line in enumerate(multiple_lines_task):
        print(c.Color.DESIGN + '||  ', end = '')
        right_separation = c.WIDTH - 9 - len(line)
        if flag == 0:
            print(' ', end = '')
            right_separation -= 1 
        flag = 0

        if 'done' in status:    
            print(c.Color.STRIKE + color + line + c.Color.NORMAL, end = '')
        else:
            print(color + line, end = '')
        
        if idx == 0 and status:
            right_separation -=  len(status)
            print(' '*right_separation, end = '')
            if 'progress' in status: 
                print(c.Color.INPROGRESS + status, end = '')
            elif 'done' in status:
                print(c.Color.DONE + status, end = '')
            else:
                print(c.Color.FORTOMORROW + status, end = '')
        else:
            print(' '*right_separation, end = '')
        print(c.Color.DESIGN + '   ||' + c.Color.NORMAL)

