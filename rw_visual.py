import matplotlib.pyplot as plt
from randomwalk import Ramdomwalk

rw = Ramdomwalk(num_pionts=3000)
rw.fillwalk()

plt.style.use('classic')
fig,ax = plt.subplots()
ax.scatter(rw.x_value,rw.y_value,s=7,c='green')

plt.show()