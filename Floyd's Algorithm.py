# Find Duplicate Number

# Given an array nums containing n + 1 where each integer is between 1 and n (inclusive).
# Prove that at least one duplicate number must exist.
# Assume that there is only one duplicate number but it could only be repeated more than once.
# Find the duplicate number.

# In order to answer this we need to use Floyd's Algorithm.

#________________________________________________________________________________________________




def findDuplicate(nums):
    turtle = nums[0]
    hare = nums[0]
    while True:
        turtle = nums[turtle]
        hare = nums[nums[hare]]
        if turtle == hare:
            break



    ptr1 = nums[0]
    ptr2 = turtle
    while ptr1 != ptr2:
        ptr1 = nums[ptr1]
        ptr2 = nums[ptr2]

    return ptr1



print(findDuplicate([3,1,3,4,2]))
