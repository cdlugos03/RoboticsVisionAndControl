import numpy as np
import math

def rot2(theta):
    return np.array([
        [np.cos(theta), -np.sin(theta)],
        [np.sin(theta), np.cos(theta)]
    ])



# Example usage
theta = (1.5708)  # angle in radians
R = rot2(theta)
print(R)
print()

start_pos = np.array([1,0])
end_pos = R @ start_pos

print(end_pos)
