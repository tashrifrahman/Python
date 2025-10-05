def two_sum(nums, target):
    num_map = {}  # stores number as key and its index as value
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i

num = list(map(int, input("nums = ").split()))
target = int(input("target = "))
result = two_sum(num, target)
print(result)
