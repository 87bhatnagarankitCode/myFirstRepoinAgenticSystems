
import numpy as np
import os

os.system('cls')

np.random.seed(42)

data = np.random.randint(0,100,(100,3))
mean = data.mean( axis= 0)
std  = data.std( axis =0 )
#print("array>> \n",data)
#print("\n Mean", mean)
#print("Std", std)

normalized = (data - mean) / std

#print("\n normalized", normalized, "\n datatype",type(normalized))

arraySlicing = int(normalized.shape[0] * 80/100)
training_set = normalized[:arraySlicing]

test_set    = normalized[arraySlicing:]

another_test_set = normalized[arraySlicing:].copy()

print("Original data shape : ", (data.shape) )
print("Mean shape : ",  ( mean.shape) )
print("Standard deviation : ", ( std.shape))
print("Training data shape : ", (training_set.shape)) 
print("Test data shape : ", (test_set.shape))

print("Test data before : \n",test_set)
test_set[0:5] = ".99"
print(" !!!!!! Modifying the slice affected the original array.!!!!!")
print("Test data after : \n", test_set )

print(" Another test set (copy): \n", another_test_set)
print(" Original Data (modified due to views change)  : \n", normalized )