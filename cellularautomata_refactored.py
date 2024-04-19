import sys
import numpy as np
import matplotlib.pyplot as plt


BASE=3
OFFSET=59049

def decimal_to_base3(x):
    """
    convers decimal to base 3 
    """
    n = []
    y = x + OFFSET
    while y > 0:
        n.insert(0, y % BASE)
        y //= BASE
    return n


def base3_to_int(n):
    """
    converts base 3 to integer.
    """
    return sum(n[-i] * (BASE ** (i - 1)) for i in range(1, len(n) + 1))


def automata_rule(x,triplet):
    """
    triplet should be a string of three digits
    converts it and returns the rule
    """
    n = decimal_to_base3(x)
    y = base3_to_int(triplet)
    rule = n[-y - 1]
    return rule
def automata(rule_number, time, length, first_row='zeros', edges='zeros'):
    """
    generates automata data
    """
    edge_types = {'zeros': np.zeros, 'ones': np.ones, 'twos': lambda shape: np.full(shape, 2), 'random': np.random.randint}
    row_types = {'zeros': np.zeros, 'ones': np.ones, 'twos': lambda shape: np.full(shape, 2), 'random': np.random.randint}

    try:
        data = edge_types[edges]([time, length], dtype=int)
    except KeyError:
        print("Enter 'zeros', 'ones', 'twos' or 'random'")
        sys.exit()

    try:
        data[0] = row_types[first_row](length, dtype=int)
    except KeyError:
        print("Enter 'zeros', 'ones', 'twos' or 'random'")
        sys.exit()

    for row in range(1, time - 1):
        for col in range(1, length - 1):
            triplet = [data[row - 1][col - 1], data[row - 1][col + 1]]
            data[row][col] = automata_rule(rule_number, triplet)

    return data
    def plot_automata(rulenum, time, length, first='zeros', edge='zeros'):
    """
    plot the automata - 4 rules in a 2x2 grid
    """
    fig, axs = plt.subplots(2, 2)
    for i, ax in enumerate(axs.flat):
        data = automata(rulenum + i, time, length, first_row=first, edges=edge)
        ax.axis("off")
        ax.imshow(data)
        ax.set_title(f"Rule {rulenum + i}")

def plot_multiple_rules(rulenum, x, time, length):
    """
    plot automata for x rules
    """
    for i in range(x):
        fig, axs = plt.subplots(2, 2)
        for j, (first_row, title) in enumerate(zip(['zeros', 'ones', 'twos'], ['zeros', 'ones', 'twos'])):
            data = automata(rulenum + i, time, length, first_row=first_row, edges='random')
            ax = axs.flat[j]
            ax.axis("off")
            ax.imshow(data)
            ax.set_title(f"Rule {rulenum + i} {title}")
        plt.show()

data = automata(3456, 100, 50, first_row='ones', edges='random')
plt.imshow(data)