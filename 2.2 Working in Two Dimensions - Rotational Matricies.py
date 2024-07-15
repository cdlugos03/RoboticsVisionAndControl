#This program will show you the basics of a rotational matrix
#using python, the applications for this could determine precise 
#rotational movement of a robot with 2 dimensions of movement

import numpy as np
import math

def rot2(theta):
    return np.array([
        [np.cos(theta), -np.sin(theta)],
        [np.sin(theta), np.cos(theta)]
    ])

#USAGE
theta = (1.5708)  # angle in radians
R = rot2(theta) #pass theta to the rotational matrix
print(R)
print()

start_pos = np.array([1,0]) #multiply starting matrix by rotational matrix to determin
#final 2D position

end_pos = R @ start_pos

print(end_pos)
