import tensorflow as tf
import numpy as np
a = np.array([[1,2], [3,4]]) 
b = np.array([[11, 12], [13, 14]])
c=tf.tensordot(a,b,axes=True)
print(c)
print(type(a))
print(type(c))