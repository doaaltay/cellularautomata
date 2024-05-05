import sys
import numpy as np
import matplotlib.pyplot as plt
import cluster_finding as cf


def dec_bin3(x):
    #convert decimal to binary base 3
    n=[]
    y=x+59049
    while (y>0):
        n.insert(0, y%3)
        y=y//3
    return n

def binb3_int(n):
    tot=0
    for i in range(1,len(n)+1):
        tot=tot+n[-i]*(3**(i-1))
    return tot

def automata_rule(x, triplet):
    # triplet should be a string of three digits
    n = dec_bin3(x)
    #convert trinary double to decimal equivalent
    y = binb3_int(triplet)
    rule = n[-y-1]
    return rule

def automata(rule_number, time, length, first_row='zeros', edges='zeros'):

    # total_length = 2 + length
    if edges =='zeros':
        data = np.zeros([time, length + 2], dtype=int)
    elif edges =='ones':
        data = np.ones([time, length + 2], dtype=int)
    elif edges =='twos':
        data = np.ones([time, length + 2], dtype=int)
        data[:,0]=2
        data[:,-1]=2
    elif edges =='random':
        data = np.random.randint(3, size=[time, length + 2], dtype=int)
    else:
        print("Enter 'zeros', 'ones' or 'random'")
        sys.exit()
    
    # initial row 
    if first_row == 'zeros':
        data[0, 1:length+1] = np.zeros(length, dtype=int)
    elif first_row =='ones':
        data[0,1:length+1] = np.ones(length, dtype =int)
    elif first_row =='twos':
        data[0,1:length+1] = 2
    elif first_row =='random':
        data[0,1:length+1] = np.random.randint(3, size=length, dtype=int)
    else:
        print("Enter 'zeros', 'ones' or 'random'")
        sys.exit()
    
    #subsequent rows
    for row in range(1, time-1):
        for col in range(1, length+1):
            triplet = []
            triplet.append(data[row-1][col-1])
            triplet.append(data[row-1][col+1])
            data[row][col] = automata_rule(rule_number, triplet)
    # cmap = plt.cm.get_cmap('summer', 2)
    # plt.imshow(data)
    # plt.colorbar()
    return data[0:time, 1:length]

def plot4rules(rulenum1,time,length, first='zeros',edge='zeros'):
    plot1=automata(rulenum1,time,length, first_row=first,edges=edge)
    plot2=automata(rulenum1+1,time,length, first_row=first,edges=edge)
    plot3=automata(rulenum1+2,time,length, first_row=first,edges=edge)
    plot4=automata(rulenum1+3,time,length, first_row=first,edges=edge)
    figure, axis = plt.subplots(2, 2)
    axis[0,0].axis("off")
    axis[0,0].imshow(plot1)
    axis[0,0].set_title("Rule " + str(rulenum1))
    axis[0,1].axis("off")
    axis[0,1].imshow(plot2)
    axis[0,1].set_title("Rule " + str(rulenum1+1))
    axis[1,0].axis("off")
    axis[1,0].imshow(plot3)
    axis[1,0].set_title("Rule "  + str(rulenum1+2))
    axis[1,1].axis("off")
    axis[1,1].imshow(plot4)
    axis[1,1].set_title("Rule " + str(rulenum1+3))
    

# Observe the different outcomes of a rule given different starting conditions
def plotXrules(rulenum1,x,time,length):
    for i in range(x):
        plot1=automata(rulenum1+i,time,length, first_row='zeros',edges='random')
        plot2=automata(rulenum1+i,time,length, first_row='ones',edges='random')
        plot3=automata(rulenum1+i,time,length, first_row='twos',edges='random')
        plot4=automata(rulenum1+i,time,length, first_row='random',edges='random')
        figure, axis = plt.subplots(2, 2)
        axis[0,0].axis("off")
        axis[0,0].imshow(plot1)
        axis[0,0].set_title("Rule " + str(rulenum1+i)+" zeros")
        axis[0,1].axis("off")
        axis[0,1].imshow(plot2)
        axis[0,1].set_title("Rule " + str(rulenum1+i)+" ones")
        axis[1,0].axis("off")
        axis[1,0].imshow(plot3)
        axis[1,0].set_title("Rule "  + str(rulenum1+i)+" twos")
        axis[1,1].axis("off")
        axis[1,1].imshow(plot4)
        axis[1,1].set_title("Rule " + str(rulenum1+i)+" random")
        # Hide last box for which we are not plotting anything
        # axis[1,1].axis("off")
        plt.show()
