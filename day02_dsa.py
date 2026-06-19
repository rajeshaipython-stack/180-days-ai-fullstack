# DSA = Data Structures & Algorithms.
# DSA Problem 1 — Sum of a list
nums = [4,8,16,32,42]
total = 0
for n in nums:
    total = total + n
print("sum:", total)

# DSA Problem 2 — Find the largest number (using a loop, not the built-in max()).
nums = [ 4,8,15,16,23,42]
largest = nums[0]
for n in nums:
    if n > largest:
        largest = n
        print("largest:", largest)

#DSA Problem 3 — Reverse a list (without the [::-1] shortcut).
nums = [4,8,15,16,23,42]
reversed_list =[]
for n in nums:
    reversed_list.insert(0,n)
print("reversed list:", reversed_list)