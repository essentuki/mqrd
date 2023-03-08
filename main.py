#!/usr/bin/env python
# coding: utf-8

# In[4]:


#!/usr/bin/env python

import title as t

from datetime import date
import time
import os
import pathlib

# ++++++++++++++++++++++++++++++++++++++
def formatting(s,m,l):
    if l > len(s):
        spaces = l-len(s)
    else:
        spaces = len(s)-l
    
    spaced_text = ''
    for i in range(spaces):
        spaced_text += ' '
    return s + spaced_text + m

# ++++++++++++++++++++++++++++++++++++++
#          PALETTE OF COLORS

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

#++++++++++++++++++++++++++++++++++++++
folder_name = date.today().strftime("%b%Y")
# if path doesn't exist we create it
try:
    # checks path's existence --> os.path.exists(folder_name)
    os.makedirs(folder_name)
except:
    # folder already exists
    pass
os.chdir(folder_name)

# the file will be name by the number of the day within the month
file_name = date.today().strftime("%d")
try:
    f = open(file_name,'a+')
except:
    pass

#++++++++++++++++++++++++++++++++++++++++
t.title()
time.sleep(1.5)

length = 0
user = ''
activities = []

f.seek(0)
for line in f:
    activities.append(line.split('\n')[0][3:])

while user != 'off':
    
    os.system('clear')
    print(bcolors.OKBLUE + "          |   Make Your Day a Good Day!   |")
    print("          |          MQRD v0.4            |")
    today_date = date.today().strftime("%b %d, %Y")
    print(f"          |        {today_date}           |")
    print(f"          |||||||||||||||||||||||||||||||||")
    print("\n")
    print("    Add (a)  |  Edit (e)  |  Del (d)  |  Exit (x)")
    print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||" + bcolors.ENDC)
    #print("......................................................." + bcolors.ENDC)
    
    if activities:
        for i,val in enumerate(activities):
            print(bcolors.WARNING + f"   [{i}]. {val}" + bcolors.ENDC)
    else:
        print(bcolors.WARNING + "               [No pending activities]" + bcolors.ENDC )
            
    print(bcolors.OKBLUE + "|||||||||||||||||||||||||||||||||||||||||||||||||||||||")
    print("Check (c)  |  Postpone (p)  |  Pomodoro (+)  |  Settings (-) " + bcolors.ENDC)
    
    user = input(bcolors.ENDC + "\nUser Input: " + bcolors.ENDC)
    
    if user.lower() == 'a'  :
        user_a = input("Add your task: ")
        if length < len(user_a):
            length = len(user_a)
        user_a = formatting(user_a, bcolors.OKCYAN + '     [in progress]' + bcolors.ENDC, length)
        
        activities.append(user_a) 
        
    elif user.lower() == 'e':
        selected_task = int(input("Which task? "))
        if activities and selected_task < len(activities):
            user_e = input("Rewrite here: ")
            if length < len(user_e):
                length = len(user_e)
            user_e = formatting(user_e, bcolors.OKCYAN + '     [in progress]' + bcolors.ENDC, length)
            activities[selected_task] = user_e
            
    elif user.lower() == 'd':
        selected_task = int(input("Which task do you want to delete? "))
        corroborate = input("Sure? Yes (y) ")
        if corroborate.lower() == 'y' and (activities and selected_task < len(activities)):
            del activities[selected_task]
    
    elif user.lower() == 'c':
        selected_task = int(input("Which task did you complete? "))
        if activities and selected_task < len(activities):
            activities[selected_task] = activities[selected_task].replace('[in progress]',bcolors.FAIL +'[done]'+bcolors.ENDC)
    
    elif user.lower() == 'p':
        selected_task = int(input("Which task do you want to postpone? "))
        if activities and selected_task < len(activities):
            if 'in progress' in activities[selected_task]:
                activities[selected_task] = activities[selected_task].replace('[in progress]',bcolors.OKGREEN +'[for tomorrow]'+bcolors.ENDC)
            else:
                activities[selected_task] = activities[selected_task].replace('[done]',bcolors.OKGREEN +'[for tomorrow]'+bcolors.ENDC)
                
    elif user.lower() != 'x':
        print("Wrong input. Please write it again.")
        
    else:
        user = 'off'
        print(bcolors.OKGREEN + "\nHave a good one!")
        print(bcolors.WARNING + "The program will exit now.\n")
        time.sleep(1.5)

for i,val in enumerate(activities):
    #f.write(f"[{i}] " + val.split("\33")[0] + " " + val.split("\33")[1][4:] + "\n")
    f.write(f"[{i}] " + val + "\n")
        
f.close()
os.system('clear')


# In[ ]:




