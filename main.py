inputvalues = input('Enter 5 elements values in ascending order: ')

numbers = inputvalues.split()
for i in range(len(numbers)):
	numbers[i] = int(numbers[i]) 

insert_number = int(input('Enter the number to insert'))

for i in range(len(numbers)):
    if insert_number < numbers[i]:
        numbers.insert(i, insert_number)
        break

print(numbers)