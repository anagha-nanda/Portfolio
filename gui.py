'''
Created on Thu Apr 19

@author: Anaghananda Santhoshkumar

Model version: 1

"""
The following code presents the GUI activity prescribed in the module 
GEO5003: Programming for Geographical Information Analysis to fulfil 
the requirements for Assignment 1: Online Portfolio.

'''
#Import relevant libraries 

import matplotlib
matplotlib.use('TkAgg') #Setting the suitable backend

import tkinter 
import random
import matplotlib.pyplot
import matplotlib.animation 

#Declare variables 
num_of_agents = 10
num_of_iterations = 100
agents = []

#Create figure, specify size
fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])

# Make the agents. 
for i in range(num_of_agents):
    agents.append([random.randint(0,100),random.randint(0,100)])

#Funciton to update the frame number to facilitate animation
def update(frame_number):
    
    fig.clear()   

    for i in range(num_of_agents):
            if random.random() < 0.5:
                agents[i][0]  = (agents[i][0] + 1) % 99 
            else:
                agents[i][0]  = (agents[i][0] - 1) % 99
            
            if random.random() < 0.5:
                agents[i][1]  = (agents[i][1] + 1) % 99 
            else:
                agents[i][1]  = (agents[i][1] - 1) % 99 
        
   
    
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i][0],agents[i][1])
       # print(agents[i][0],agents[i][1])

#Function to run the animation
async def run():
     animation = matplotlib.animation.FuncAnimation(fig, update, interval=1)
     canvas.draw() 

# animation = matplotlib.animation.FuncAnimation(fig, update, interval=1)

# matplotlib.pyplot.show()

root = tkinter.Tk()
root.wm_title("Model") #Function to set title of GUI
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1) 

menu_bar = tkinter.Menu(root)#Function to create menu of GUI
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Run model", command= run) #Set commands in the menu

tkinter.mainloop() # Wait for interactions. 


