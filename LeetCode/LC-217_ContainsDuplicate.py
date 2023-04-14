import time

def containsDuplicate(nums):
    nums.sort()
    walker = 0
    for i in nums:
        if (walker + 1) <= (len(nums) - 1):
            if nums[walker + 1] == nums[walker]:
                return True
        
        else:
            return False
        walker += 1

nums = [3, 3]
print(containsDuplicate(nums))

