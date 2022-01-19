import matplotlib.pyplot as plt
from Random_Walk import RandomWalk

# Keep making new walks, as long as the program is active. 

def pollen_walk():
    while True:
        rw = RandomWalk(5000)
        rw.fill_walk()

        #Plotting the points in the walk.
        plt.style.use('classic')
        fig, ax = plt.subplots(figsize=(15, 9))
        point_numbers = range(rw.num_points)
        ax.plot(rw.x_values, rw.y_values, c='purple', linewidth=3)

        #Setting title, axes and ticks.
        ax.set_title('Pollen Drift', fontsize=24)
        ax.set_xlabel('x axis', fontsize=14)
        ax.set_ylabel('y axis', fontsize=14)
        ax.tick_params(axis='both', labelsize=14)

        plt.show()

        keep_running = input("Make another walk? (y/n): ")
        if keep_running == 'n': 
            return
pollen_walk()
