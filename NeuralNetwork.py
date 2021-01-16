import numpy as np
from test import training_animals

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
    # print(network.weights)
    # print()

    # wyciagamy sto zdjec kotow i psow (kazde to tablica o wielkosci 90000)

    print("wczytujemy koty")
    koty = np.array(training_animals('cat'))
    print("wczytujemy psy")
    psy = np.array(training_animals('dog'))

    # 90 pierwszych kotow i psow idzie do trenowania sieci

    train_inputs = []
    train_outputs = []
    for i in range(90):
        train_inputs.append(koty[i])
        train_outputs.append([0])
        train_inputs.append(psy[i])
        train_outputs.append([1])

    # output na wyjsciu rowny 0 oznacza kota, 1 oznacza psa

    train_iterations = 50000

    np_train_inputs = np.array(train_inputs)
    np_train_outputs = np.array(train_outputs)

    network.train(np_train_inputs, np_train_outputs, train_iterations)

    # print(network.weights)

    # na pozostalych sprawdzamy

    test_data = []
    for i in range(90, 100):
        test_data.append(koty[i])
        test_data.append(psy[i])

    np_test_data = np.array(test_data)

    print("Test zapisu i odczytu wag sieci")
    # network.saveNetwork()
    # otherNetwork = NeuralNetwork()
    # otherNetwork.load()

    for data in test_data:
        print(f"Result for {data} is:")
        print(network.propagation(data))
    pass
