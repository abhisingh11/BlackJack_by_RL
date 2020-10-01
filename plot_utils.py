import numpy as np
import matplotlib.pyplot as plt

def plot_values(V):
	# reshape value function
	V_sq = np.reshape(V, (4,4))
	
	# plot the state-value function
	# so that its easy to read !
	fig = plt.figure(figsize=(7, 7))
	#figure size changes to 7 by 7
	ax = fig.add_subplot(111)
	im = ax.imshow(V_sq, cmap='blue')
	for (j,i),label in np.ndenumerate(V_sq):
	    ax.text(i, j, np.round(label, 5), ha='center', va='center', fontsize=14)
	plt.tick_params(bottom=False, left=False, labelbottom=False, labelleft=False)
	plt.title('State-Value Function')
	plt.show()
	
	
