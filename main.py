inputvalues = input('Enter 5 elements values in ascending order: ')
numbers = inputvalues.split()
for i in range(len(numbers)):
	numbers[i] = int(numbers[i]) 
    
while sorted(numbers) != numbers or len(numbers) > 5:
    print('Invalid input')
    inputvalues = input('Enter 5 elements values in ascending order: ')
    numbers = inputvalues.split()
    for i in range(len(numbers)):
	    numbers[i] = int(numbers[i]) 

insert_number = int(input('Enter the number to insert: '))

for i in range(len(numbers)):
    if insert_number < numbers[i]:
        numbers.insert(i, insert_number)
        break
    if i == 4:
        numbers.insert(i+1, insert_number)

print(numbers)