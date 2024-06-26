n = int(input("Enter n: "))

for i in range(1,n+1): #loops for rows 
    for j in range(1,i+1): #loops for columns
        print(j, end="")
    print()  