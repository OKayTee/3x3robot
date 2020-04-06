import numpy as np 
from colorgrab import grab

data = grab()

weights = np.array([[np.random.randn() for i in range(5)]for i in range(6)])

def sigmoid(x):
    return 1/(1+np.exp(-x))

def sigmoid_p(x):
    
#training loop

for i in range (1):
    ri = np.random.randint(2400)
    inpdata =np.array([data[ri][0],data[ri][1],data[ri][2],data[ri][3],data[ri][5]])
    inpdata.reshape(5,1)
    
    correct = data[ri][6]

    colors = [0,0,0,0,0,0]
    colors = weights.dot(inpdata)
    predictions = [sigmoid(color)for color in colors]
    print(correct)
    print(colors)
    print(predictions)