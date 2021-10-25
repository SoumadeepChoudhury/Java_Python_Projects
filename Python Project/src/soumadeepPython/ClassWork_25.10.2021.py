# # Print the series 1,-4,7,-10....-40
k = 1
for i in range(1, 41, 3):
    print(i*k, end=" ")
    k *= -1
