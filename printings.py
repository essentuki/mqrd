#!/usr/bin/env python
# coding: utf-8

# In[16]:


import config as c

def cut_lines(s,limit):
    """
    The maximum length for a sentence is 49 characters. Beyond that amount, the code 
    tries to find a space to cut the sentence and print it in multiple lines.
    """
    list_s = []
    if len(s) <= limit:
        list_s.append(s)
        return list_s
    
    while len(s) > limit:
        for i in range(limit,-1,-1):
            if s[i] == ' ':
                if list_s:
                    list_s.append(s[:i])
                    s = '     ' + s[i+1:]
                else:
                    list_s.append(s[:i])
                    s = s[i+1:]
                break
        limit = 49
    if s:
        list_s.append('     ' + s)
    return list_s
    
def print_task(task = '', status = '', flag = 0, notes_activated = 0):
    """
    Print Task function.
    It has been considered the standard size of a terminal as (80 x 24).
    print_task(task -> string, status -> string)
    
    This functions prints a TASK and its STATUS. Each of them with a given color.
    
    flag = 0 means one digit number
    flag = 1 means two digit number
    """
    if notes_activated:
        color = c.Color.INPROGRESS
    else:
        color = c.Color.ADDTASKS
        
    multiple_lines_task = cut_lines(task,54)
    if len(multiple_lines_task) > 1:
        for idx,line in enumerate(multiple_lines_task):
            if flag == 1:
                print(c.Color.DESIGN + '||  ', end = '')
                right_separation = c.WIDTH - 9 - len(line)
                flag = 0
            else:
                print(c.Color.DESIGN + '||   ', end = '')
                right_separation = c.WIDTH - 10 - len(line)
            
            if 'done' in status:    
                print(c.Color.STRIKE + color + line + c.Color.NORMAL, end = '')
            else:
                print(color + line, end = '')
                
            if idx == 0 and status:
                right_separation -=  len(status)
                print(' '*right_separation, end = '')
                if 'progress' in status: 
                    print(c.Color.INPROGRESS + status + c.Color.DESIGN + '   ||' + c.Color.NORMAL)
                elif 'done' in status:
                    print(c.Color.DONE + status + c.Color.DESIGN + '   ||' + c.Color.NORMAL)
                else:
                    print(c.Color.FORTOMORROW + status + c.Color.DESIGN + '   ||' + c.Color.NORMAL)
            else:
                print(' '*right_separation, end = '')
                print(c.Color.DESIGN + '   ||' + c.Color.NORMAL)
    else:
        if flag == 1:
            print(c.Color.DESIGN + '||  ', end = '')
            right_separation = c.WIDTH - 9 - len(multiple_lines_task[-1]) - len(status)
            flag = 0
        else:
            print(c.Color.DESIGN + '||   ', end = '')
            right_separation = c.WIDTH - 10 - len(multiple_lines_task[-1]) - len(status)
        
        if 'done' in status:    
            print(c.Color.STRIKE + color + multiple_lines_task[-1] + c.Color.NORMAL, end = '')
        else:  
            print(color + multiple_lines_task[-1], end = '')
        
        print(' '*right_separation, end = '')
        if 'progress' in status: 
            print(c.Color.INPROGRESS + status + c.Color.DESIGN + '   ||' + c.Color.NORMAL)
        elif 'done' in status:
            print(c.Color.DONE + status + c.Color.DESIGN + '   ||' + c.Color.NORMAL)
        else:
            print(c.Color.FORTOMORROW + status + c.Color.DESIGN + '   ||' + c.Color.NORMAL)

