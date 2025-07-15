import numpy as np

lists = [1,23,4,5,6,7,8,6,87]
Array = np.array(lists)
end = np.append(Array,[43,23,26])

print(f"Before Append : {Array}")
print(f"After Append : {end}")