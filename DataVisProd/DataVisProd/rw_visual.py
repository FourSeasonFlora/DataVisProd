import matplotlib.pyplot as plt
from Random_Walk import RandomWalk

#Make a random_walk.
rw = RandomWalk()
rw.fill_walk()

#Plotting the points in the walk.
plt.style.use('classic')
fig, ax = plt.subplots()
ax.scatter(rw.x_values, rw.y_values, s=15)
plt.show()
