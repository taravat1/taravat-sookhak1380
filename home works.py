number=[1,2,3,7,5.4]

for i in range(0 , len(number)):
    for j in range(0 , len(number)):
        if number[i] <= number[j]:
            temp=number[i]
            number[i]=number[j]
            number[j]=temp
print(number)