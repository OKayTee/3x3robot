import numpy as np 
from colorgrab import grab

data = grab()

weights = np.array([[np.random.randn() for i in range(5)]for i in range(6)])

def sigmoid(x):
    return 1/(1+np.exp(-x))

def sigmoid_p(x):
    return x*(1-x)
    
#training loop

for i in range (100000):
    ri = np.random.randint(2400)
    inpdata =np.array([data[ri][0],data[ri][1],data[ri][2],data[ri][3],data[ri][5]])
    inpdata.reshape(5,1)
    learningrate = 0.001
    correct = data[ri][6]

    colors = [0,0,0,0,0,0]
    colors = weights.dot(inpdata)
    predictions = [sigmoid(color)for color in colors]
    prediction = predictions.index(max(predictions))
    
    #print(prediction)
    error =0
    adjustments = 0
    for i in range(5):
        if i == prediction:
            error =  (1-prediction) ** 2
            adjustments = error*sigmoid_p(predictions[i])
            weights[i] = weights[i]+(learningrate * adjustments)     
       # else:
           # error =  0-predictions[i]
           # adjustments = error*sigmoid_p(predictions[i])
            #weights[i] = weights[i]+(learningrate * adjustments)  
print(correct)
print(predictions)
print(prediction)
print(weights)
