import activations
import numpy as np

class DenseLayer:
  def __init__(self, input_shape, units=None, activation=None, name="Dense"):
    self.input_shape = input_shape
    self.units = units
    self.activation=activations.get(activation)
    self.name = name
  def build(self, input_shape):
    self.weight = np.random.randn(input_shape[-1], self.units) 
    self.bias = np.random.randn(self.units)
    
  def feed_forward(self, input):
    z = np.matmul(input, self.weight) + self.bias
    z = self.activation(z)
    return z
  
  def compute_output_shape(self):
    output_shape = list(self.input_shape)
    output_shape[-1] = self.units
    return tuple(output_shape)