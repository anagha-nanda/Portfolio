"""
Created on Thu Apr 21 

@author: Anaghananda Santhoshkumar

Model version: 1

This model describes the Agent Class and associated methods
"""


import random

class Agent:
    
    
    # The class agent is initiated using the _init_ function
        def __init__(self,value,x,y,agentss):
            self.x= x
            self.y= y
            self.value = value
            self.store = 0 # We'll come to this in a second.   
            self.agents=agentss
            
            
     # This method represents the class objects as a string     
        def _str_(self):
                return str(self)   
            
            
     # The agents will subtract value from their environment and add it to their store to simulate eating       
        def eat(self):
            if self.value > 10:
                    self.value -= 10
                    self.store += 10 
       
        
     # The agents move using this method   
        def move(self):
            #self.x= 
            if random.random() < 0.5:
                self.x = self.x+ 1 % 100
            else:
                self.x = self.x - 1 % 100

            if random.random() < 0.5:
                self.y = self.y + 1 % 100
            else:
                self.y = self.y - 1 % 100
   
      # The agents interact with other agents and share their store to average out the food they have collected   
        def share_with_neighbours(self, neighbourhood):
            for agent in self.agents:
                random.shuffle(self.agents)
                dist = self.distance_between(agent)
                if dist <= neighbourhood:
                    sum = self.store + agent.store
                    ave = sum /2
                    self.store = ave
                    agent.store = ave
      
        # This method calculates the distance between two agents       
        def distance_between(self, agent):
            return (((self.x - agent.x)**2) + ((self.y - agent.y)**2))**0.5         