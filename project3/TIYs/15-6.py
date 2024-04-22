from random import randint
import plotly.express as px

class Die: 
    '''A class representing a single die.'''

    def __init__(self, num_sides = 6):
        '''Assume a six-sided die'''
        self.num_sides = num_sides

    def roll(self): 
        '''Return a random value between 1 and number of sides.'''
        return randint(1, self.num_sides)


def die_visual():

    die_1 = Die(8) 
    die_2 = Die(8) 

    results = []
    for roll_num in range(1000): 
        result = die_1.roll() + die_2.roll()        
        results.append(result) 

    frequencies = []
    max_result = die_1.num_sides + die_2.num_sides
    poss_results = range(2, max_result + 1) 
    for value in poss_results: 
        frequency = results.count(value) 
        frequencies.append(frequency)

    # visualize the results 

    title = "Results of Rolling Two D8 Dice 1,000 Times"    
    labels = {'x': 'Results', 'y': 'Frequency of Result'}
    fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)
    fig.show() 

die_visual()
