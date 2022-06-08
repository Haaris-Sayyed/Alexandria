# Lists are mutable.

# https://docs.python.org/3/tutorial/datastructures.html#more-on-lists 

nums = ['one', 'two', 'three', 'four', 'five']

print(nums[1])

print(nums)

nums.append('six') 
print(nums)

print(nums.index('four'))

nums.insert(0,'zero')
print(nums)

nums.remove('zero')
print(nums)

print(nums.pop())

print(nums[1:5:2])

print(' , '.join(nums))

print(len(nums))

# Tuples are immutable.

nums = ('one', 'two', 'three', 'four', 'five')

print(nums[1])

print(nums)

print(nums.index('four'))

print(nums[1:5:2])

print(' , '.join(nums))

print(len(nums))
