"""
Print vs. Return in Functions
Here are two valid functions. One returns a value and one simply 
prints a value, without returning anything. Test run this code 
and experiment to understand the difference.
"""

# this prints something, but does not return anything
def show_plus_ten(num):
    print(num + 10)


# this returns something
def add_ten(num):
    return(num + 10)

'''
Default Arguments of Functions
'''
def cylinder_volume(height, radius=5):
    """This aspect of code is demonstrating Default Arguments"""
    pi = 3.14159
    return height * pi * radius ** 2

'''
Population Density Function
'''
def population_density(population, land_area):
    """This is a function for Population density
    
    INPUT
    population (int,float): This is the value of the population
    land_area (int, float): This is the value of the land_area

    OUTPUT
    answer (int, float): The  answer to this function is the 
                        dividend of population by land_area
    """
    answer = population/land_area
    return answer

# test cases for your function
test1 = population_density(10, 1)
expected_result1 = 10
print("expected result: {}, actual result: {}".format(expected_result1, test1))

test2 = population_density(864816, 121.4)
expected_result2 = 7123.6902801
print("expected result: {}, actual result: {}".format(expected_result2, test2))