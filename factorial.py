fact=1
n=int(input("Enter number for factorial: "))
for i in range(n,0,-1):
  fact=fact*i
print('factorial',fact)