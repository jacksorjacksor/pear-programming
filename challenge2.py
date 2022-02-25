# Working as a pair/swarm write two separate functions (and accompanying tests to prove
# your functions work) that compute the sum of the numbers in a given list using a for-loop,
# and a while-loop


# # 1 for-loop
sum = 0

for n in list_of_numbers:
    sum += n

print(sum)

# # 2 while-loop

length_of_list = len(list_of_numbers)

i = 0
sum_2 = 0

while i < length_of_list:
    number_of_that_index = list_of_numbers[i]
    sum_2 += number_of_that_index
    i += 1

print(sum_2)

# if sum == sum_2:
#     print("GO TEAM!!!")
# else:
#     print("NOOOOOOOOO")


list_of_numbers = [1, 2, 3, 4, 5, 6, 7]


def recursion_version(list_of_numbers):
    # Reduction step
    if len(list_of_numbers) > 1:
        return list_of_numbers[0] + recursion_version(list_of_numbers[1:])
    # End step
    else:
        return list_of_numbers[0]


print(recursion_version(list_of_numbers))
