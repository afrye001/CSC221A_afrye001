from random import randint
import plotly.express as px

class Die: 
    '''A class representing a single die.'''

    def __init__(self, num_sides=6):
        '''Assume a six-sided die'''
        self.num_sides = num_sides

    def roll(self): 
        '''Return a random value between 1 and number of sides.'''
        return randint(1, self.num_sides)


def die_visual():

    die_1 = Die() 
    die_2 = Die() 

    results = []
    for roll_num in range(1000): 
        result = die_1.roll() * die_2.roll()        
        results.append(result) 

    max_result = die_1.num_sides * die_2.num_sides
    poss_results = range(1, max_result + 1) 

    frequencies = [results.count(value) for value in poss_results]

    # visualize the results 

    title = "Results of Multiplying Two D6 Dice 1,000 Times"    
    labels = {'x': 'Results', 'y': 'Frequency of Result'}
    fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)
    fig.show() 

die_visual()
