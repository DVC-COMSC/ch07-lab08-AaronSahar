inputvalues = input()
numbers = inputvalues.split()
for i in range(len(numbers)):
	numbers[i] = int(numbers[i]) 
    

insert_number = int(input())

for i in range(len(numbers)):
    if insert_number < numbers[i]:
        numbers.insert(i, insert_number)
        break
for i in range(len(numbers)):
    print(numbers[i], end=' ')