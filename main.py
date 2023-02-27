#!/usr/bin/env python
# coding: utf-8

# In[63]:


import title as t

from datetime import date
import time
import os

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

t.title()
time.sleep(2.5)

user = ''
activities = []
while user != 'off':
    
    os.system('clear')
    print(bcolors.WARNING + "              Make Your Day a Good Day!")
    print("                     MQRD v0.1")
    today_date = date.today().strftime("%b %d, %Y")
    print(f"                   {today_date}")
    print("\n")
    print("    Add (a)  |  Edit (e)  |  Del (d)  |  Exit (x)")
    print("......................................................." + bcolors.ENDC)
    
    if activities:
        for i,val in enumerate(activities):
            print(bcolors.BOLD + f"   [{i}]. {val}" + bcolors.ENDC)
    else:
        print(bcolors.BOLD + "            [No pending activities]" + bcolors.ENDC )
            
    print(bcolors.WARNING + ".......................................................")
    print("Check (c)  |  Postpone (p)  |  Stats (s)  |  Print (-) " + bcolors.ENDC)
    
    user = input(bcolors.BOLD + "\nUser Input: " + bcolors.ENDC)
    
    if user.lower() == 'a'  :
        activities.append(input("Add your task: ") + bcolors.OKCYAN + '    [in progress]' + bcolors.ENDC)
        
    elif user.lower() == 'e':
        selected_task = int(input("Which task? "))
        activities[selected_task] = input("Rewrite here: ") + bcolors.OKCYAN + '    [in progress]' + bcolors.ENDC
        
    elif user.lower() == 'd':
        selected_task = int(input("Which task? "))
        corroborate = input("Sure? Yes (y) or No (n) ")
        if corroborate.lower() == 'y' :
            del activities[selected_task]
    
    elif user.lower() == 'c':
        selected_task = int(input("Which task did you complete? "))
        if selected_task < len(activities):
            activities[selected_task] = activities[selected_task].replace('[in progress]',bcolors.FAIL +'[done]'+bcolors.ENDC)
        
    elif user.lower() != 'x':
        print("Wrong input. Please write it again.")
        
    else:
        user = 'off'
        print("\nHave a good one!")
        print("The program will exit now.\n")
        time.sleep(1.5)
os.system('clear')


# In[ ]:




