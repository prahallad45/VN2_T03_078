def t(nums):
    result = int(''.join(map(str,nums)))
    return result

nums = (1,2,3)
print("Original tuple: ") 
print(nums)

print(t(nums))
nums = (10,20,40,5,70)
print(t(nums))