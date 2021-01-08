import numpy as np

class NeuralNetwork:
    
    def __init__(self):
        np.random.seed(1)
        self.weights = 2 * np.random.random((2, 1)) - 1  # 2 to chyba liczba parametrów danych wejściowych

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def d_sigmoid(self, x):
        return x * (1 - x)

    def train(self, train_input, train_output, train_iters):
        for _ in range(train_iters):
            propagation_result = self.propagation(train_input)
            self.backward_propagation(
                propagation_result, train_input, train_output)

    def propagation(self, inputs):
        return self.sigmoid(np.dot(inputs.astype(float), self.weights))

    def backward_propagation(self, propagation_result, train_input, train_output):
        error = train_output - propagation_result
        self.weights += np.dot(
            train_input.T, error * self.d_sigmoid(propagation_result)
        )

    # zapis sieci
    def saveNetwork(self):
        np.save( './neuralnet/weights.npy' , self.weights )

    # odczyt sieci z pliku
    def load(self):
        self.weights = np.load( './neuralnet/weights.npy' )


if __name__=='__main__':
    # przykładowe użycie NeuralNetwork 
    network = NeuralNetwork()
    print(network.weights)
    print()

    train_inputs = np.array([[2, 3],
                            [1, 1],
                            [3, 1],
                            [2, 2],
                            [1, 0],
                            [3, 2]]) 

    train_outputs = np.array([[8], [1], [3], [4], [1], [9]])

    train_iterations = 50000

    network.train(train_inputs, train_outputs, train_iterations)

    print(network.weights)

    test_data = np.array([[0, 0], [1, 1]])

    print("Test zapisu i odczytu wag sieci")
    network.saveNetwork()
    otherNetwork = NeuralNetwork()
    otherNetwork.load()

    for data in test_data:
        print(f"Result for {data} is:")
        print(otherNetwork.propagation(data))
    pass