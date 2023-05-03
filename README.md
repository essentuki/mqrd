![image](https://user-images.githubusercontent.com/11930196/231281450-8a6c384e-51e4-4f38-b058-915b36b9802e.png)

# MQRD v1.2

Make Your Day a Good Day! -- To-Do List program for a Terminal

Current version: 1.2

A program for those who love the terminal and the efficiency of doing everything from their keyboard.

Why MQRD? It's a funny way to shorten the expression Make Your Day. 

                  (M)-a-(KeYou)-(RD)-ay = MQRD 

Reminding ourselves that we are responsible for anything that happens on our day.


![tasks](https://user-images.githubusercontent.com/11930196/231283495-8ce85aed-c335-40e3-ac1f-49cd24b91e56.png)

Created Features:
- Add an element in automatic mode
- Edit an element
- Delete an element
- Check an element as done
- Postpone an element for next day
- Start Pomodoro with a defined time
- Pomodoro stops and produces a sound
- An additional option for daily notes
- Exit the program
- After exiting, if open again, it automatically recovers the pending day's tasks
- It is possible to recover the undone tasks of the previous day
- It creates a file, with all changes occurring during a day

INSTALLATION:

To properly run the program your system requires you to install the following python packages.

    pip install playsound pytimedinput

Download all the files. Then via the terminal situate yourself in the folder where you have the python files. From there run the mqrd.py file.

    python mqrd.py

To check log files just go to the same folder where all your files are.

HOW TO USE IT:
- It automatically adds tasks.
- One can edit/check/delete/postpone/uncheck them by only entering a character 
  e/r/d/t/p and correctly choosing the index.
- It is possible to enter into Notes mode by entering n. To exit it we enter again the n letter.
- One may start a Pomodoro by entering the symbol +
- To exit we enter x

Notes will not be saved. 
