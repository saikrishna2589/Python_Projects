#enter the numbers with spaces in between

user_input = input("Enter the numbers with spaces inbetween:\n")

print(type(user_input))

print(user_input)
list_of_numbers = user_input.split()

number_count = len(list_of_numbers)

print(list_of_numbers)



#converting to number format
number_format = [int(number) for number in list_of_numbers]
print(number_format)

#sum of numbers
sum_of_numbers = sum(number_format)

#range of numbers

max_number = max(number_format)
min_number = min(number_format)
range_numbers = max_number - min_number

#most frequent number
number_dictionary ={}

for numb in list_of_numbers:
    if numb in number_dictionary:
        number_dictionary[numb] +=1
    else:
        number_dictionary[numb] =1

print(number_dictionary)

most_frequent_number = max(number_dictionary , key =number_dictionary.get)
Average_number = sum_of_numbers/ number_count


print(f"Total Numbers: {number_count}")
print(f"Sum of Numbers: {sum_of_numbers}")
print(f"Range of Numbers: {range_numbers}")
print(f"most frequent number is '{most_frequent_number}' (used {number_dictionary[most_frequent_number]} times)")
print(f"Average value of user inputted numbers is {Average_number}")