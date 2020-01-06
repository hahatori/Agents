# Import the random module using the import statement.
import random

# Build the Agent class.
class Agent:
    
    # Define the initialization method to assign values of x and y.
    def __init__(self):      # The first argument of __init__ is always self.
        self.y = random.randint(0,99)  # Generate a random number between 0 and 99 and assign it to y.
        self.x = random.randint(0,99)  # Generate a random number between 0 and 99 and assign it to x.
        
    # Define the "move" method, use if...else statement to change x and y. 
    def move(self):
        if random.random() < 0.5:         # If the generated random number is less than 0.5,
            self.x = (self.x + 1) % 100   # execute this statement and assign result to x.
        else:                             # Otherwise, 
            self.x = (self.x - 1) % 100   # execute next statement and assign result to x.

        if random.random() < 0.5:         # If the generated random number is less than 0.5,
            self.y = (self.y + 1) % 100   # execute this statement and assign result to y.
        else:                             # Otherwise,                       
            self.y = (self.y - 1) % 100   # execute next statement and assign result to y.
       
        print("y= %s, x= %s" % (self.y, self.x))   # Test the output of random numbers.
 

# Creat the Agent object, test the output random numbers y and x.             
a = Agent()
print(a)            # Display a hexadecimal address.
print(a.y, a.x)     # Display random numbers of y and x.

# Calling move method and output numbers.
a.move()            #The output of x and y is the same as the following line.
print("y= %s, x= %s" % (a.y, a.x))



