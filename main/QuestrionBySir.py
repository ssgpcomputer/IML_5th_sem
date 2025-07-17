import numpy as np

even = np.arange(2, 101, 2)
one = np.ones(100)

meanEven = np.mean(even)
meanOne = np.mean(one)

stdEven = np.std(even)
stdOne = np.std(one)

varEven = np.var(even)
varOne = np.var(one)

print("Even numbers array:", even)
print("Mean of even numbers:", meanEven)
print("Standard deviation of even numbers:", stdEven)
print("Variance of even numbers:", varEven)

print("\nArray of ones:", one)
print("Mean of ones:", meanOne)
print("Standard deviation of ones:", stdOne)
print("Variance of ones:", varOne)
