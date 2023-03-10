#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#!/usr/bin/env python

# internal libraries
import title as t

# external libraries
from datetime import date
import time
import os
import pathlib

# ++++++++++++++++++++++++++++++++++++++
#       Function to Format Text
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

class col:
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
def main():
    # we define the name of the folder via the name of the month and year
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
    
    WIDTH = 80 #standard width of a terminal window
    length = 0
    user = ''
    activities = []

    f.seek(0) # this is require when using append
    for line in f:
        if '[in progress]' in line:
            length = max(length,len(line.split('\033')[0][4:]))
            activities.append(line.split('\n')[0][4:])
        elif 'PREVIOUS SESSION' in line:
            break
            
    f.seek(0)
    f.write('++++++ PREVIOUS SESSION ++++++ \n')
    f.seek(0)
    f.write('\n \n')
    f.seek(0)

# ++++++++++++++++++++++++++++++++++++++++++++++++
    s5 = '     '
    s10 = s5*2
    
    while user != 'off':

        os.system('clear')
        today_date = date.today().strftime("%b %d, %Y")
        print(col.OKBLUE)
        print( s10+s10+ "|||||||||||||||||||||||||||||||||||||")
        print( s10+s10+ "|||   Make Your Day a Good Day!   |||")
        print( s10+s10+ "|||          MQRD v0.6            |||")
        print( s10+s10+f"|||         {today_date}          |||")
        print( s10+s10+ "|||||||||||||||||||||||||||||||||||||")
        print( "\n")
        print( s10+s5 + "   Add  |  Edit (e)  |  Del (d)  |  Exit (x)")
        print( "||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")

        if activities:
            print("||" + " "*(WIDTH-4) + "||")
            for i,val in enumerate(activities):
                complement_space = WIDTH - 5 - 5 - len(f"[{i}]. {val}") + 9
                print(col.OKBLUE + "||   "
                 + col.WARNING + f"[{i}]. {val}"
                 + ' '*complement_space  
                 + col.OKBLUE + "   ||"
                 )
            print("||" + " "*(WIDTH-4) + "||")
            
        else:
            print("||" + " "*(WIDTH-4) + "||")
            complement_space = WIDTH - 5 - 5 - len(s10+s10+"  [No pending activities]")
            print(col.OKBLUE + "||   "
                 + col.WARNING + s10+s10+"  [No pending activities]"
                 + ' '*complement_space  
                 + col.OKBLUE + "   ||"
                 )
            print("||" + " "*(WIDTH-4) + "||")
        
        print( "||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
        print( s10+" Ready (r)  |  Tomorrow (t)  |  Pomodoro (+)  |  Config (-)")
        print(col.ENDC)
        
        user = input(col.WARNING + "Add your task: " + col.ENDC)

        if user.lower() == 'e':
            selected_task = int(input("Which task do you want to edit? "))
            if activities and selected_task < len(activities):
                user_e = input("Rewrite here: ")
                if length < len(user_e):
                    length = len(user_e)
                user_e = formatting(user_e, 
                                    col.OKCYAN + '     [in progress]' + col.ENDC, 
                                    length
                                   )
                activities[selected_task] = user_e

        elif user.lower() == 'd':
            selected_task = int(input("Which task do you want to delete? "))
            corroborate = input("Sure? Yes (y) ")
            if corroborate.lower() == 'y' and (activities and selected_task < len(activities)):
                del activities[selected_task]

        elif user.lower() == 'r':
            selected_task = int(input("Which task did you complete? "))
            if activities and selected_task < len(activities):
                if 'in progress' in activities[selected_task]:
                    activities[selected_task] = activities[selected_task].replace(
                        '[in progress]',col.FAIL +'   [done]'+ col.ENDC
                    )
                else:
                    activities[selected_task] = activities[selected_task].replace(
                        '[for tomorrow]',col.FAIL +'   [done]'+ col.ENDC
                    )
                    
        elif user.lower() == 't':
            selected_task = int(input("Which task do you want to postpone? "))
            if activities and selected_task < len(activities):
                if 'in progress' in activities[selected_task]:
                    activities[selected_task] = activities[selected_task].replace(
                        '[in progress]',col.OKGREEN +'[for tomorrow]'+ col.ENDC
                    )
                else:
                    activities[selected_task] = activities[selected_task].replace(
                        '   [done]',col.OKGREEN +'[for tomorrow]'+ col.ENDC
                    )

        elif user.lower() == 'x':
            user = 'off'
            print(col.OKGREEN + "\nHave a good one!")
            print(col.OKGREEN + "The program will exit now.\n")
            time.sleep(1.5)

        else:            
            length = max(length,len(user))
            user = formatting(user, 
                            col.OKCYAN + '     [in progress]' + col.ENDC, 
                            length
                           )
            activities.append(user) 
            
    f.seek(0)
    for i,val in enumerate(activities):
        f.write(f"[{i}] " + val + "\n")

    f.close()
    os.system('clear')

if __name__ == '__main__':
    main()

