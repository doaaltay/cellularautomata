import numpy as np
import matplotlib.pyplot as plt

def three_ca(initial_state, rule_number, steps):
    #convert rule number 
    rule_string = np.base_repr(rule_number, base=3).zfill(27)  #  27 rules for 
    rule = np.array([int(bit) for bit in rule_string[::-1]])


    ca = np.zeros((steps, len(initial_state)), dtype=int)
    ca[0] = initial_state

    #applying rule
    for i in range(1, steps):
        for j in range(1, len(initial_state) - 1):
            neighborhood = ca[i - 1, j - 1:j + 2]  
            index = sum(3**k * v for k, v in enumerate(neighborhood))  
            ca[i, j] = rule[index]

    return ca


initial_state = np.random.randint(0, 3, 100)
rule_number = 19683  # can be any number any number  0 to (3^9 - 1)


ca = three_ca(initial_state, rule_number, 100)

plt.imshow(ca, cmap='viridis', interpolation='none')
plt.show()