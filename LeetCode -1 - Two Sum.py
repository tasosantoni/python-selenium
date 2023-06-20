# Leetcode - 1 - Two Sum

def twoSum(nums, target):
    map = {}

    for i in range(len(nums)):
        x = target - nums[i]

        if x in map.keys():
            print('The two numbers have been found!')
            return [map[x], i]
        else:
            map.setdefault(nums[i], i)

    print('There is no pair of integers that sums up to tagret!')
    return [None,None]

numbers = [2,54,8,1,3,5,98,13,25]
targ = 100
ind = twoSum(numbers, targ)
if ind[0] != None and ind[1] != None:
    print('Numbers ' + str(numbers[ind[0]]) + ' and ' + str(numbers[ind[1]]) + ' sum up to ' + str(targ))

