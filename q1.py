
print("Enter value of x , y & z for vector 1 - \n")
vector_1 = []
vector_2 = []

for(i in range(3)):
	x = int(input("-"))
	vector_1.append(x)

print("Enter value of x , y & z for vector 2 0 \n")
for(j in range(3)):
	x = int(input("-"))
	vector_2.append(x)

result = []

for(i in range(3)):
	result.append(vector_1[i]*vector_2[i])

print("Result : ",result)

