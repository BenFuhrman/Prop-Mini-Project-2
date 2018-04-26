# Global variables
import math
import matplotlib.pyplot as plt
import scipy.stats as st

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

random_probs = generate(140455)

for j in range(110):
    x_5.append(simulate(5))
    x_10.append(simulate(10))
    x_30.append(simulate(30))
    x_50.append(simulate(50))
    x_100.append(simulate(100))
    x_150.append(simulate(150))
    x_250.append(simulate(250))
    x_500.append(simulate(500))


dec_pi = 4 - math.pi
two_a_squared = (1/57)*(1/57)*2
sigma = math.sqrt(dec_pi/two_a_squared)
mean_pop = 57 * math.sqrt(math.pi / 2)


def z_score(provided_value, n_value):
    numerator = provided_value - mean_pop
    denominator = sigma / math.sqrt(n_value)
    return numerator / denominator


def turn_to_z_list(provided_list, n_val):
    z_list = []
    for i in range(110):
        z_list.append(z_score(provided_list[i], n_val))
    return z_list


def list_little_z_probs(z_list):
    the_return = []
    the_return.append(z_prob_list(z_list, -1.4))
    the_return.append(z_prob_list(z_list, -1.0))
    the_return.append(z_prob_list(z_list, -0.5))
    the_return.append(z_prob_list(z_list, 0))
    the_return.append(z_prob_list(z_list, 0.5))
    the_return.append(z_prob_list(z_list, 1.0))
    the_return.append(z_prob_list(z_list, 1.4))
    return the_return


def z_prob_list(the_list, little_z):
    z_count = 0
    for j in range(110):
        if the_list[j] <= little_z:
            z_count = z_count + 1
    return z_count / 110


def get_mad(the_list):
    the_little_zs = [-1.4, -1, -0.5, 0, 0.5, 1, 1.4]
    return_list = []
    for j in range(7):
        mad = abs(the_list[j] - st.norm.cdf(the_little_zs[j]))
        return_list.append(mad)
    return max(return_list)


f_hat_5 = (list_little_z_probs(turn_to_z_list(x_5, 5)))
f_hat_10 = (list_little_z_probs(turn_to_z_list(x_10, 10)))
f_hat_30 = (list_little_z_probs(turn_to_z_list(x_30, 30)))
f_hat_50 = (list_little_z_probs(turn_to_z_list(x_50, 50)))
f_hat_100 = (list_little_z_probs(turn_to_z_list(x_100, 100)))
f_hat_150 = (list_little_z_probs(turn_to_z_list(x_150, 150)))
f_hat_250 = (list_little_z_probs(turn_to_z_list(x_250, 250)))
f_hat_500 = (list_little_z_probs(turn_to_z_list(x_500, 500)))


print(f_hat_5)
print(f_hat_10)
print(f_hat_30)
print(f_hat_50)
print(f_hat_100)
print(f_hat_150)
print(f_hat_250)
print(f_hat_500)




#print(get_mad(f_hat_5))
#print(get_mad(f_hat_10))
#print(get_mad(f_hat_30))
#print(get_mad(f_hat_50))
#print(get_mad(f_hat_100))
#print(get_mad(f_hat_150))
#print(get_mad(f_hat_250))
#print(get_mad(f_hat_500))







#count = 0
#for i in range(1, 100):
#    tmp_x = simulate(50)
#    if -10 < tmp_x - mean_pop < 10:
#        count = count + 1
#print(count / 100)






