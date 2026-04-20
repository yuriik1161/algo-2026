def two_sum(numbers, target):    
    seen = {}
    for i, num in enumerate(numbers):
        diff = target - num
        if diff in seen:
            return [seen[diff], i]
        seen[num] = i
    return [-1]

print("Two Sum")
nums = input("Числа: ")
nums = [int(x) for x in nums.split(",")]
t = int(input("Target: "))
print("Відповідь:", two_sum(nums, t))

print()
