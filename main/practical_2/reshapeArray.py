import numpy as np

lists = [[1,3],[5,6],[7,8]]
Array = np.array(lists)
end = Array.reshape(2,3)

print(f"Before reshape :\n {Array}")
print(f"After reshape :\n {end}")