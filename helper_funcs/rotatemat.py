A = [[8, 5], [9, 2], [3, 4]]
# 8 5
# 9 2
# 3 4
print(A)

print(list(zip(*A)))

# rotate mat clockwise
print(list(zip(*A[::-1]))) 
# 3 9 8
# 4 2 5