import matplotlib.pyplot as plt


squares = [1, 4, 9, 16, 25]

def squared_linegraph(values):
    input_values = [1, 2, 3, 4, 5]

    plt.style.use('seaborn')
    fig, ax = plt.subplots()
    ax.plot(squares, linewidth = 3)

    #Setting chart title and label axes. 
    ax.set_title ("Square Numbers", fontsize = 24)
    ax.set_xlabel ("Value", fontsize = 14)
    ax.set_ylabel ("Square of Value", fontsize = 14)

    #Setting size of tick labels. 
    ax.tick_params (axis = 'both', labelsize = 14)

    plt.show()

#squared_linegraph(squares)



x_values = [1, 2, 3, 4, 5]
y_values = [1, 4, 9, 16, 25]

def scatterplot_graph (value_set1, value_set2):
    plt.style.use('seaborn-dark')
    fig, ax = plt.subplots()
    ax.scatter (value_set1, value_set2, c='purple', s = 100)

    #Setting Chart Title and Axis Labels
    ax.set_title("Square Numbers", fontsize = 24)
    ax.set_xlabel("Value", fontsize = 14)
    ax.set_ylabel("Square of Values", fontsize = 14)

    #Setting Tick Labels
    ax.tick_params(axis = 'both', which = 'major', labelsize = 14)

    plt.show()

#scatterplot_graph(x_values, y_values)



def auto_calculating_data ():
    x_values = range (1, 1001)
    y_values = [x**2 for x in x_values]

    plt.style.use('seaborn')
    fig, ax = plt.subplots()
    ax.scatter (x_values, y_values, c=y_values, cmap=plt.cm.Blues, s = 10)

    #Setting chart title and label axes.
    ax.set_title("Square Numbers", fontsize = 24)
    ax.set_xlabel("Value", fontsize = 14)
    ax.set_ylabel("Square of Values", fontsize = 14)

    #Setting range for each axis.
    ax.axis([0, 1100, 0, 1100000])

    plt.show()

#auto_calculating_data()



xVal = range(0, 100)
yVal = [x**3 for x in xVal]

def cubes (dataSet1, dataSet2):

    plt.style.use('seaborn')
    fig, ax = plt.subplots ()
    ax.scatter (dataSet1, dataSet2, c='purple', s = 10)

    ax.set_title("Cubed Numbers", fontsize = 24)
    ax.set_xlabel("Value", fontsize = 14)
    ax.set_ylabel("Cube of Values", fontsize = 14)

    ax.axis([0, 30, 0, 400])

    plt.show()

#cubes(xVal, yVal)