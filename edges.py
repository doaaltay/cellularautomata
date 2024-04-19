def automata(rule_number, time, length, first_row='zeros', edges='zeros'):

    if edges =='zeros':
        data = np.zeros([time, length], dtype=int)
    elif edges =='ones':
        data = np.ones([time, length], dtype=int)
    elif edges =='twos':
        data = np.ones([time, length], dtype=int)
        data[:,0]=2
        data[:,-1]=2
    elif edges =='random':
        data = np.random.randint(3, size=[time, length], dtype=int)
    else:
        print("Enter 'zeros', 'ones' or 'random'")
        sys.exit()
    
    print(data)
    # #initial row 
    if first_row == 'zeros':
        data[0, 1:length-1] = np.zeros(length - 2, dtype=int)
    elif first_row =='ones':
        data[0,1:length-1] = np.ones(length - 2, dtype =int)
    elif first_row =='twos':
        data[0,1:length-1] = 2
    elif first_row =='random':
        data[0,1:length-1] = np.random.randint(3, size=length, dtype=int)
    else:
        print("Enter 'zeros', 'ones' or 'random'")
        sys.exit()
    print(data)
    #subsequent rows
    for row in range(1, time-1):
        for col in range(1, length-1):
            triplet = []
            triplet.append(data[row-1][col-1])
            triplet.append(data[row-1][col+1])
            data[row][col] = automata_rule(rule_number, triplet)
    # cmap = plt.cm.get_cmap('summer', 2)
    # plt.imshow(data)
    # plt.colorbar()
    return data
