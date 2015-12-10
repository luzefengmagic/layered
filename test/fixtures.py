import pytest
import numpy as np
from layered.activation import Linear, Relu, Sigmoid, Softmax
from layered.cost import Squared, CrossEntropy
from layered.network import Matrices, Layer, Network
from layered.utility import pairwise
from layered.example import Example


def random_matrices(shapes):
    np.random.seed(0)
    matrix = Matrices(shapes)
    print(matrix.shape)
    matrix.flat = np.random.normal(0, 0.1, len(matrix.flat))
    print(matrix.shape)
    return matrix


@pytest.fixture(params=[(5, 5, 6, 3)])
def weights_and_gradient(request):
    shapes = list(pairwise(request.param))
    weights = random_matrices(shapes)
    gradient = random_matrices(shapes)
    return weights, gradient


@pytest.fixture(params=[Linear, Relu, Sigmoid, Softmax])
def network_and_weights(request):
    np.random.seed(0)
    layers = [Layer(5, Linear)] + [Layer(5, request.param) for _ in range(3)]
    network = Network(layers)
    weights = Matrices(network.shapes)
    weights.flat = np.random.normal(0, 0.01, len(weights.flat))
    return network, weights


@pytest.fixture
def example():
    data = np.array(range(5))
    label = np.array(range(5))
    return Example(data, label)


@pytest.fixture
def examples():
    examples = []
    for i in range(7):
        data = np.array(range(5)) + i
        label = np.array(range(5)) + i
        examples.append(Example(data, label))
    return examples


@pytest.fixture(params=[Squared, CrossEntropy])
def cost(request):
    return request.param()
