"""
Created on Thu Apr 21 

@author: Anaghananda Santhoshkumar

Model version: 1
"""

'''
The following code presents the activities prescribed in the module 
GEO5003: Programming for Geographical Information Analysis to fulfil 
the requirements for Assignment 1: Online Portfolio.

The code has been split into different functions to capture each 
of the activities. 
'''

#Importing all the libraries that will be used to run this model
import random
import matplotlib.pyplot as plt
import csv
import agentframework3
import matplotlib.animation 
import sys

#Declaring global variables
environment = []
num_of_agents = 20
num_of_iterations = 10
neighbourhood = 20	
agents = []

'''
Each agent contains the x-coordinate, the y-coordinate, the value of the environment,
the total amount of food stored in each agent, and information regarding other agents
'''

# Function to create random Agents and append to a list
def build_agents():
    
        for i in range(num_of_agents):
            x= random.randint(0,299)
            y= random.randint(0,299)
            value= random.randint(0,300)
            agents.append(agentframework3.Agent(value,x,y,agents))
        return agents
    

'''        
Properties of agents such as move, eat, and share_with neighbours have been
included as methods in the 'Agent' class. 
'''

#Function to diplay environmental data
def display_data(agents):
    plt.xlim(0, 300)
    plt.ylim(0, 300)
    for i in range(num_of_agents):
        plt.scatter(agents[i].x, agents[i].y)
    plt.show()
    # The program is terminated here as matplotlib failed to plot while the program was still running   
    sys.exit() 

#Function to read environmental data from a .csv file
def read_env_data():
    
    #Open the file
    f = open('in.csv') 
    reader = csv.reader(f)
    
    #Append all the data from the csv file into a 2D array called 'environment'.
    for row in reader:	
        rowlist = []
        for value in row:				
            rowlist.append(int (value))
        environment.append(rowlist)		
		
    f.close() #close the reader
    return environment


#Function to write environmental data into a new .csv file
def write_env_data(environment):
    column_headers = ['Value', 'x', 'y']
    with open("output.csv", "w",newline='') as f:
        writer = csv.writer(f)
        writer.writerow(column_headers) # Ensure the headers: Value, x-coordinate, and y-coordinate are mentioned
        writer.writerows(environment)


#Function to convert data collected from 'int' to objects of class 'Agent'
def convert_to_Agents(environment):    
    for i in range(len(environment)):
        for j in range(len(environment[i])):
            agents.append(agentframework3.Agent(environment[i][j],i,j,agents))
    return agents


#Function to call method to move agents in the environment 
def move_agents (agents):
        #random.shuffle(agents)
        for j in range(num_of_iterations):
            for i in range(num_of_agents):
                agents[i].move()
        
        print("These are the new Agent locations")
        for i in range(num_of_agents):
            print("x=",agents[i].x,", y=",agents[i].y,", store=",agents[i].store,", value=",agents[i].value)
        return agents
    
#Function to call method for agents to eat
def eat_agents (agents):
    #random.shuffle(agents)
    for j in range(num_of_iterations):
        for i in range(num_of_agents):
            agents[i].eat()
    print("These are the new Agent values")
    for i in range(num_of_agents):
             print("x=",agents[i].x,", y=",agents[i].y,", store=",agents[i].store,", value=",agents[i].value)
    return agents

#Function to call method for agents to share with neighbours
def share(agents,neighbourhood):
    #random.shuffle(agents)
    for j in range(num_of_iterations):
     for i in range(num_of_agents):       
        agents[i].share_with_neighbours(neighbourhood) 
    print("These are the new Agent values")
    for i in range(num_of_agents):
             print("x=",agents[i].x,", y=",agents[i].y,", value=",agents[i].value,", store=",agents[i].store)
    return agents    
        
