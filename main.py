# Global variables
import math
import matplotlib.pyplot as plt

the_index = 0
number_of_inputs = 4
user_input = [0] * number_of_inputs
user_input_text = ['starting value', 'multiplier', 'increment', 'modulus']


def prompt(variable_name, prompt_index):
    while True:
        try:
            user_input[prompt_index] = float(input("Please enter the " + variable_name + ": "))
        except ValueError:
            print('Dummy, enter in the correct format.')
        else:
            break


#for i in range(number_of_inputs):
#    prompt(user_input_text[i], i)

# starting_value = user_input[0]
# multiplier = user_input[1]
# increment = user_input[2]
# modulus = 2**user_input[3]

starting_value = 1000
multiplier = 24693
increment = 1753
modulus = 2**17


def generate(how_many):
    pseudo_random_values_x = [starting_value] * how_many
    pseudo_random_values_u = [starting_value] * how_many
    for i in range(how_many):
        if i != 0:
            x_i = multiplier * pseudo_random_values_x[i-1] + increment
            pseudo_random_values_x[i] = x_i % modulus

    for j in range(how_many):
        pseudo_random_values_u[j] = pseudo_random_values_x[j] / modulus
    return pseudo_random_values_u


def natural_log(x):
    return math.log(x)


def get_x(p):
    return math.sqrt(-6498*natural_log(1-p))


def simulate(n):
    global the_index
    tmp = 0
    for i in range(0, n):
        tmp = tmp + get_x(random_probs[the_index])
        the_index = the_index + 1
    return tmp / n


# 1000, 24693, 1753, 17


x_5 = []
x_10 = []
x_30 = []
x_50 = []
x_100 = []
x_150 = []
x_250 = []
x_500 = []

random_probs = generate(120455)
for j in range(110):
    x_5.append(simulate(5))
    x_10.append(simulate(10))
    x_30.append(simulate(30))
    x_50.append(simulate(50))
    x_100.append(simulate(100))
    x_150.append(simulate(150))
    x_250.append(simulate(250))
    x_500.append(simulate(500))

print(x_30)
print("")
print(x_50)
print("")
print(x_100)
print("")
print(x_150)
print("")
print(x_250)
print("")
print(x_500)


