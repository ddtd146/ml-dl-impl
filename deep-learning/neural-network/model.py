import numpy as np

class NeuralNetwork:
  def __init__(self):
    self.layers = []
  def add(self, layer):
    self.layers.append(layer)
  def pop(self):
    self.layers.pop()
    
  def compile(self, loss):
    self.loss = loss
  def predict(self, x):
    _x = x
    for layer in self.layers:
      _x = layer.feed_forward(_x)
    return _x
  def fit_partial(self, x, y):
    A = [x]
    out = A[i-1]
    # feedforward
    for i in range(0, len(self.layers) - 1):
      out = self.layers[i].feed_forward(out)
      A.append(out)
      
    #backpropagation
    y = y.reshape(-1, 1)
    dA
    
  def fit(self, x, y, epochs, learning_rate=0.001):
    for i in epochs:
      self.fit_partial(x, y)