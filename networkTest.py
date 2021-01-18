import numpy as np
import NeuralNetwork as nn
from test import training_animals
from test import test_animals

cats = training_animals("cat", 1, 10)
dogs = training_animals("dog", 1, 10)

test_data = test_animals(20, 25)

network = nn.NeuralNetwork(300)
print(network.weights)
print()

train_inputs = cats + dogs 

# żałosny kod na próbę
def catOrDog(i):
    if i < 10 :
        return 0 # dla kota
    else:
        return 1 # dla psa

train_outputs = np.array([[catOrDog(i) for i in range(1, 21)]])
train_iterations = 50000
network.train(train_inputs, train_outputs, train_iterations)

print(network.weights)

for data in test_data:
    print(f"Result for {data} is:")
    print(network.propagation(data))