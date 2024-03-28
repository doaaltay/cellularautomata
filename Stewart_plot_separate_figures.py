#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 13:52:25 2024

@author: fionastewart
"""
import numpy as np
import matplotlib.pyplot as plt
import cellular_automata as ca

# Generating cellular automata arrays with same starting conditions and generation numbers but different rules
A = ca.automata(80, 100, 100, first_row='zeros', edges='ones')
B = ca.automata(90, 100, 100, first_row='zeros', edges='ones')

plt.plot(A)
plt.title("Rule 80")
plt.ylabel("Generations")
plt.xlabel("Cells")
plt.imshow(A)
plt.show(block=True)


plt.title("Rule 90")
plt.ylabel("Generations")
plt.xlabel("Cells")
plt.imshow(B)
plt.show(block=True)