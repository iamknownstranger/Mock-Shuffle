import numpy as np
import pandas as pd
import random
blocks=['A4-C','A3-S','A2-T'] #All the blocks
floors=['G','F','S','T'] #The floors in each block
classes=list(range(1,11)) #Class rooms in each floor
desks=['A','B','C','D','E','F'] #Desks in each class room
positions=list(range(1,11)) #Positions in each desk
all_calsses=[]
desk_positions=[]
total_sitting_positions=[]
shuffle={}
for i in blocks: #Applying cross product on blocks,floors,classes to get the list of all classes available
    for j in floors:
        for k in classes:
            all_calsses.append(i+j+str(k))
for i in desks: #Applying cross product on desks and positions in order to get the all the desk positions in each class room
    for j in positions:
        desk_positions.append(i+str(j))
for i in pos: #Applying cross product on all classes and all positions to get total sitting positions
    for j in desk_positions:
        total_sitting_positions.append(i+' '+j)
for i in range(len(total_sitting_positions)): #Generating numbers like ID numbers
    j=random.choice(total_sitting_positions) #Choosing a random position
    shuffle[j]='N07'+str(i) #Suffle was generated combinig positions and ID numbers
print(shuffle,end='\n')