#Function to animate and display data
def animation(agents):
    fig = plt.figure(figsize=(7, 7))
    ax = fig.add_axes([0, 0, 1, 1])
    def update(frame_number):
        
        fig.clear()   

        for i in range(num_of_agents):
                if random.random() < 0.5:
                    agents[i].x  = (agents[i].x + 1) % 99 
                else:
                    agents[i].x  = (agents[i].x - 1) % 99
                
                if random.random() < 0.5:
                    agents[i].y  = (agents[i].y + 1) % 99 
                else:
                    agents[i].y  = (agents[i].y - 1) % 99 
            
       
        
        for i in range(num_of_agents):
            plt.scatter(agents[i].x,agents[i].y)
            # print(agents[i][0],agents[i][1])


    animation = matplotlib.animation.FuncAnimation(fig, update, interval=1)   
    return animation


#Function to shuffle the order of agents
def shuffle(agents):
    random.shuffle(agents)
    

while True : 

    # Menu 1 to allow the user to create agents
    print(''' 
          
          Menu
          
    [1] Create agents using the random function
    [2] Create agents using data from a .csv file
    
                ''')
    choice = int(input("Please select a suitable option: "))       


    if choice == 1:
        #Get input from user regarding how many agents to create
        num_of_agents = int(input("Please input the number of agents you would like to create: "))
        #Build the agents 
        build=build_agents()
        #Print out the x,y, and value of the agents created
        print("The following agents were created:")
        for i in range(num_of_agents):
            print("x=",build[i].x,"y=",build[i].y,"value=",build[i].value)
        break    
            
    elif choice == 2:
        build=[]
        #Read data from .csv file
        temp=read_env_data()
        #Convert the data to Agents
        temp=convert_to_Agents(temp)
        
        #Get input from user regarding how many agents to manipulate
        num_of_agents = int(input("Please input the number of agents you would like to manipulate: "))
        
        #To avoid selection of agents only near the origin, shuffle the list
        random.shuffle(temp)
        
        #Create an array of agents to manipulate 
        for i in range(num_of_agents):
            build.append(agentframework3.Agent(temp[i].value,temp[i].x,temp[i].y,temp))
        
        #Print the array of agents to manipulate 
        print("The following agents have been selected to manipulate:")
        for i in range(num_of_agents):
            print("x=",build[i].x,"y=",build[i].y,"value=",build[i].value)
        break
    
    else:
        print("Invalid choice, try again!")
        


print(" We can now manipulate the agents:")

#Menu 2 to manipulate agents

while True: 
    print(''' 
            
    [1] Move the agents around 
    [2] Have the agents nibble the environment
    [3] Have the agents share with their neighbours 
    [4] Shuffle the list of agents
    [5] Write the list of agents into a .csv file
    [6] I do not wish to manipulate. Proceed to display agents. 
                ''')


    choice = int(input('''Please select a suitable option: 
                       
                       '''))
    if choice == 1:
            move_agents (build) #Call to function
            print("The agents have been moved!")
                        
    elif choice == 2:
          eat_agents (build) #Call to function
          print("The agents have nibbled!")
                    
    elif choice == 3:
          share(build,neighbourhood) #Call to function
          print("The agents have shared!")
                    
    elif choice == 4:
        shuffle(build)#Call to function
        print("The agents have been shuffled!")
            
    elif choice == 5:
        values=[]
        
        for i in range(len(build)):
            temp=[]
            temp.append(build[i].value)
            temp.append(build[i].x)
            temp.append(build[i].y)
            values.append(temp) #Creating a 2D list of Agent coordinates and values 
        print(values)
        write_env_data(values)#Call to function
        print("The agents have been written into a .csv file!")
            
    elif choice == 6:
        break
        
    else:
        print("Invalid Option")
        

#Menu 3 will allow the user to display the data that they have created and manipulated
print(''' 

We will now plot our agents!
      
[1] Display agents
[2] Animate agents
            ''')
while True:
    choice = int(input("Please select a suitable option: "))
    if choice == 1:
            display_data(build)
            sys.exit()
            
    elif choice == 2:
          r=animation(build)
          plt.show()
          sys.exit()
    else:
        print("Invalid Option, try again")