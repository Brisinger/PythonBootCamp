# Function scope
def upload(num, nums=[]):
    nums.append(num)
    return nums

# Checking the elements in nums list by calling function returning the list outside it's scope.
print(upload(2))
print(upload(3))