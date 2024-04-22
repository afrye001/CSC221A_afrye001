import matplotlib.pyplot as plt
from random import choice

class RandomWalk:
    '''A class to generate random walks.'''

    def __init__(self, num_points=5000): 
        '''Initialize attributes of a walk.'''
        self.num_points = num_points 

        # All walks start at (0,0) 
        self.x_values = [0]
        self.y_values = [0]

    def get_step(self): 
        '''Determine the direction and distance for a step.'''
        direction = choice([1, -1])
        distance = choice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        step = direction * distance
        return step

    def fill_walk(self): 
        '''Calculate all points in a walk'''
        
        # Keep taking steps until desired length.
        while len(self.x_values) < self.num_points: 

            # Decide which direction to go and how far to go
            x_step = self.get_step()
            y_step = self.get_step() 

            # Reject moves that go nowhere 
            if x_step == 0 and y_step == 0:
                continue 

            # Calculate new position
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y) 

new_walk = RandomWalk() 
new_walk.fill_walk() 

plt.figure(figsize=(10, 6))
plt.plot(new_walk.x_values, new_walk.y_values, linewidth=1)

plt.scatter(0, 0, c='green', edgecolors='none', s=100)
plt.scatter(new_walk.x_values[-1], new_walk.y_values[-1], c='red', edgecolors='none', s=100)

plt.gca().get_xaxis().set_visible(False)
plt.gca().get_yaxis().set_visible(False)

plt.show()
