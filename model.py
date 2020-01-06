import random                # Import the random module using the import statement.
import operator              # Import the operator package to calculate distance.
import matplotlib.pyplot     # Import the matplotlib.pyplot to plot data in graphs.
import agentframework        # Import the agentframework.py file.

# Define a function and Calculate the distance between two points. 
def distance_between(agents_row_a, agents_row_b):
    return (((agents_row_a.x - agents_row_b.x)**2) +
    ((agents_row_a.y - agents_row_b.y)**2))**0.5   

# Define arguments.
num_of_agents = 10      # Make a num_of_agents variable and assign it the value 10
num_of_iterations = 100 # Make a num_of_iterations variable and assign it the value 100
agents = []        # Creat a new empty list

# Make the agents by putting into a for-loop.
for i in range(num_of_agents):
    agents.append(agentframework.Agent()) # Creat and add agents.

# Move the agents by putting into nest for-loops.
for j in range(num_of_iterations):
    for i in range(num_of_agents):
        agents[i].move()      # Calling move method from agent.

# Set the plot attributes.        
matplotlib.pyplot.xlim(0, 99)            # Set the x-axis range from 0 to 99
matplotlib.pyplot.ylim(0, 99)            # Set the y-axis range from 0 to 99
matplotlib.pyplot.title("Scatter Plot")  # Set plot title.

# Make for-loops and show the scatter dots plot.
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
matplotlib.pyplot.show() 

# Use for-each loop iterator to put out agents.
for agents_row_a in agents:
    for agents_row_b in agents:
        distance = distance_between(agents_row_a, agents_row_b)
        


