 #arthimetic operators 
print("sum:", 4 + 3 )
print("difference:", 4 - 3)
print("product:", 4*3)
print("division:", 4/3)
print(" floor division:", 4//3)
print("reminder:", 4%3)
print("exponentionation:", 4**3)

#assignment operators 
n1=5
n2=n1
print(n1,n2)

n2+= n1 
print(n1,n2) 

n2*= n1 
print(n1,n2)

#comparison opertors 
n1=4
n2=3
print(n1>n2)

#logical operators
exp1= 2>1
exp2= 5<4
print("exp1 and exp2:", exp1  and exp2)
print("exp1 or exp2:", exp1 or exp2)
print("not exp1 :",not exp1)

#identity operators 
x = 5 
y = 5
print("if x is y:", x is y )
print ("if x is y:", x is not y)

#membership operators 
fruits=["apple","banana","cherry"]
print("if banana is present in fruits:", "banana" in fruits)
print("if mango is not present in fruits:", "mango" not in fruits)

#bitwise operators
a = 5 
b = 3
print("a and b:", a&b)
print("a or b:", a|b)
print("a xor b:", a^b)