def findMaxInList(numbers):
    # your code goes here
    max_value = numbers[0]
    for each in numbers:
          if each > max_value:
            max_value = each
    return max_value

List = [4, 1, 11, 2, 15]
findMaxInList(List)
print(findMaxInList(List))