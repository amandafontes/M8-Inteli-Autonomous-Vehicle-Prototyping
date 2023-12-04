import numpy as np

class Perceptron:

    # Função de inicialização do perceptron
    def __init__(self, learning_rate=0.1, n_iterations=100, threshold=0.5):
        self.learning_rate = learning_rate
        self.n_iterations = n_iterations
        self.threshold = threshold
        self.weights = np.zeros(2)
        self.bias = 0

    # Função de ativação do perceptron
    def activation_function(self, x):
        return 1 if x >= self.threshold else 0

    # Função de predição do perceptron
    def predict(self, inputs):

        # Calcula a soma ponderada das entradas
        linear_output = np.dot(inputs, self.weights) + self.bias
        
        # Aplica a função degrau para determinar a saída
        y_predicted = self.activation_function(linear_output)
        return y_predicted
    
    def train(self, X, y):
        for _ in range(self.n_iterations):
            for inputs, label in zip(X, y):
                prediction = self.predict(inputs)
                error = label - prediction
                self.weights += self.learning_rate * (label - prediction) * inputs
                self.bias += self.learning_rate * (label - prediction)

if __name__ == "__main__":

    # Define a entrada de treinamento
    X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])

    # Define a saída de treinamento
    y = np.array([0, 1, 1, 0])

    # Define o perceptron
    perceptron = Perceptron()

    # Treina o perceptron
    perceptron.train(X, y)
    
    # Testa o perceptron
    print(perceptron.predict(np.array([0, 0])))
    print(perceptron.predict(np.array([0, 1])))
    print(perceptron.predict(np.array([1, 0])))
    print(perceptron.predict(np.array([1, 1])))