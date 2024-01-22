import numpy as np
import math 


class Activation:
  
  def call(x):
    return x;
  def dx(x):
    return 1;
  

  
class Sigmoid(Activation):
  def call(x):
    return 1 / (1 + np.exp(-x))
  def dx(self, x):
    return self.call(x) * (1 - self.call(x))

class ReLu(x):
  def call(x):
    return np.maximum(0, x)
  def dx(x):
    return np.where(x > 0, 1, 0)

  
