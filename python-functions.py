# 1. Write a function named sum_to that accepts a single integer, n, and returns the sum of the integers from 1 to n.

def sum_to(n):
  total = 0
  for num in range(n):
    total += num
  return total + n

sum_to(10)


# 2. Write a function named largest that takes a list of numbers as an argument and returns the largest number in that list.

def largest(num_list):
  return max(num_list)

largest([1, 2, 25, 4, 99])

# 3. Write a function named occurrences that takes two string arguments as input and counts the number of occurrences of the second string inside the first string.

def occurences(string1, string2):
  count = 0
  if string1 in string2:
    count += 1
  print(count)

occurences('fleep floop', 'e')